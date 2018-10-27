import os
from multiprocessing import Process
def runInParallel(*fns):
    proc = []
    for fn, arg in fns:
        p = Process(target=fn, args=(arg,))
        p.start()
        proc.append(p)
    for p in proc:
        p.join()
    # endfor
# end function
def printFile(fileName):
	print(fileName)
# end fucntion

directory = 'E:\HelloWorld\RNA\RSPPk\data\cro\input/'

string = ""
for fileName in os.listdir(directory):
	print(fileName)
	string += "(printFile, "+ fileName+"),"
# endfor
string = string[:-1]
print(string)
runInParallel((printFile, "BaEV.txt"))
