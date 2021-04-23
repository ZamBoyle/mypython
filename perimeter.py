import math


def RectanglePerimeter(_length, _width):
    return 2 * (_length + _width)


def CirclePerimeter(_radius):
    return 2 * math.pi * _radius


def SquarePerimeter(_side):
    return 4 * _side


def TrianglePerimeter(_length1, _length2, _length3):
    return _length1 + _length2 + _length3
