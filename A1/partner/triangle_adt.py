## @file triangle_adt.py
#  @brief Contains the TriangleT class which represents triangles
#  @author Nathan Uy
#  @date 01/21/2021

from math import sqrt
from enum import Enum, auto

## @brief An abstract data type that represents triangles.
class TriangleT:

	## @brief TriangleT constructor
	# @details Initializes a TriangleT object with the three sides.
	# @param l1 An integer that represents the length of one side of the triangle.
	# @param l2 An integer that represents the length of one side of the triangle.
	# @param l3 An integer that represents the length of one side of the triangle.
	# @throws AssertionError Throws AssertionError if one of the sides is equal to zero.
	def __init__(self, l1, l2, l3):
		##assert(l1 > 0 and l2 > 0 and l3 > 0), "All three sides must be greater than 0"
		self.l1 = l1
		self.l2 = l2
		self.l3 = l3

	## @brief Gets the length of the three sides of the triangle.
	# @return A tuple with the lengths of each side of the triangle.
	def get_sides(self):
		return (self.l1, self.l2, self.l3)

	## @brief Determines whether the current object and the argument are equal.
	# @param Triangle A TriangleT object.
	# @return True if the current object and the argument are equal; False otherwise.
	def equal(self, Triangle):
		currObj = list(self.get_sides())
		arg = list(Triangle.get_sides())
		currObj.sort()
		arg.sort()
		compare = currObj == arg
		return compare

	## @brief Calculates the perimeter of the current object.
	## @details It is assumed that the given triangle is valid
	# @return An integer that represents the perimeter of the current object.
	def perim(self):
		return self.l1+self.l2+self.l3

	## @brief Calculates the area of the current object.
	## @details It is assumed that the given triangle is valid
	# @return A float that represents the area of the current object.
	# @throws AssertionError Throws AssertionError if half the sum of the sides is less than or equal the greatest side.
	def area(self):
		s = (self.l1+self.l2+self.l3)/2
		assert(s > max(self.get_sides()))
		area = sqrt(s*(s-self.l1)*(s-self.l2)*(s-self.l3))
		return area

	## @brief Determines whether the three sides of the current object form a valid triangle or not.
	# @return True if the three sides of the current object form a valid triangle; False otherwise.
	def is_valid(self):
		if (self.l1+self.l2 > self.l3 and self.l1+self.l3 > self.l2 and self.l3+self.l2 > self.l1):
			return True
		else:
			return False

	## @brief Determines the triangle type of the current object.
	## @details It is assumed that the given triangle is valid
	# @return A TriType object that corresponds to the triangle type of the current object.
	def tri_type(self):
		sides = list(self.get_sides())
		AandB = list(self.get_sides())
		hypotenuse = max(sides)
		AandB.remove(hypotenuse)

		if AandB[0]**2 + AandB[1]**2 == hypotenuse**2:
			triangleType = TriType(1)
		elif sides[0] == sides[1] and sides[0] == sides[2]:
			triangleType = TriType(2)
		elif sides[0] == sides[1] or sides[0] == sides[2] or sides[2] == sides[1]:
			triangleType = TriType(3)
		else:
			triangleType = TriType(4)

		return triangleType


## @brief TriType constructor.
# @details Creates an enumeration that corresponds to the triangle types.
# @param Enum An integer that represents the type of the triangle.
class TriType(Enum):
	right = auto()
	equilat = auto()
	isosceles = auto()
	scalene = auto()