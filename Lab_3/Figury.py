import math

class Circle:
    r = None
    def __init__(self,r):
        self.r = r
    def areac(r):
        try:
            result = pow(r,2)*math.pi;
            return result
        except:
            pass

class Rectangle:
    a = None
    b = None
    def __index__(self ,a, b):
        self.a = a
        self.b = b
    def arear(a , b):
        try:
            result = a * b
            return result
        except:
            pass


class Triangle:
    a = None
    h = None
    def __init__(self , a , h):
        self.a = a
        self.h = h
    def areat(a , h):
        try:
            result = 0.5 * a * h
            return result
        except:
            pass
