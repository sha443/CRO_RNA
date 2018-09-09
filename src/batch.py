import os
import main

directory = 'E:\HelloWorld\RNA\RSPPk\data\input\short'

for fileName in os.listdir(directory):
	print(fileName)
	main.main(fileName)
