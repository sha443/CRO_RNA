import os
import sys
import glob
from main import main
from subprocess import call
def fasta(commandline):
	lines = []              # Store ids and sequences in list
	input_list = []
	fasta_file = commandline[1]
	f = open(fasta_file,"U")
	for line in f:                                  
		if line:
			lines.append(line) 
		# endif
	# endfor

	fileId = lines[0]
	fileId = fileId.replace('>','')
	print(fileId)

	sequence = lines[1]
	sequence = sequence.replace(' ', '')
	sequence = sequence.upper()
	print(sequence)
# end function


path = 'E:\HelloWorld\RNA\Daatasets\Datasets-master\Datasets-master\input\ipknot/'
fastaFiles = os.listdir(path)
for file in fastaFiles:
	print(file)
	fasta(file)
# endfor
