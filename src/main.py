import os
import population
import pseudoknot
import energy
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
		# print(mol.infoTable)
		# print(mol.moleculeTable)

		#----------------------------------------------------------------------------------------------
		# Finding Psedoknot
		#----------------------------------------------------------------------------------------------
		for population in mol.moleculeTable:
			stemList = []
			pkList = []
			for serial in population:
				# take i,j, len form infoTable according to the gene serial
				stemList.append(mol.infoTable[serial])
			# endfor
			pkList,stems_shortened = pseudoknot.BuildPseudoknots(stemList)
			stemList.clear()
			print(pkList)
			print(stems_shortened)
		#endfor
		cc06,cc09,longPk = pseudoknot.ScanList(pkList)

		#----------------------------------------------------------------------------------------------
		# Initial Energy Evaluation
		#----------------------------------------------------------------------------------------------
		# energy.CC06(cc06,stemList,sequence)
		# print(cc06)


		#----------------------------------------------------------------------------------------------
		# Optimize with CRO
		#----------------------------------------------------------------------------------------------
		C  = CRO()
		C.Init(popSize, KELossRate, MoleColl, InitialKE, alpha, beta, buffer, sequence, mol)
		C.CRO(popSize, KELossRate, MoleColl, InitialKE, alpha, beta, buffer, sequence, mol,iteration,"output")

		

		
	
program = main()

