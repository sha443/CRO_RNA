#-----------------------------------------------------------------------------------------
# Parallel processing area
#-----------------------------------------------------------------------------------------
import threading
import time
import os

# directory = 'E:/HelloWorld/RNA/RSPPk/data/cro/input/'
directory = '/media/shahid/EDUCATIONAL/HelloWorld/RNA/RSPPk/data/dk/input/'
for fileName in os.listdir(directory):
	cmd = "gnome-terminal -x python3 main.py "+fileName
	# print(cmd)
	os.system(cmd)


	# # windows
	# cmd_win ="python main.py "+fileName
	# os.system(cmd_win)
	
	# process = os.popen(cmd_win)
	# break
# end for
