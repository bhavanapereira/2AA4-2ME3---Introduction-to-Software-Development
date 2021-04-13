## @file Shape.py
#  @author Bhavna Pereira
#  @brief Shape ADT Class implementations
#  @date 16/02/2021

from abc import ABC, abstractmethod

## @brief The class outlines shape properties
#  @details The class contains four methods to detail the x and y coordinates
#           of the center of mass, along with the mass and the m_inert


class Shape(ABC):
    ## @brief Abstract method to pass the x coordinate of the center of mass
    #  @details defines and passes on this property for use by other modules

    @abstractmethod
    def cm_x(self):
        pass

    ## @brief Abstract method to pass the y coordinate of the center of mass
    #  @details defines and passes on this property for use by other modules
    @abstractmethod
    def cm_y(self):
        pass

    ## @brief Abstract method to pass the mass of the shape
    #  @details defines and passes on this property for use by other modules
    @abstractmethod
    def mass(self):
        pass

    ## @brief Abstract method to pass the maoment of inertia
    #  @details defines and passes on this property for use by other modules
    @abstractmethod
    def m_inert(self):
        pass
