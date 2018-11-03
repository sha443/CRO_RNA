import os
import shutil
from os import path

directory = '/media/shahid/EDUCATIONAL/HelloWorld/RNA/RSPPk/data/ipknot/input/'
inD = '/media/shahid/EDUCATIONAL/HelloWorld/RNA/RSPPk/data/ipknot/benchmark/'
outD = '/media/shahid/EDUCATIONAL/HelloWorld/RNA/RSPPk/data/ipknot/benchmarkVal/'

# Move
# for fileName in os.listdir(directory):
# 	print(fileName)

# 	src = inD+fileName
# 	dst = outD+fileName
# 	if(path.exists(src)):
# 		shutil.move(src,dst)
# # end for


# Compare
# sl = 1
# for fileName in os.listdir(directory):

# 	src = directory+fileName
# 	dst = outD+fileName
# 	if(path.exists(dst)):
# 		continue
# 	else:
# 		print(sl,fileName)
# 		sl+=1
# # end for

# print list
# for fileName in os.listdir(directory):
# 	print(fileName)
# end for


# # Sequence length
# min=1000
# max=0
# directory = 'E:/HelloWorld/RNA/RSPPk/data/cro/input/'
# for fileName in os.listdir(directory):
# 	file = open(directory+fileName,"r")
# 	Sequence = file.readline()

# 	length = len(Sequence)
# 	if(length>max):
# 		max = length
# 	if(length<min):
# 		min = length
# 	# print(fileName,len(Sequence))
# # end for
# print(min,max)