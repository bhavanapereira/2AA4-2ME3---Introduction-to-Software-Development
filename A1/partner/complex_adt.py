## @file complex_adt.py
#  @brief Contains the ComplexT class which represents complex numbers
#  @author Nathan Uy
#  @date 01/21/2021

from math import sqrt, atan, atan2, pi

## @brief An abstract data type that represents complex numbers.
class ComplexT:

	## @brief A ComplexT constructor.
	# @details Initializes a ComplexT object with the real and imaginary part.
	# @param x A float that represents the real part of the complex number.
	# @param y A float that represents the imaginary part of the complex number.
	# @throws AssrtionError Throws AssertionError if x and y are equal to zero.
	def __init__(self, x, y):
		assert (not(x == 0 and y == 0)), "x and y must be non-zero."
		self.x = x 
		self.y = y

	## @brief Gets the real part of the complex number.
	# @return A float that represents the real part of the complex number.
	def real(self):
		return self.x

	## @brief Gets the imaginary part of the complex number.
	# @return A float that represents the imaginary part of the complex number.
	def imag(self):
		return self.y

	## @brief Calculates the modulus of the complex number.
	# @return A float that represents the modulus of the complex number.
	def get_r(self):
		return sqrt(self.x**2 + self.y**2)

	## @brief Calculates the phase of the complex number in radians.
	# @details Assuming phi is between 0 and 2pi.
	# @return A float that represents the phase of the complex number.
	def get_phi(self):
		if self.x < 0 and self.y < 0:
			return pi + atan2(self.y, self.x)
		elif self.x > 0 and self.y < 0:
			return pi + atan2(self.y, self.x)
		else:
			return atan2(self.y, self.x)

	## @brief Determines whether the current object and the argument are equal.
	# @param Complex A ComplexT object.
	# @return True if the current object is equal to Complex; False otherwise.
	def equal(self, Complex):
		return (self.x == Complex.x and self.y == Complex.y)

	## @brief Calculates the complex conjugate of the current object.
	# @return A ComplexT object which represents the complex conjugate of the current object.
	def conj(self): 
		y = -1 * self.y
		return ComplexT(self.x, y)

	## @brief Calculates the sum of the current object and the argument.
	# @param Complex A ComplexT object. 
	# @return A ComplexT object which represents the sum of the argument and the current object.
	def add(self, Complex):
		x = self.x + Complex.x
		y = self.y + Complex.y
		return ComplexT(x,y)

	## @brief Subtracts the argument from the current object.
	# @param Complex A ComplexT object. 
	# @return A ComplexT object that subtracts the argument from the current argument.
	def sub(self, Complex):
		x = self.x - Complex.x
		y = self.y - Complex.y
		return ComplexT(x,y)

	## @brief Calculates the product of the current object and the argument.
	# @param Complex A ComplexT object. 
	# @return A ComplexT object that represents the product of the current object and the argument.
	def mult(self, Complex):
		y = self.x*Complex.y + self.y*Complex.x
		x = self.x*Complex.x - self.y*Complex.y
		return ComplexT(x,y)

	## @brief Calculates the reciprocal of the current object.
	# @return A ComplexT object that represents the reciprocal of the current object.
	def recip(self):
		divisor = self.x**2 + self.y**2
		x = self.x / divisor
		y = -1 * self.y / divisor
		return ComplexT(x,y)

	## @brief Divides the current object by the argument.
	# @param Complex A ComplexT object. 
	# @return A ComplexT object that divides the current argument by the argument.
	def div(self, Complex):
		x = (self.x*Complex.x + self.y*Complex.y) / (Complex.x**2 + Complex.y**2)
		y = (self.y*Complex.x - self.x*Complex.y) / (Complex.x**2 + Complex.y**2)
		return ComplexT(x,y)

	## @brief Calculates the squareroot of the current object.
	# @return A ComplexT object that represents the squareroot of the current object 
	# @throws ZeroDivisionError Throws ZeroDivisionError if y is equal to zero.
	# @throws ValueError Throws ValueError if the modulo of the object + x < 0 or the modulo of the object - x < 0).
	def sqrt(self): 
		if self.y == 0:
			raise ZeroDivisionError("The imaginary part of the complex number must be non-zero for sqrt to exist.")
		elif (self.get_r() + self.x < 0 or self.get_r() - self.x < 0):
			raise ValueError("This complex number does not have a squareroot")
		else:
			x = sqrt((self.get_r() + self.x) / 2)
			y = (self.y / abs(self.y)) * sqrt((self.get_r() - self.x) / 2)
		return ComplexT(x,y)