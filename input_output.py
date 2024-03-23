from PyQt6.QtCore import *
from PyQt6.QtGui import *
#from PyQt6.QtGui import QMouseEvent, QPaintEvent
from PyQt6.QtWidgets import *
import json

def read_pnts(pnt_list : list):
    coords = []
    for part in pnt_list:
        if type(part) == list and (type(part[0]) == float or type(part[0]) == int):
            if (part[0], part[1]) in coords:
                continue
            else:
                #print('appending: ', part[0], part[1])
                coords.append((part[0], part[1]))
                '''for vertex in part:
                    pnts.append(QPointF(vertex[0], vertex[1]))'''
        else:
            for pnt in read_pnts(part):
                coords.append(pnt)
    return coords

def loadJSON(file : str) -> list:
    with open(file, encoding = 'utf-8') as f:
        data = json.load(f)
    
    polygons = []
    for polygon in data['features']:
        '''try:
            coords = read_pnts(polygon['geometry']['rings'])      # extraction of coordinates ignores polygons parts, removes duplicate points
        except KeyError:
            try:
                coords = read_pnts(polygon['geometry']['curveRings'])      # extraction of coordinates ignores polygons parts, removes duplicate points
            except:
                raise SystemError('špatný geometry key')'''
        try:
            coords = read_pnts(polygon['geometry']['coordinates'])      # extraction of coordinates ignores polygons parts, removes duplicate points
        except:
            raise SystemError('Chyba při načítání')

        #print('polygon: ', coords)     
        q_pnts = [QPointF(i[0], i[1]) for i in coords]
        polygons.append(QPolygonF(q_pnts))

    #print('load JSON: ', polygons)
    return polygons
