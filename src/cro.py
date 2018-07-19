import os
import population

def main():

	filename = "../data/TYMV.txt"
	file = open(filename,"r",)
	sequence = file.readline()
	#print(sequence)

	#----------------------------------------------------------------------------------------------
	# Population generation
	#----------------------------------------------------------------------------------------------
	noOfPopulation = 5
	dotplot = population.Checkerboard(sequence)
	infoTable = population.FindDiagonal(sequence,dotplot)
	molecule, stemPool, infoEnergy, moleculeEnergy = population.GenerateMolecule(sequence,len(sequence),noOfPopulation,infoTable)
	population.PrintInfo(molecule,stemPool,infoEnergy,moleculeEnergy)

main()

