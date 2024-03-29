import math
def midpoint(x1,y1,x2,y2):
    return (x1+x2)/2, (y1+y2)/2
    
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def endpointmidpoint(x1, y1, x2, y2):
    return (2 * x2) - x1, (2 * y2) - y1
    
for i in range(50):
    which = int(input("1 for midpoint, 2 for distance, three for endpoint"))
    if which == 1:
        x1 = int(input())
        y1 = int(input())
        x2 = int(input())
        y2 = int(input())
        print(midpoint(x1, y1, x2, y2))
    elif which == 2:
        x1 = int(input())
        y1 = int(input())
        x2 = int(input())
        y2 = int(input())
        print(distance(x1, y1, x2, y2))
    elif which == 3:
        x1 = int(input())
        y1 = int(input())
        x2 = int(input())
        y2 = int(input())
        print(endpointmidpoint(x1, y1, x2, y2))
    
    
