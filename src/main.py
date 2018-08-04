import os
import population
from molecule import Molecule


class main():
	def __init__(self):
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
		m = Molecule()
		m.Mol(sequence, popSize, InitialKE)
	
program = main()

