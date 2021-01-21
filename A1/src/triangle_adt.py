## @file triangle_adt.py
#  @author 
#  @brief 
#  @date 
from math import sqrt
from enum import Enum, auto

class TriType(Enum):
	equilat = auto()
	isosceles = auto()
	scalene = auto()
	right = auto()


class TriangleT:
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

	def get_sides(self):
		if self.is_valid() == False:
			raise ValueError ("This is not a valid triangle")
		else:
			return (self.__x, self.__y, self.__z)

	def equal(self, triangleT):
		return self.__eq__(triangleT)


	def perim(self):
		if self.is_valid() == False:
			raise ValueError ("This is not a valid triangle")
		else:	
			return (self.__x + self.__y + self.__z)

	def area(self):
		if self.is_valid() == False:
			raise ValueError ("This is not a valid triangle")
		else:	
			s = self.perim() / 2
			return (sqrt(s * (s-self.__x) * (s-self.__y) * (s-self.__z)))

	def is_valid(self):
		if self.__x + self.__y > self.__z and self.__y + self.__z > self.__x:
			if self.__x + self.__z > self.__y:
				return True
			else:
				return False
		else:
			return False

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


