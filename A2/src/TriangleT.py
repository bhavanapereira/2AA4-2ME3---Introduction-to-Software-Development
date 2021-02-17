## @file TriangleT.py
#  @author
#  @brief
#  @date

from Shape import *

class TriangleT(Shape):

    def __init__(self, x, y, s, m):
        if s < 0 or m < 0:
            raise ValueError
        else:
            self.__x = x
            self.__y = y
            self.__s = s
            self.__m = m

    def cm_x(self):
        return self.__x

    def cm_y(self):
        return self.__y

    def mass(self):
        return self.__m

    def m_inert(self):
        return (self.__m * (self.__s**2))/12

