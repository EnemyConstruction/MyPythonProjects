class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Абсцисса объекта: {self.x}\nОрдината объекта: {self.y}'
    
class Rect:

    def __init__(self, down_corner, upper_corner):
        self.down_corner = down_corner
        self.upper_corner = upper_corner

    def __str__(self):
        return f'Координаты нижнего правого угла прямоугольника: \n{self.down_corner}\nКоординаты верхнего левого угла прямоугольника: \n{self.upper_corner}'
    
    def sides(self):
        horizontal = abs(self.down_corner.x - self.upper_corner.x)
        vertical = abs(self.down_corner.y - self.upper_corner.y)
        return horizontal, vertical
    
    def perim(self):
        horizontal, vertical = self.sides()
        print(f"Периметр прямоугольника равен {2*horizontal + 2*vertical}")


down_corner = Point(3, 8)
upper_corner = Point(-3, 3)

print(str(down_corner))
print(str(upper_corner))

rect1 = Rect(down_corner, upper_corner)
print(str(rect1))

print(rect1.sides())
rect1.perim()