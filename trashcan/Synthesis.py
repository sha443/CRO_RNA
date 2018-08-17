import random

def Synthesis(molecule1, molecule2):

	length = len(molecule1)
	m = list(range(length))
	for i in range(0,length):
		r = random.uniform(0, 1)
		if (r<.5):
			m[i] = molecule1[i]
		else:
		   m[i] = molecule2[i]

	#test
	#print(m)
	return m
#Module Test
#Synthesis([1, 2, 4, 5, 8, 10, 0, 3, 5, 1],[3, 2, 0, 5, 8, 10, 5, 2, 5, 1])