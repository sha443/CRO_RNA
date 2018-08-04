import random

def Intermolecular(molecule1, molecule2):
	length1 = len(molecule1)
	length2 = len(molecule2)
	m1 = list(range(length1))
	m2 = list(range(length2))

	#Random numbers x1, x2 generation
	x1 = random.randint(0, length1)
	for j in range(4000):
	    for k in range(200):
	        pass
	    #Endf
	#Endf
	x2 = random.randint(0, length2)

	# Randormly choose form molecule1 or molecule2
	for i in range(0,length1):
	    if (i<x1 or i>x2):	#if odd segments
	        m1[i] = molecule1[i]
	        m2[i] = molecule2[i]
	    elif (i>=x1 and x2>=i):	# if even segment
	        m1[i] = molecule2[i]
	        m2[i] = molecule1[i]

	#test
	# print(m1)
	# print(m2)
	# Return 2 new molecule
	return m1,m2

#Module Test
#Intermolecular([1, 2, 4, 5, 8, 10, 0, 3, 5, 1],[3, 2, 0, 5, 8, 10, 5, 2, 5, 1])