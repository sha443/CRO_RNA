import os
import sys
import population
import energy
from function import Function as func
from molecule import Molecule
from cro import CRO
import tictoc


class main():
	def run(self,filename,path):
		
		file = open(path+"input/"+filename,"r",)
		sequence = file.readline()

		# Clean up data
		sequence = sequence.replace(' ', '')
		sequence = sequence.upper()
		print(sequence)
		
		# Parameters
		iteration = 10
		popSize = 10
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
		# Initial INN-HB energy calculation
		#----------------------------------------------------------------------------------------------
		# Unique stemlist energy
		# Sorted by energy in ascending order
		# basePairsEnergy = energy.Turner04Handlar(mole.basePairs,sequence)
		# print(basePairsEnergy)
		#----------------------------------------------------------------------------------------------
		# Optimize with CRO
		#----------------------------------------------------------------------------------------------
		C  = CRO()
		# C.Init(popSize, KELossRate, MoleColl, InitialKE, alpha, beta, buffer, sequence, mole)
		C.CRO(popSize, KELossRate, MoleColl, InitialKE, alpha, beta, buffer, sequence, mole,iteration,path,filename)

	# end function
# end class


#-----------------------------------------------------------------------------------------

path = "../data/sa/"
filename = "Ec_PK3.txt" # Manual input
main().run(filename,path)

# commandline = sys.argv
# print(commandline[1])
# # print(commandline[2])
# file = open('log.txt')
# file.write('Hwl')
# main().run(commandline[1],path)