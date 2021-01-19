## @file complex_adt.py
#  @author 
#  @brief 
#  @date 

import cmath

class ComplexT:
	def __init__(self, x, y):
		self.__x = x
		self.__y = y

	def __str__(self):
		return "coordinates: ({}, {})".format(self.__x, self.__y)

	def real(self):
		return self.__x

	def imag(self):
		return self.__y

	def r(self):
		return abs(sqrt(x**2 + y**2))

	def get_phi(self):
		comp = complex(self.__x,self.__y)
		return cmath.phase(comp)

	def equal(self, complexT):
		if complexT.real() == self.__x and complexT.imag() == self.__y:
			return True
		else:
			return False

	def conj(self):
		return ComplexT(self.__x, -self.__y)

	def add(self, complexT):
		return ComplexT(complexT.real() + self.__x, complexT.imag() + self.__y)

	def sub(self, complexT):
		return ComplexT(self.__x - complexT.real(), self.__y - complexT.imag())

	def mult(self, complexT):
		return ComplexT((self.__x * complexT.real()), (self.__y * complexT.imag()))

	def recip(self):
		comp = (1/(self.__x + self.__y*1j))
		return ComplexT(comp.real, comp.imag)


	def div(self, complexT):
		return complex((self.__x / complexT.real()), (self.__y / complexT.imag()))

	def sqrt(self):
		cmath.sqrt(self.__x + self.__y*1j)

test = ComplexT(2,3)
test2 = ComplexT(0,0)
testn = ComplexT(3,9)
print (test.real())
print (test2.conj())
print (testn.recip())



