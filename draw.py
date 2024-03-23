from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtGui import QMouseEvent, QPaintEvent
from PyQt6.QtWidgets import *
from math import *
import numpy as np


class Draw(QWidget):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.q = QPointF(-100, -100)
        self.polyg_list = []
        self.polyg_status = []
        
        
    def mousePressEvent(self, e: QMouseEvent):
        
        #Get coordinates of q
        x = e.position().x()
        y = e.position().y()
        
        self.q.setX(x)
        self.q.setY(y)
        
        # Change statuses of all polygons to 0 (not highlighted)
        self.polyg_status = [0] * len(self.polyg_list)
        
        #Repaint screen
        self.repaint()
        
        
    def paintEvent(self, e: QPaintEvent):
        #Draw situation
        
        #Create new graphic object
        qp = QPainter(self)
        
        #Start drawing
        qp.begin(self)
        
        #Set graphical attributes
        qp.setPen(Qt.GlobalColor.black)
        
        #Repaint polygons based on their status
        for i in range(len(self.polyg_list)):
            #Paint cyan if point is on an edge or inside a polygon
            if self.polyg_status[i] == 1 or self.polyg_status[i] == -1 or self.polyg_status[i] == -2:
                qp.setBrush(Qt.GlobalColor.cyan)
            #Paint yellow if point is outside a polygon or no analysis has been done
            else:
                qp.setBrush(Qt.GlobalColor.yellow)
            qp.drawPolygon(self.polyg_list[i])
        
        
        #Set graphical attributes
        qp.setBrush(Qt.GlobalColor.red)
        
        #Draw point
        r = 5
        qp.drawEllipse(int(self.q.x() - r), int(self.q.y() - r), 2 * r, 2 * r)
        
        #End drawing
        qp.end()
            
            
    def getQ(self):
        
        #Return analyzed point
        return self.q
    
    
    def getPol(self):
        
        #Return analyzed polygon
        return self.polyg_list
    
    
    def clearData(self):
        
        #Clear polygon
        self.polyg_list = []
        
        #Shift point
        self.q.setX(-100)
        self.q.setY(-100)
        
        #Repaint screen
        self.repaint()
        
        
    def findBoundingPoints(self, p:QPointF, xmin, ymin, xmax, ymax):
        
        #Returns minimum and maximum coordinates of bounding box around input polygons
        if p.x() < xmin:
            xmin = p.x()
        if p.y() < ymin:
            ymin = p.y()
        if p.x() > xmax:
            xmax = p.x()
        if p.y() > ymax:
            ymax = p.y()
        return xmin, ymin, xmax, ymax
    

    def resizePolygons(self, xmin, ymin, xmax, ymax):
        
        #Resizes input data to fit to display
        canvas_height = self.frameGeometry().height()
        canvas_width = self.frameGeometry().width()
        
        #Iterate over each coordinate for repositioning
        for polygon in self.polyg_list:
            for point in polygon:
                new_x = int((point.x() - xmin) * canvas_width/(xmax - xmin))
                new_y = int((point.y() - ymin) * canvas_height/(ymax - ymin))
                
                #Reposition coordinates accordingly
                point.setX(new_x)
                point.setY(new_y)
                
    
    def loadData(self, data):
        
        #Loads input shapefile
        polygony = data.geometry
        
        #Initialize min and max coordinates to compute bounding box
        xmin = inf
        ymin = inf
        xmax = -inf
        ymax = -inf
        
        #
        for index, polyg in enumerate(polygony):
            
            #
            pol = QPolygonF()
            g = []
            
            
            for i in polygony:
                g.append(i)
            if polyg.geom_type == "Polygon":
                x,y = g[index].exterior.coords.xy
            else:
                x,y = g[index].convex_hull.exterior.coords.xy  
            coords = np.dstack((x,y)).tolist()
            for i in coords[0]:
                p = QPointF(i[0],-i[1])
                pol.append(p)
                xmin, ymin, xmax, ymax = self.findBoundingPoints(p, xmin, ymin, xmax, ymax)
            self.polyg_list.append(pol)
            self.polyg_status.append(0)
        self.resizePolygons(xmin, ymin, xmax, ymax)
        self.repaint()