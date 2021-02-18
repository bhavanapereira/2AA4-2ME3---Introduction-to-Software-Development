## @file BodyT.py
#  @author Nathan Uy
#  @brief Contains the BodyT module which creates bodies.
#  @date 02/16/2021

from functools import reduce
from Shape import Shape

## @brief An abstract data type that represents a body.


class BodyT(Shape):

    ## @brief A BodyT constructor.
    # @details Initializes a BodyT object with its center of mass wrt x and y,
    # its mass, and its moment.
    # @param x A sequence of floats that represents the x-coordinate of each shape.
    # @param y A sequence of floats that represents the y-coordinate of each shape.
    # @param m A sequence of floats that represents the mass of each shape.
    # @throws ValueError Throws ValueError if the length of x, y and m are not equal
    # or if any of the mass is less than or equal to zero.
    def __init__(self, x, y, m):
        if not(len(x) == len(y) == len(m)) or \
           not(reduce(lambda x, y: x and (y > 0), m, True)):
            raise ValueError
        self.cmx = self.__cm__(x, m)
        self.cmy = self.__cm__(y, m)
        self.m = self.__sum__(m)
        self.moment = self.__mmom__(x, y, m) - self.__sum__(m) * \
            (self.__cm__(x, m)**2 + self.__cm__(y, m)**2)

    ## @brief Gets the x component of the body's center of mass.
    # @return A float that represents the x component of the body's center of mass.
    def cm_x(self):
        return self.cmx

    ## @brief Gets the y component of the body's center of mass.
    # @return A float that represents the y component of the body's center of mass.
    def cm_y(self):
        return self.cmy

    ## @brief Gets the mass of the body.
    # @return A float that represents the mass of the body.
    def mass(self):
        return self.m

    ## @brief Gets the moment of inertia of the body.
    # @return A float that represents the moment of inertia of the body.
    def m_inert(self):
        return self.moment

    ## @brief Calculates the overall mass of the body.
    # @param m A sequence of floats that represents the
    # mass of each shape in the body.
    # @return A float that represents the total mass of the shapes in the body.
    def __sum__(self, m):
        return reduce(lambda x, y: x + y, m, 0)

    ## @brief Calculates the center of mass of the body.
    # @param z A sequence of floats that represents the x position
    # of each shape in the body.
    # @param m A sequence of floats that represents the
    # mass of each shape in the body.
    # @return A float that represents the center of mass of the body.
    def __cm__(self, z, m):
        accum = 0
        for i in range(len(m)):
            accum += z[i] * m[i]
        return accum / self.__sum__(m)

    ## @brief Calculates the mass moment of inertia of the body.
    # @param x A sequence of floats that represents the x position of each
    # shape in the body.
    # @param y A sequence of floats that represents the y position of each
    # shape in the body.
    # @param m A sequence of floats that represents the mass of each
    # shape in the body.
    # @return A float that represents the mass moment of inertia of the body.
    def __mmom__(self, x, y, m):
        accum = 0
        for i in range(len(m)):
            accum += m[i] * (x[i]**2 + y[i]**2)
        return accum / self.__sum__(m)
