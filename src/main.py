import os
import sys
import population
import energy
from function import Function as func
from molecule import Molecule
from cro import CRO
import tictoc
import sqlite

class main():
	def __init__(self):
		pass
	def run(self,filename,path):
		
		file = open(path+"input/"+filename,"r",)
		sequence = file.readline()

		# Clean up data
		sequence = sequence.replace(' ', '')
		sequence = sequence.upper()
		print(sequence)
		
		# Parameters
		iteration = 10
		popSize = 20
		KELossRate= 0.8
		MoleColl= 0.5
		InitialKE= 0
		alpha = 1
		beta = 5
		buffer =0

		# Timer starts
		tictoc.tic()

		#----------------------------------------------------------------------------------------------
		# Population generation
		#----------------------------------------------------------------------------------------------
		mole = Molecule()
		mole.Mol(sequence, popSize, InitialKE)
		
		# Save initial informations
		minEnergy = 99999
		index = 0
		minIndex = 0
		initPop = open(path+"output/initial_population_"+filename,"a")
		for molecule in mole.molecules:
			# initPop.write(population.PrintableMolecule(molecule)
			# initPop.write(str(mole.PE[index]))
			# initPop.write("\n")
			if(mole.moleculeEnergy[index]<minEnergy):
				minIndex = index
				minEnergy=mole.moleculeEnergy[index]

			index+=1
		# endfor
		# initPop.write("\n")

		# Initial Comparison
		benchmark = open(path+"benchmark/"+filename,"r").read()
		predicted = population.PrintableMolecule(mole.molecules[minIndex])
		# print(predicted,end="\t")
		# print(minEnergy)
		# print("(sen, sp, f, tp, fp, fn)")
		# print("==================================")
		# print("Before CRO:")
		# # sensitivity,specificity,f_measure,true_basepair,false_positive_basepair,false_negative_basepair
		# print(func.Performance(predicted,benchmark))
		# print(mole.elements[minIndex])

		#----------------------------------------------------------------------------------------------
		# Optimize with CRO
		#----------------------------------------------------------------------------------------------
		C  = CRO()
		# C.Init(popSize, KELossRate, MoleColl, InitialKE, alpha, beta, buffer, sequence, mole)
		sen,sp,f_m,tp,fp,fn = C.CRO(popSize, KELossRate, MoleColl, InitialKE, alpha, beta, buffer, sequence, mole,iteration,path,filename)
		return sen,sp,f_m,tp,fp,fn
	# end function
	def Test(self,filename):
		print(filename,"problem")
		db = "../data/database/ipknot.db"
		path = "../data/ipknot/"
		# filename = "PKB1.txt" # Manual input
		sen,sp,f1,tp,fp,fn = main().run(filename,path)
		sqlite.helperDB(db,filename,sen,sp,f1,tp,fp,fn)
# end
# end class


#-----------------------------------------------------------------------------------------
# Test area
#-----------------------------------------------------------------------------------------
def Test(filename):
	print(filename,"problem")
	db = "../data/database/ipknot.db"
	path = "../data/ipknot/"
	# filename = "PKB1.txt" # Manual input
	sen,sp,f1,tp,fp,fn = main().run(filename,path)
	sqlite.helperDB(db,filename,sen,sp,f1,tp,fp,fn)
# end
# Test("PKB3.txt")

#-----------------------------------------------------------------------------------------
# Command line processing area
#-----------------------------------------------------------------------------------------
# commandline = sys.argv
# print(commandline[1])
# # print(commandline[2])
# file = open('log.txt')
# file.write('Hwl')
# main().run(commandline[1],path)