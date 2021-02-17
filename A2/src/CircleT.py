## @file CircleT.py
#  @author
#  @brief
#  @date

from Shape import *

class CircleT(Shape):


    def __init__(self, x, y, r, m):
        if r < 0 or m < 0:
            raise ValueError
        else:
            self.__x = x
            self.__y = y
            self.__r = r
            self.__m = m

    def cm_x(self):
        return self.__x

    def cm_y(self):
        return self.__y

    def mass(self):
        return self.__m

    def m_inert(self):
        return (self.__m * (self.__r**2))/2