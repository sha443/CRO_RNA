import os
import population

def main():

	filename = "../data/test.txt"
	file = open(filename,"r",)
	sequence = file.readline()
	#print(sequence)

	#----------------------------------------------------------------------------------------------
	# Population generation
	#----------------------------------------------------------------------------------------------
	noOfPopulation = 10
	dotplot = population.Checkerboard(sequence)
	infoTable = population.FindDiagonal(sequence,dotplot)
	molecule, stemPool = population.GenerateMolecule(len(sequence),noOfPopulation,infoTable)
	population.PrintInfo(molecule,stemPool)

main()

