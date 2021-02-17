## @file Shape.py
#  @author
#  @brief
#  @date

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def cm_x(self):
        pass

    @abstractmethod
    def cm_y(self):
        pass
   
    @abstractmethod
    def mass(self):
        pass

    @abstractmethod
    def m_inert(self):
        pass