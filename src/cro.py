import os
import population

def main():

	filename = "../data/test.txt"
	file = open(filename,"r",)
	sequence = file.readline()
	#print(sequence)
	population.Checkerboard(sequence)
	population.FindDiagonal(sequence)
	population.GenerateMolecule(len(sequence),25)


main()
