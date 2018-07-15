import os
import population

def main():

	filename = "../data/test.txt"
	file = open(filename,"r",)
	sequence = file.readline()
	print(sequence)
	print("hello world")

main()