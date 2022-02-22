# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         temp = Point(0, 0)
#         temp.x = self.x + other.x
#         temp.y = self.y + other.y
#         return temp

#     def __sub__(self, other):
#         temp = Point(0, 0)
#         temp.x = self.x - other.x
#         temp.y = self.y - other.y
#         return temp
    
#     def __str__(self):
#         return "({}, {})".format(self.x, self.y)

# a = Point(1, 2)
# b = Point(3, 4)
# c = a + b
# print(c)
# d = a - b
# print(d)

# Bai 2
# class Polygon():
#     def __init__(self, num_sides):
#         self.num_sides = num_sides
#         self.side_length = [0 for i in range(num_sides)]

#     def input(self):
#         for i in range(self.num_sides):
#             self.side_length[i] = float(input("Side length: "))
    
#     def output(self):
#         for i in range(self.num_sides):
#             print("Side length:", self.side_length[i])

# class Triangle(Polygon):
#     def __init__(self):
#         Polygon.__init__(self, 3)

#     def perimeter(self):
#         sum = 0
#         for i in range(self.num_sides):
#             sum += self.side_length[i]
#         print("Perimeter:", sum)

#     def area(self):
#         a, b, c = self.side_length
#         p = (a + b + c) / 2
#         area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
#         print("Area:", area)

# class Square(Polygon):
#     def __init__(self):
#         Polygon.__init__(self, 1)

#     def perimeter(self):
#         sum = 0
#         for i in range(self.num_sides):
#             sum = self.side_length[i] * 4
#         print("Perimeter:", sum)

#     def area(self):
#         a = self.side_length[0]
#         area = a ** 2
#         print("Area:", area)

# class Rectangle(Polygon):
#     def __init__(self):
#         Polygon.__init__(self, 2)

#     def perimeter(self):
#         sum = 0
#         for i in range(self.num_sides):
#             sum += self.side_length[i] * 2
#         print("Perimeter:", sum)

#     def area(self):
#         a, b = self.side_length
#         area = a * b
#         print("Area:", area)

# shape = input("Enter your shape: ")
# if shape == "triangle":
#     triangle = Triangle()
#     triangle.input()
#     triangle.perimeter()
#     triangle.area()
# elif shape == "square":
#     square = Square()
#     square.input()
#     square.perimeter()
#     square.area()
# elif shape == "rectangle":
#     rectangle = Rectangle()
#     rectangle.input()
#     rectangle.perimeter()
#     rectangle.area()