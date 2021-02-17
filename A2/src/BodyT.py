## @file BodyT.py
#  @author Bhavna Pereira
#  @brief Class implementation of BodyT with the use of Shape.py
#  @date 16/02/2021

from Shape import *


## @brief The following class outlines properties of all other shapes in motion
#  @details The properties include x and y coordinate of Center of Mass,
#  the mass, and the moment of inertia
class BodyT(Shape):

## @brief This method is a constructor for BodyT
#  @details The method ensures that all masses in sequence
#  are greater than zero, and if the length of the sequences
#  of all parameters are equal. If they are, the x and y
#  coordinates and the mass are stated using local functions
#  @param the method takes in three natural numbers x,y,m 
#  to represent the x coordinate, the y coordinate,
#  and the mass, respectively
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

## @brief this method returns the value of the x coordinate of the shape's
#  center of mass
#  @returns Returns the state variable of the correct type
    def cm_x(self):
        return self.__cmx

## @brief this method returns the value of the y coordinate of the shape's
#  center of mass
#  @returns Returns the state variable of the correct type
    def cm_y(self):
        return self.__cmy

## @brief this method returns the value of the mass of the shape
#  @returns Returns the state variable of the correct type
    def mass(self):
        return self.__m

## @brief this method calculates the moment of inertia of the triangle
#  @details this method returns a value based on the calculated moment of
#  inertia through local function mmom(x,y,z)
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



