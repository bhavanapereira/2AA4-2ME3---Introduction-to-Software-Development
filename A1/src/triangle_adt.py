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

	def getsides(self):
		return (self.__x, self.__y, self.__z)

	def equal(self, triangleT):
		inputted = [triangleT.__x, triangleT.__y, triangleT.__z]
		current = [self.__x, self.__y, self.__z]
		if inputted.sort() == current.sort():
			return True
		else:
			return False 


	def perim(self):
		return (self.__x + self.__y + self.__z)

	def area(self):
		s = self.perim() / 2
		return (math.sqrt(s * (s-self.__x) * (s-self.__y) * (s-self.__z)))

	def valid(self):
		if self.__x + self.__y > self.__z and self.__y + self.__z > self.__x:
			if self.__x + self.__z > self.__y:
				return True
			else:
				return False
		else:
			return False

	def tri_type(self):

		if self.__x == self.__y and self.__y == self.__z:
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

test1 = TriangleT(1,1,2)
test2 = TriangleT(1,2,3)
test3 = TriangleT(3,4,5)
test4 = TriangleT(3,3,3)
print (test1.tri_type())
print (test2.tri_type())
print (test3.tri_type())
print (test4.tri_type())
