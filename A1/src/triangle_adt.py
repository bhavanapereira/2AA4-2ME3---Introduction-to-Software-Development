## @file triangle_adt.py
#  @author Bhavna Pereira
#  @brief Triangle_adt method implementation; step 1 of Assignment 1
#  @date 21/01/2021

from math import sqrt
from enum import Enum, auto

## @brief This Class creates an object of type TriType 
#  @details The class determine the classification in the form 
#  of a triangle, based on their values
class TriType(Enum):
	equilat = auto()
	isosceles = auto()
	scalene = auto()
	right = auto()

## @brief This Class creates an object of type TriangleT
#  @details The class takes in three integers and uses their values as
#  the side lengths of triangles to calculate various functions
class TriangleT:

## @brief This is a constructor for TriangleT
#  @details This constructor creates a triangle based on the inputted values
#  @param x An integer representing the first side length
#  @param y An integer representing the second side length
#  @param z An integer representing the third side length
	def __init__(self, x,y,z):
		self.__x = x
		self.__y = y
		self.__z = z

	def __eq__(self, triangleT):
		inputted = [triangleT.__x, triangleT.__y, triangleT.__z]
		inputted.sort()
		current = [self.__x, self.__y, self.__z]
		current.sort()
		if inputted == current:
			return True
		else:
			return False 

## @brief this method differentiates the sides of the triangle
#  @details the method checks to see if the triangle is valid, and if it is it returns
#  the side lengths
#  @return the returned values are in the form of integers 
	def get_sides(self):
		if self.is_valid() == False:
			raise ValueError ("This is not a valid triangle")
		else:
			return (self.__x, self.__y, self.__z)

## @brief this method checks to see if the current side lengths are equal
#  @details the method check equality of the side lenghts of the inputted TriangleT object
#  by passing it to "__eq__"
#  @return the returned value is in the form of boolean
	def equal(self, triangleT):
		return self.__eq__(triangleT)

## @brief this method calculates the perimeter of the TriangleT object
#  @details The method verifies if the triangle is valid, and if it is,
#  it calculates the perimeter by adding together the three side lengths
#  @return the returned value is in the form of an integer
	def perim(self):
		if self.is_valid() == False:
			raise ValueError ("This is not a valid triangle")
		else:	
			return (self.__x + self.__y + self.__z)

## @brief this method calculates the area of the TriangleT object
#  @details The method verifies if the triangle is valid, and if it is,
#  it calculates the perimeter using heron's formula
#  @return the returned value is in the form of a float
	def area(self):
		if self.is_valid() == False:
			raise ValueError ("This is not a valid triangle")
		else:	
			s = self.perim() / 2
			return (sqrt(s * (s-self.__x) * (s-self.__y) * (s-self.__z)))

## @brief this method verifies the validity of the object of type TriangleT
#  @details The method checks to see if the addition of any two of the three side
#  lengths have a sum greater than the value of the third side length. If this is 
#  not true, the triangle is invalid
#  @return the returned value is in the form of a  boolean
	def is_valid(self):
		if self.__x + self.__y > self.__z and self.__y + self.__z > self.__x:
			if self.__x + self.__z > self.__y:
				return True
			else:
				return False
		else:
			return False

## @brief this method calculates the type of triangle of the TriangleT object
#  @details The method verifies if the triangle is valid, and if it is,
#  it calculates whether the triangle is scalene, right, isosceles, or equilateral
#  based on a variety of interdependent properties of each side length value
#  @return the returned value is in the form of TriType.x, where x represents
#  either scalene, right, equilateral, or isosceles
	def tri_type(self):
		if self.is_valid() == False:
			raise ValueError ("This is not a valid triangle")
		elif self.__x == self.__y and self.__y == self.__z:
			return TriType.equilat
		elif self.__x == self.__y and self.__y != self.__z:
			return TriType.isosceles
		elif self.__x == self.__z and self.__z != self.__y:
			return TriType.isosceles
		elif self.__y == self.__z and self.__z != self.__x:
			return TriType.isosceles
		elif self.__y != self.__x and self.__x != self.__z and self.__y != self.__z:
			if ((self.__x)**2 + (self.__y**2)) == (self.__z)**2:
				return TriType.right
			if ((self.__x)**2 + (self.__z)**2) == (self.__y)**2:
				return  TriType.right
			if ((self.__y)**2 + (self.__z)**2) == (self.__x)**2:
				return TriType.right
			else:
				return TriType.scalene


