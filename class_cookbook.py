# class Pair:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return 'Pair(%r, %r)' % (self.x, self.y)
#
#     def __str__(self):
#         return '(%s, %s)'% (self.x, self.y)
#
#
# p = Pair(3, 4)
# print('p is {0!r}'.format(p))
# print(p)

#
# _formats = {
#     'ymd' : '{d.year}-{d.month}-{d.day}',
#     'mdy' : '{d.month}/{d.day}/{d.year}',
#     'dmy' : '{d.day}/{d.month}/{d.year}'
# }
#
# class Date:
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day
#
#     def __format__(self, code):
#         if code == '':
#             code = 'ymd'
#         fmt = _formats[code]
#         return fmt.format(d=self)
#
# d = Date(2018, 4, 8)
# print(format(d, 'dmy'))
# print('This date is {:ymd}'.format(d))

#
# class TestContext:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.result = None
#
#     def __enter__(self):
#         self.result =  self.x + self.y
#         return self.result
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.result = None
#
#
# tc = TestContext(11, 22)
#
# with tc as t:
#     print(t)
#


class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius **2

    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius

c = Circle(3)
print(c.radius)
print(c.area)
print(c.area)
print(c.perimeter)
print(c.perimeter)