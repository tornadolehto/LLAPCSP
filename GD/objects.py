class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Vector:
    def __init__(self,p1: Point,p2: Point):
        self.p1 = p1
        self.p2 = p2

def ccw(A,B,C):
    return (C.y-A.y)*(B.x-A.x) > (B.y-A.y)*(C.x-A.x)

def intersects(v1: Vector,v2: Vector):
    return ccw(v1.p1,v2.p1,v2.p2) != ccw(v1.p2,v2.p1,v2.p2) and ccw(v1.p1,v1.p2,v2.p1) != ccw(v1.p1,v1.p2,v2.p2)


def get_intersection(v1: Vector, v2: Vector):
    return
#implement




class Body:
    def __init__(self,points: list,sprite):
        self.points = points
        self.sprite = sprite
        self.vectors = []
        for i in range(len(self.points)):
            if i == len(self.points) - 1:
                self.vectors.append(Vector(self.points[i],self.points[0]))
            else:
                self.vectors.append(Vector(self.points[i],self.points[i+1]))
    class Rectangle:
        def __init__(self,h,w,c:Point):
            return
        #make this implement super constructor while keeping hwc inputs

        