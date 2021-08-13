#Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.
#A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side. 

def shapeArea(n):
    area=0
    level=1
    for i in range(n):
        if i<n-1:
            area=area+level*2
        else:
            area=area+level
        level+=2
    return area
