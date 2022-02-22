# Bai 1
# class Rectangle():
#     def __init__(self, height, width):
#         self.height = height
#         self.width = width

#     def __str__(self):
#         return "Rectangle object with height = {} and width = {}".format(self.height, self.width)

# rect = Rectangle(2, 1)
# print(rect)

# Bai 2
# class MathList():
#     def __init__(self, values):
#         self.values = values

#     def __add__(self, other):
#         return MathList([self.values[i] + 2 for i in range(len(self.values))])

#     def __sub__(self, other):
#         return MathList([self.values[i] - 2 for i in range(len(self.values))])

#     def __str__(self):
#         return str(self.values)

# m_list = MathList([1, 2, 3, 4, 5])
# print(m_list)

# m_list += [2]
# print(m_list)

# m_list -= [2]
# print(m_list)

# Bai 3
# class Square():
#     def __init__(self, side):
#         self.side = side

#     def cal_area(self):
#         return self.side * self.side

# class Cube(Square):
#     def __init__(self, side):
#         Square.__init__(self, side)

#     def cal_area(self):
#         return 6 * Square.cal_area(self)

#     def cal_volume(self):
#         return self.side * self.side * self.side

# square = Square(2)
# print('Square area:', square.cal_area())

# cube = Cube(2)
# print('Cube area:', cube.cal_area())
# print('Cube volume:', cube.cal_volume())

# Bai 4
from datetime import datetime
class User():
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def check_password(self, password):
        if self.password == password:
            return True
        else:
            return False

    def welcome(self):
        print("Welcome,", self.name)

class SubscribedUser(User):
    def __init__(self, name, password, subscription_date):
        User.__init__(self, name, password)
        self.subscription_date = subscription_date
        
    def is_expired(self):
        if datetime.now() < self.subscription_date:
            return True
        else:
            return False

# user = User('mindx', '12345')
# user.welcome()
# print(user.check_password('1234'))

s_user = SubscribedUser('s_mindx', '1234', datetime(2021, 1, 1))
s_user.welcome()
print(s_user.check_password('1234'))
print(s_user.is_expired())
