## @file TriangleT.py
#  @author Bhavna Pereira
#  @brief Class implementation of TriangleT with the use of Shape.py
#  @date 16/02/2021

from Shape import *

## @brief The following class outlines properties of a triangle in motion
#  @details The properties include x and y coordinate of Center of Mass,
#           the mass, and the moment of inertia


class TriangleT(Shape):
    ## @brief This method is a constructor for TriangleT
    #  @details The method ensures that the radius and mass
    #           are greater than zero, and if they are, the x and y
    #           coordinates, along with the radius and mass are stated
    #  @param x represents the x coordinate of the center of mass (Real Number)
    #  @param y represents the y coordinate of the center of mass (Real Number)
    #  @param s represents the sidelength of the triangle (Real Number)
    #  @param m represents the mass of the objet (Real Number)
    def __init__(self, x, y, s, m):
        if s < 0 or m < 0:
            raise ValueError('Invalid Input')
        else:
            self.__x = x
            self.__y = y
            self.__s = s
            self.__m = m

    ## @brief this method returns the value of the x coordinate of the triangle's
    #         center of mass
    #  @returns Returns the state variable of the correct type
    def cm_x(self):
        return self.__x

    ## @brief this method returns the value of the y coordinate of the triangle's
    #         center of mass
    #  @returns Returns the state variable of the correct type
    def cm_y(self):
        return self.__y

    ## @brief this method returns the value of the mass of the triangle
    #  @returns Returns the state variable of the correct type
    def mass(self):
        return self.__m

    ## @brief this method calculates the moment of inertia of the triangle
    #  @details using the mass, multiplied by the square of the sidelength
    #           and dividind the product by 12, this method returns the value of
    #           the moment of inertia
    def m_inert(self):
        return (self.__m * (self.__s**2)) / 12
