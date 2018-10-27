#-----------------------------------------------------------------------------------------
# Parallel processing area
#-----------------------------------------------------------------------------------------
import threading
import time
import os

# Test("PKB3.txt")
directory = '/media/shahid/EDUCATIONAL/HelloWorld/RNA/RSPPk/data/preAlgorithm/input/'
for fileName in os.listdir(directory):
	cmd = "gnome-terminal -x python3 main.py "+fileName
	# print(cmd)
	os.system(cmd)
# end for