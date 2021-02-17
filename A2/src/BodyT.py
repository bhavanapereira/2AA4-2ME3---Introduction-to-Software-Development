## @file BodyT.py
#  @author
#  @brief
#  @date

from Shape import *

class BodyT(Shape):

    def __init__(self, x, y, m):
        for i in m:
            if i < 0:
                raise ValueError
        if len(x) == len(y) and len(y) == len(m):
            self.__cmx = cm(x, m)
            self.__cmy = cm(y, m)
            self.__m = sum(m)
            self.__moment = mmom(x, y, m) - sum(m)*(cm(x, m)**2 + cm(y, m)**2)
        else:
            raise ValueError

    def cm_x(self):
        return self.__cmx

    def cm_y(self):
        return self.__cmy

    def mass(self):
        return self.__m

    def m_inert(self):
        return self.__moment

def cm(z,m):
    total = 0
    for i in range(0, len(m)):
        val = z[i]*m[i]
        total += val
    return total/sum(m)


def mmom(x,y,m):
    total = 0
    for i in range(0, len(m)):
        val = m[i]*(x[i]**2 + y[i]**2)
        total += val
    return total 



