import math as m

class Point:
    def __init__(self, x_coord, y_coord):
        self.coords = (x_coord, y_coord)
    
    def distance(self, dot_2):
        dot_1 = self.coords
        return m.dist(dot_1, dot_2)
    
    def change_coords(self, x_coord, y_coord):
        self.coords = (x_coord, y_coord)
