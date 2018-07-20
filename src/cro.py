import os
import population
import onwall

def main():

	filename = "../data/TYMV.txt"
	file = open(filename,"r",)
	sequence = file.readline()
	#print(sequence)

	#----------------------------------------------------------------------------------------------
	# Population generation
	#----------------------------------------------------------------------------------------------
	noOfPopulation = 50
	dotplot = population.Checkerboard(sequence)
	infoTable = population.FindDiagonal(sequence,dotplot)
	molecule, stemPool, infoEnergy, moleculeEnergy, moleculeTable = population.GenerateMolecule(sequence,len(sequence),noOfPopulation,infoTable)
	population.PrintInfo(molecule,stemPool,infoEnergy,moleculeEnergy)

	#onwall.OnWall(moleculeTable)

main()

