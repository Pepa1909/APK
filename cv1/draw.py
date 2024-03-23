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
        self.mmb_list = []
        
        
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
        
        
        #Set graphical attribute for point
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
        
        #Return analyzed list of polygons
        return self.polyg_list
    
    def getMmb(self):
        
        #Return min-max box list of analyzed polygons
        return self.mmb_list
    
    
    def clearData(self):
        
        #Clear polygon list and min-max box list
        self.polyg_list = []
        self.mmb_list = []
        
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
    

    def resizePolygons(self, pol_list, xmin, ymin, xmax, ymax):
        
        #Resizes input data to fit to display
        canvas_height = self.frameGeometry().height()
        canvas_width = self.frameGeometry().width()
        
        #Iterate over each coordinate for repositioning
        for polygon in pol_list:
            for point in polygon:
                new_x = int((point.x() - xmin) * canvas_width/(xmax - xmin))
                new_y = int((point.y() - ymin) * canvas_height/(ymax - ymin))
                
                #Reposition coordinates accordingly
                point.setX(new_x)
                point.setY(new_y)
                
    def minMaxBox(self, pol: QPolygonF):
        #Returns min-max box of polygon
        
        #Find points with maximum coordinates
        px_min = min(pol, key = lambda k: k.x())
        px_max = max(pol, key = lambda k: k.x())
        
        py_min = min(pol, key = lambda k: k.y())
        py_max = max(pol, key = lambda k: k.y())
        
        #Create points of min-max box
        v1 = QPointF(px_min.x(), py_min.y())
        v2 = QPointF(px_max.x(), py_min.y())
        v3 = QPointF(px_max.x(), py_max.y())
        v4 = QPointF(px_min.x(), py_max.y())
        
        #Create min_max box
        box = QPolygonF([v1,v2,v3,v4])
        
        return box
    
    def loadData(self, data):
        
        #Loads input shapefile
        polygony = data.geometry
        
        #Initialize min and max coordinates to compute bounding box of file
        xmin = inf
        ymin = inf
        xmax = -inf
        ymax = -inf
        
        
        #Iterate over all polygons
        for polyg in polygony:
            
            #Create empty polygon
            pol = QPolygonF()
            
            #Check if polygon is really a polygon
            if polyg.geom_type == "Polygon":
                #Get coordinates of exterior
                x,y = polyg.exterior.coords.xy
            else:
                #Otherwise create convex hull and get exterior (for multipolygons)
                x,y = polyg.convex_hull.exterior.coords.xy  
                
            #Create a list of points
            coords = np.dstack((x,y)).tolist()
            
            #Iterate over every point and add it to polygon
            for i in coords[0]:
                p = QPointF(i[0],-i[1])
                pol.append(p)
                #Find bounding points of polygon
                xmin, ymin, xmax, ymax = self.findBoundingPoints(p, xmin, ymin, xmax, ymax)
            
            #Add polygon to list of polygons and set status to 0
            self.polyg_list.append(pol)
            self.polyg_status.append(0)
            
            #Create min-max box of polygon and add it to list of min-max boxes
            mmb = self.minMaxBox(pol)
            self.mmb_list.append(mmb)
            
        # Resize all polygons and min-max boxes according to the canvas size
        self.resizePolygons(self.polyg_list, xmin, ymin, xmax, ymax)
        self.resizePolygons(self.mmb_list, xmin, ymin, xmax, ymax)
        self.repaint()