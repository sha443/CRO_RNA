import os
import population
import molecule

def main():

	filename = "../data/TYMV.txt"
	file = open(filename,"r",)
	sequence = file.readline()
	# Parameters
	popSize = 10
	KELossRate= 0.8
	MoleColl= 0.5
	InitialKE= 0
	alpha = 1
	beta = 5
	buffer =0

	#----------------------------------------------------------------------------------------------
	# Population generation
	#----------------------------------------------------------------------------------------------
	molecule.Molecule(sequence, popSize, InitialKE)
	
main()

