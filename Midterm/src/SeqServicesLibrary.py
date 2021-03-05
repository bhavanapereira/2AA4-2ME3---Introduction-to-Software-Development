## @file SeqServicesLibrary.py
#  @author Bhavna Pereira
#  @brief Library module that provides functions for working with sequences
#  @details This library assumes that all functions will be provided with arguments of the expected types
#  @date 03/04/2021



def max_val(s):
	if len(s) == 0:
		raise ValueError 
	else:
		m = 0
		for i in s:
			if abs(i) > m: 
				m = abs(i)
		return m 



def count(t, s): 
	if len(s) == 0:
		raise ValueError
	else:
		result = 0
		for r in s:
			if r == t:
				result += 1
	return result


def spices(s):
	if len(s) == 0:
		raise ValueError 
	else:
		result = []
		for x in s:
			if x <= 0: 
				result.append("Nutmeg")
			else:
				result.append("Ginger") 
	return result 


def new_max_val(s, f):
	if len(s) == 0: 
		raise ValueError
	else:
		result = [] 
		for x in s:
			if f(x) == True: 
				result.append(x)
		return max_val(result) 
