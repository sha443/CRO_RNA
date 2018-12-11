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
		minStem = func.getMinStem(len(sequence))
		# # Override rule
		minStem = 3
		print(sequence)
		
		# Parameters
		iteration = 100
		popSize = 70
		KELossRate= 0.55
		MoleColl= 0.30
		InitialKE= 0
		alpha = 2
		beta = 8
		buffer = 0

		# Timer starts
		tictoc.tic()

		#----------------------------------------------------------------------------------------------
		# Population generation
		#----------------------------------------------------------------------------------------------
		mole = Molecule()
		mole.Mol(sequence, popSize, InitialKE,minStem)
		
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
		sen,sp,f_m,tp,fp,fn,time,ene = C.CRO(popSize, KELossRate, MoleColl, InitialKE, alpha, beta, buffer, sequence, mole,iteration,path,filename)
		return sen,sp,f_m,tp,fp,fn,time,ene
	# end function
	def Test(self,filename):
		path = "../data/dk/"
		table = "dk"
		# filename = "PKB1.txt" # Manual input
		sen,sp,f1,tp,fp,fn,time,ene = main().run(filename,path)
		time = float(time)
		ene = float(ene)
		sqlite.helperDB(table,filename,sen,sp,f1,tp,fp,fn,time,ene)
# end
# end class

#-----------------------------------------------------------------------------------------
# Manual test area
#-----------------------------------------------------------------------------------------
# main().Test("GaLV.txt")

#-----------------------------------------------------------------------------------------
# Command line processing area
#-----------------------------------------------------------------------------------------
commandline = sys.argv
main().Test(commandline[1])