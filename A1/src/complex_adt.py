## @file complex_adt.py
#  @author Bhavana Pereira
#  @brief Complex_adt method implementation; step 1 of Assignment 1
#  @date 21/01/2021

import cmath

## @brief This Class creates an object of ComplexT
#  @details The class takes in two integers and formats them as complex numbers. 
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
## @brief this method returns the real number of a complex number
#  @details in a complex number of format a + bi, this method returns the value a
#  @return the returned value in the form of an integer
	def real(self):
		return self.__x

## @brief this method returns the imaginary number of a complex number
#  @details in a complex number of format a + bi, this method returns the value b
#  @return the returned value in the form of an integer
	def imag(self):
		return self.__y

## @brief this method returns the radius of a complex number
#  @details in a complex number of format a + bi, this method 
#  returns the square root of (a^2 + b^2)
#  @return the returned value in the form of a float
	def get_r(self):
		return abs(sqrt(x**2 + y**2))

## @brief this method returns the phase of a complex number
#  @details in a complex number of format a + bi, this method uses the cmath
#  library to compute the phase of the complex number
#  @return the returned value in the form of a float
	def get_phi(self):
		comp = complex(self.__x,self.__y)
		return cmath.phase(comp)

## @brief this method computes if the current complex number
#   equals another inputted complex number
#  @details in a complex number of format a + bi, this method 
#  compares the a and b values of each to check if they're equal
#  @param the method takes in another object of type ComplexT
#  @return the returned value in the form of a boolean
	def equal(self, complexT):
		return self.__eq__(complexT)

## @brief this method computes the conjugate of a complex number
#  @details in a complex number of format a + bi, this method 
#  computes the negative of the imaginary value, i.e., the negative
#  of value b
#  @return the returned value in the form of an integer
	def conj(self):
		return ComplexT(self.__x, -self.__y)

## @brief this method adds to the current complex number
#  another inputted complex number
#  @details in two complex numbers of format a + bi, c + di, this method 
#  adds a+c and b+d
#  @param the method takes in another object of type ComplexT
#  @return the returned value in the form of an integer
	def add(self, complexT):
		return ComplexT(complexT.real() + self.__x, complexT.imag() + self.__y)

## @brief this method subtracts from the current complex number
#  another inputted complex number
#  @details in two complex numbers of format a + bi, c + di, this method 
#  subtracts a-c and b-d
#  @param the method takes in another object of type ComplexT
#  @return the returned value in the form of an integer
	def sub(self, complexT):
		return ComplexT(self.__x - complexT.real(), self.__y - complexT.imag())

## @brief this method multiplies the values of the current complex number
#  by the values of another inputted complex number
#  @details in two complex numbers of format a + bi, c + di, this method 
#  multiplies a*c and b*d
#  @param the method takes in another object of type ComplexT
#  @return the returned value in the form of an integer
	def mult(self, complexT):
		return ComplexT((self.__x * complexT.real()), (self.__y * complexT.imag()))

## @brief this method calculates the reciprocal of a complex number
#  @details in the form of a + bi, this method calculates the inverse
#  of a + bi
#  @return the returned value in the form of an float
	def recip(self):
		comp = (1/(self.__x + self.__y*1j))
		return ComplexT(comp.real, comp.imag)


## @brief this method divides the values of the current complex number
#  by the values of another inputted complex number
#  @details in two complex numbers of format a + bi, c + di, this method 
#  multiplies a/c and b/d. It raises an exception if the inputted values are 0,
#  as a number cannot be divided by 0
#  @param the method takes in another object of type ComplexT
#  @return the returned value in the form of an float
	def div(self, complexT):
		if complexT.real() == 0 or complexT.imag() == 0:
			raise ZeroDivisionError("Cannot Divide By Zero")
		else:
			return ComplexT((self.__x / complexT.real()), (self.__y / complexT.imag()))

	def sqrt(self):
		ans = cmath.sqrt(self.__x + self.__y*1j)
		return ComplexT(ans.real, ans.imag)





