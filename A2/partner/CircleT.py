## @file CircleT.py
#  @author Nathan Uy
#  @brief Contains the CircleT module which creates circles.
#  @date 02/16/2021

from Shape import Shape

## @brief An abstract data type that represents circles.


class CircleT(Shape):

    ## @brief A CircleT constructor.
    # @details Initializes a CricleT object with its x, y position, radius, and mass.
    # @param x A float that represents the x-coordinate of the circle.
    # @param y A float that represents the y-coordinate of the circle.
    # @param r A float that represents the radius of the circle.
    # @param m A float that represents the mass of the circle.
    # @throws ValueError Throws ValueError if the radius and mass
    # of the circle are less than or equal to zero.
    def __init__(self, x, y, r, m):
        if not(r > 0 and m > 0):
            raise ValueError
        self.x = x
        self.y = y
        self.r = r
        self.m = m

    ## @brief Gets the x-coordinate of the circle.
    # @return A float that represents the x-coordinate of the circle.
    def cm_x(self):
        return self.x

    ## @brief Gets the y-coordinate of the circle.
    # @return A float that represents the y-coordinate of the circle.
    def cm_y(self):
        return self.y

    ## @brief Gets the mass of the circle.
    # @return A float that represents the mass of the circle.
    def mass(self):
        return self.m

    ## @brief Gets the moment of inertia of the circle.
    # @return A float that represents the moment of inertia of the circle.
    def m_inert(self):
        return (self.m * self.r**2) / 2
