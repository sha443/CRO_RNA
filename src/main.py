import os
import population
import pseudoknot
from function import Function
import energy
from molecule import Molecule
from cro import CRO


class main():
	def __init__(self):
		filename = "../data/TMV.txt"
		file = open(filename,"r",)
		sequence = file.readline()
		# Parameters
		iteration = 10
		popSize = 1
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
			pkList,stemShortened = pseudoknot.BuildPseudoknots(stemList)
			# print(pkList)
			# print(stemShortened)
		#endfor
		cc06,cc09,longPk = pseudoknot.ScanList(pkList)

		#----------------------------------------------------------------------------------------------
		# Initial Pseudoknot Energy Evaluation
		#----------------------------------------------------------------------------------------------
		INIT = 7.0
		PENALTY = 0.1
		stem_dic = mol.infoTable  # Actually a list
		CC06Result = energy.CC06(cc06,stem_dic,stemShortened,sequence)
		CC09Result = energy.CC09(cc09,stem_dic)
		longPKResult = energy.LongPK(longPk, stem_dic, INIT, PENALTY)
		# Now we form a pseudoknot dictionary out of the three results
		pk_core_dic = {}
		if(CC06Result):
			pk_core_dic.update(CC06Result)
		if(CC09Result):
			pk_core_dic.update(CC09Result)
		if(longPKResult):
			pk_core_dic.update(longPKResult)

		# Sorted pseudoknot dictionary
		sorted(pk_core_dic)
		#----------------------------------------------------------------------------------------------
		# Without optimization
		#----------------------------------------------------------------------------------------------
		function = Function()
		function.Merge(mol.basePairs,pk_core_dic,len(sequence))
		
		#----------------------------------------------------------------------------------------------
		# Optimize with CRO
		#----------------------------------------------------------------------------------------------
		C  = CRO()
		C.Init(popSize, KELossRate, MoleColl, InitialKE, alpha, beta, buffer, sequence, mol)
		C.CRO(popSize, KELossRate, MoleColl, InitialKE, alpha, beta, buffer, sequence, mol,iteration,"output")
	

program = main()

