## @file TriangleT.py
#  @author Nathan Uy
#  @brief Contains the TriangleT module which creates triangles.
#  @date 02/16/2021

from Shape import Shape

## @brief An abstract data type that represents equilateral triangles.


class TriangleT(Shape):

    ## @brief A TriangleT constructor.
    # @details Initializes a TriangleT object with its x, y position, side, and mass.
    # @param x A float that represents the x-coordinate of the triangle.
    # @param y A float that represents the y-coordinate of the triangle.
    # @param r A float that represents the side length of the triangle.
    # @param m A float that represents the mass of the triangle.
    # @throws ValueError Throws ValueError if the side length and mass
    # of the triangle are less than or equal to zero.
    def __init__(self, x, y, s, m):
        if not(s > 0 and m > 0):
            raise ValueError
        self.x = x
        self.y = y
        self.s = s
        self.m = m

    ## @brief Gets the x-coordinate of the triangle.
    # @return A float that represents the x-coordinate of the triangle.
    def cm_x(self):
        return self.x

    ## @brief Gets the y-coordinate of the triangle.
    # @return A float that represents the y-coordinate of the triangle.
    def cm_y(self):
        return self.y

    ## @brief Gets the mass of the triangle.
    # @return A float that represents the mass of the triangle.
    def mass(self):
        return self.m

    ## @brief Gets the moment of inertia of the triangle.
    # @return A float that represents the moment of inertia of the triangle.
    def m_inert(self):
        return (self.m * self.s**2) / 12
