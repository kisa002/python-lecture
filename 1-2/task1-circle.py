class Circle(object):
    radius = -1
    cx = -1
    cy = -1

    def __init__(self, radius, cx, cy):
        self.radius = radius
        self.cx = cx
        self.cy = cy

    def area(self):
        return float(self.radius ^ 2) * 3.14

    def center(self):
        return "position: {0}, {1}".format(self.cx, self.cy)

circle = Circle(5, 6, 8)
print("[Area]\n" + str(circle.area()) + "\n")
print("[Center]\n" + str(circle.center()))