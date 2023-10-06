from functools import reduce

def factorial(num):
	if num == 0:
		return 1
	
	numbers = list(range(1, num + 1)) # create list from 1 n

	answer = reduce(lambda a, b: a * b, numbers) # reduce() multiplies all numbers in list
	return answer