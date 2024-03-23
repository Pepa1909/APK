from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from math import *


#Processing data 
class Algorithms:
    
    def __init__(self):
        pass
    
    def rayCrossingAlgorithm(self, q:QPointF, pol:QPolygonF):
        
        #Inicialize amount of right-sided intersections
        kr = 0
        
        #Inicialize amount of left-sided intersections
        kl = 0
        
        #Amount of vertices
        n = len(pol)
        
        #Process all segments
        for i in range(n):
            
            #Reduce coordinates
            xi = pol[i].x() - q.x()
            yi = pol[i].y() - q.y()
            
            #Check if point is located on a vertex
            if xi == 0 and yi == 0:
                return -1

            #Reduce coordinates of the next vertex
            xi1 = pol[(i+1) % n].x() - q.x()
            yi1 = pol[(i+1) % n].y() - q.y()

            #Check for horizontal edge
            if (yi1 - yi) == 0:
                continue
            
            #Compute intersection of ray and edge
            xm = (xi1 * yi - xi * yi1) / (yi1 - yi)

            #Process lower segment
            if (yi1 < 0) != (yi < 0):
                #Increment the number of left intersections if xm is on the left
                if xm < 0:
                    kl += 1

            #Process upper segment
            if (yi1 > 0) != (yi > 0):
                #Increment the number of right intersections if xm is on the right
                if xm > 0:
                    kr += 1
        
        #Point q on edge
        if kl % 2 != kr % 2:
            return -1
        
        #Point q inside polygon
        elif kr % 2 == 1:
            return 1
        
        #Point q outside polygon
        else:
            return 0


    def windingNumberAlgorithm(self, q:QPointF, pol:QPolygonF):
        
        #Amount of vertices
        n = len(pol)
        
        #Sum of angles
        total_angle = 0
        
        #Very small positive treshold values close to 0
        eps = 1.0e-10

        #Process all segments
        for i in range(n):
            
            #Check if point is located on a vertex
            if (q == pol[i]) or (q == pol[(i + 1) % n]):
                return -1
            
            #Compute: vertex i+1 - vertex i
            ux = pol[(i+1) % n].x() - q.x()
            uy = pol[(i+1) % n].y() - q.y()
            
            #Compute: point q - vertex i
            vx = q.x() - pol[i].x()
            vy = q.y() - pol[i].y()
            
            #Compute determinant to analyze position of the point
            det = (ux * vy) - (vx * uy)

            #Compute vector u: point q - vertex i
            ux = pol[i].x() - q.x()
            uy = pol[i].y() - q.y()

            #Compute vecotr v: point q - vertex i+1
            vx = pol[(i+1) % n].x() - q.x()
            vy = pol[(i+1) % n].y() - q.y()

            #Compute angle of vectors u and v
            angle = Algorithms.computeAngle(ux, uy, vx, vy)

            #Determinant determines the addition/subtraction of angle to the totalAngle
            if det > 0:
                total_angle += angle
            elif det < 0:
                total_angle -= angle

            #Point q on edge
            if det == 0 and abs(angle - pi) < eps:
                return -1
            
        #Point q inside polygon
        if abs(abs(total_angle) - 2*pi) < eps:
            return 1
        #Point q outside polygon
        return 0


    #Computing the angle between two vectors
    def computeAngle(ax, ay, bx, by):
        dot = ax * bx + ay * by
        mod = abs(sqrt(ax**2 + ay**2) * sqrt(bx**2 + by**2))
        omega = dot / mod
        if omega > 1:
            omega = 1
        return abs(acos(omega))