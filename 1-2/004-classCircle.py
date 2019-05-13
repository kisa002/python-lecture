class Circle(object):
    radius = -1
    cx = -1
    cy = -1

    def __init__(self, radius, cx, cy):
        self.radius = radius
        self.cx = cx
        self.cy = cy

    def GetArea(self):
        return float(self.radius ^ 2) * 3.14

    def GetCenter(self):
        return "x: " + str(self.cx) + "\ny: " + str(self.cy)

circle = Circle(5, 6, 8)
print("[Area]\n" + str(circle.GetArea()))
print("[Center]\n" + str(circle.GetCenter()))