import os
import sys
import glob

def fasta(fasta_file):
	lines = []              # Store ids and sequences in list
	input_list = []
	f = open(path+fasta_file,"U")
	for line in f:                                  
		if line:
			lines.append(line) 
		# endif
	# endfor

	fileId = lines[0]
	fileId = fileId.replace('>','')
	fileId = fileId.replace('\n','')
	print(fileId)

	sequence = lines[1]
	sequence = sequence.replace(' ', '')
	sequence = sequence.replace('\n', '')
	sequence = sequence.upper()
	print(sequence)

	if(fileId!="IMPORTSYS" or fileId!="import os\n"):
		file = open("./txt/"+fileId+".txt","w")
		file.write(sequence)
# end function


path = 'E:\HelloWorld\RNA\Daatasets\Datasets-master\Datasets-master\input\ipknot/'
fastaFiles = os.listdir(path)
for file in fastaFiles:
	print(file)
	fasta(file)
# endfor
