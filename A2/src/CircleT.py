## @file CircleT.py
#  @author Bhavna Pereira
#  @brief Class implementation of CircleT with the use of Shape.py
#  @date 16/02/2021

from Shape import *

## @brief The following class outlines properties of a circle in motion
#  @details The properties include x and y coordinate of Center of Mass,
#  the mass, and the moment of inertia
class CircleT(Shape):


## @brief This method is a constructor for CircleT
#  @details The method ensures that the radius and mass
#  are greater than zero, and if they are, the x and y
#  coordinates, along with the radius and mass are stated
#  @param the method takes in four natural numbers x,y,r,m 
#  to represent the x coordinate, the y coordinate, the radius
#  and the mass, respectively
    def __init__(self, x, y, r, m):
        if r < 0 or m < 0:
            raise ValueError
        else:
            self.__x = x
            self.__y = y
            self.__r = r
            self.__m = m

## @brief this method returns the value of the x coordinate of the circle's
#  center of mass
#  @returns Returns the state variable of the correct type
    def cm_x(self):
        return self.__x

## @brief this method returns the value of the y coordinate of the circle's
#  center of mass
#  @returns Returns the state variable of the correct type
    def cm_y(self):
        return self.__y

## @brief this method returns the value of the mass of the circle
#  @returns Returns the state variable of the correct type
    def mass(self):
        return self.__m

## @brief this method calculates the moment of inertia of the circle
#  @details using the mass, multiplied by the square of the radius
#  and dividind the product by 2, this method returns the value of the
#  moment of inertia
    def m_inert(self):
        return (self.__m * (self.__r**2))/2