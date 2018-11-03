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
		iteration = 20
		popSize = 20
		KELossRate= 0.85
		MoleColl= 0.30
		InitialKE= 0
		alpha = 1
		beta = 10
		buffer = 0

		# Timer starts
		tictoc.tic()

		#----------------------------------------------------------------------------------------------
		# Population generation
		#----------------------------------------------------------------------------------------------
		mole = Molecule()
		mole.Mol(sequence, popSize, InitialKE)
		
		# # Save initial informations
		# minEnergy = 99999
		# index = 0
		# minIndex = 0
		# initPop = open(path+"output/initial_population_"+filename,"a")
		# for molecule in mole.molecules:
		# 	# initPop.write(population.PrintableMolecule(molecule)
		# 	# initPop.write(str(mole.PE[index]))
		# 	# initPop.write("\n")
		# 	if(mole.moleculeEnergy[index]<minEnergy):
		# 		minIndex = index
		# 		minEnergy=mole.moleculeEnergy[index]

		# 	index+=1
		# # endfor
		# initPop.write("\n")

		#----------------------------------------------------------------------------------------------
		# Optimize with CRO
		#----------------------------------------------------------------------------------------------
		C  = CRO()
		# C.Init(popSize, KELossRate, MoleColl, InitialKE, alpha, beta, buffer, sequence, mole)
		sen,sp,f_m,tp,fp,fn = C.CRO(popSize, KELossRate, MoleColl, InitialKE, alpha, beta, buffer, sequence, mole,iteration,path,filename)
		return sen,sp,f_m,tp,fp,fn
	# end function
	def Test(self,filename):
		db = "../data/database/sa.db"
		path = "../data/sa/"
		# filename = "PKB1.txt" # Manual input
		sen,sp,f1,tp,fp,fn = main().run(filename,path)
		sqlite.helperDB(db,filename,sen,sp,f1,tp,fp,fn)
# end
# end class

# main().Test("CrPV.txt")

#-----------------------------------------------------------------------------------------
# Command line processing area
#-----------------------------------------------------------------------------------------
commandline = sys.argv
main().Test(commandline[1])