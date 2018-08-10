import os
import population
import pseudoknot
from molecule import Molecule
from cro import CRO


class main():
	def __init__(self):
		filename = "../data/TYMV.txt"
		file = open(filename,"r",)
		sequence = file.readline()
		# Parameters
		iteration = 10
		popSize = 10
		KELossRate= 0.8
		MoleColl= 0.5
		InitialKE= 1
		alpha = 1
		beta = 5
		buffer =0

		#----------------------------------------------------------------------------------------------
		# Population generation
		#----------------------------------------------------------------------------------------------
		sequence = sequence.upper()
		mol = Molecule()
		mol.Mol(sequence, popSize, InitialKE)

		C  = CRO()
		C.Init(10, .5, .4, 1, 1, 5, 0, sequence, mol)
		C.CRO(10, .5, .4, 1, 1, 5, 0, sequence, mol,iteration,"output")

		# print(mol.infoTable)
		# print(mol.moleculeTable)

		for population in mol.moleculeTable:
			stemList = []
			pkList = []
			for serial in population:
				# take i,j, len form infoTable according to the gene serial
				stemList.append(mol.infoTable[serial])
			# endfor
			pkList = pseudoknot.BuildPseudoknots(stemList)
			stemList.clear()
			print(pkList)
		#endfor
	
program = main()

