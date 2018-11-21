# Uncomment each segment and run

import os
import shutil
from os import path

directory = '/media/shahid/EDUCATIONAL/HelloWorld/RNA/RSPPk/data/hk_long/input/'
inD = '/media/shahid/EDUCATIONAL/HelloWorld/RNA/RSPPk/data/hk_long/benchmark/'
outD = '/media/shahid/EDUCATIONAL/HelloWorld/RNA/RSPPk/data/hk_long/benchmarkVal/'

# Move
# for fileName in os.listdir(directory):
# 	print(fileName)

# 	src = inD+fileName
# 	dst = outD+fileName
# 	if(path.exists(src)):
# 		shutil.move(src,dst)
# # end for


# Check if all files in input directory also exist in benchmark directory
sl = 1
for fileName in os.listdir(directory):

	src = directory+fileName
	dst = inD+fileName
	if(path.exists(dst)):
		continue
	else:
		print(sl,fileName)
		sl+=1
# end for

# print list of files in a directory
# for fileName in os.listdir(directory):
# 	print(fileName)
# end for


# # Sequence length range
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