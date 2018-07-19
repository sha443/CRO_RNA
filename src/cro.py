import os
import population

def main():

	filename = "../data/HPeV1.txt"
	file = open(filename,"r",)
	sequence = file.readline()
	#print(sequence)

	#----------------------------------------------------------------------------------------------
	# Population generation
	#----------------------------------------------------------------------------------------------
	noOfPopulation = 50
	dotplot = population.Checkerboard(sequence)
	infoTable = population.FindDiagonal(sequence,dotplot)
	molecule, stemPool, infoEnergy = population.GenerateMolecule(len(sequence),noOfPopulation,infoTable)
	population.PrintInfo(molecule,stemPool,infoEnergy)

	#population.Overlap(molecule,stemPool)

main()

