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
		return "({}, {})".format(self.__x, self.__y) 

	def __eq__(self, complexT):
		if complexT.real() == self.__x and complexT.imag() == self.__y:
			return True
		else:
			return False

	def real(self):
		return self.__x

	def imag(self):
		return self.__y

	def get_r(self):
		return abs(sqrt(x**2 + y**2))

	def get_phi(self):
		comp = complex(self.__x,self.__y)
		return cmath.phase(comp)

	def equal(self, complexT):
		return self.__eq__(complexT)

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
		if complexT.real() == 0 or complexT.imag() == 0:
			raise ZeroDivisionError("Cannot Divide By Zero")
		else:
			return ComplexT((self.__x / complexT.real()), (self.__y / complexT.imag()))

	def sqrt(self):
		cmath.sqrt(self.__x + self.__y*1j)


compEdgeCase1 = ComplexT(0,0)
expectedReal1 = 0
print (compEdgeCase1.real() == expectedReal1)



