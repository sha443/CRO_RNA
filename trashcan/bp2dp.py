data = []
data.append('')
file = open("PKB100.bpseq")
for lines in file:
	lines = lines.replace('\n','')
	out = lines.split(' ')
	data.append(out)
# endfor
# print(data)
mol = []
length = len(data)
for i in range(length):
	mol.append('.')
# endfor

for i in range(1,length):
	match = int(data[i][2])
	if(match!=0 and mol[i]=='.' and mol[match]=='.'):
		# print(i,"--",data[i][2])
		mol[i] = '('
		mol[match] = ")"
	# endif
# endfor

for index in range(1,len(mol)):
	print(mol[index],end="")
# endfor
print("\n")
