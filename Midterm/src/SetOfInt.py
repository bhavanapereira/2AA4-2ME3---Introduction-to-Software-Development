## @file SetOfInt.py
#  @author Your Name
#  @brief Set of integers
#  @date 03/04/2021

class SetOfInt:

	def __init__(self, xs):
		self.__xs = set(xs)


	def is_member(self, x):
		if x in self.__xs:
			return True
		else:
			return False

	def to_seq(self):
		seq_equivalent = []
		for x in self.__xs:
			seq_equivalent.append(x) 
		return seq_equivalent

#	def union(self, t):


#	def diff(self, t):

	def size(self):
		return len(self.__xs)


	def empty(self):
		if len(self.__xs) == 0:
			return True 
		else:
			return False

	#def equals(self, t):




@staticmethod
def set_to_seq(s):
	result = []
	for x in s:
		result.append(x)
	return result

#@staticmethod
#def complement(A):


