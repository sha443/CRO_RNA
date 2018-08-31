#===================================================================================
# INN-HB energy model
#===================================================================================
def Turner(infoEnergy,sequence):
	# Energy calculation
	flag1 = 0   # Found au/gu penalty
	flag2 = 0   # Check if it is the first input
	flag3 = 0
	flag4 = 0
	total_energy = 0
	molecule_energy = {}
	energy = 0
	infoEnergy.sort()
	for i in range(len(infoEnergy)-1):
	    
	    if(infoEnergy[i][0]+1==infoEnergy[i+1][0]):
	        flag3 = 1
	        flag4 = 1
	        if (flag2 == 0 and ((sequence[infoEnergy[i][0]] == 'A') or (sequence[infoEnergy[i][0]] == 'U') or (sequence[infoEnergy[i][0]] == 'G' and sequence[infoEnergy[i][1]] == 'U') or (sequence[infoEnergy[i][0]]== 'U' and sequence[infoEnergy[i][1]] == 'G'))):
	            flag1 = 1
	            flag2 = 1
	            energy += .45
	            energy += CalculateEnergy(sequence[infoEnergy[i][0]], sequence[infoEnergy[i][1]], sequence[infoEnergy[i+1][0]], sequence[infoEnergy[i+1][1]])
	        else:
	            energy += CalculateEnergy(sequence[infoEnergy[i][0]], sequence[infoEnergy[i][1]], sequence[infoEnergy[i+1][0]], sequence[infoEnergy[i+1][1]])
	    else:
	        flag4 = 2
	        if(flag3==1):
	            if (((sequence[infoEnergy[i][0]] == 'A') or (sequence[infoEnergy[i][0]] == 'U') or (sequence[infoEnergy[i][0]] == 'G' and sequence[infoEnergy[i][1]] == 'U') or (sequence[infoEnergy[i][0]] == 'U' and sequence[infoEnergy[i][1]] == 'G'))):
	                energy += .45
	                energy += .43
	                energy += 4.09
	                total_energy += energy
	                flag2 = 0
	                flag1 = 0
	            else:
	                if(flag1==1):
	                    energy += .43
	                    energy += 4.09
	                    total_energy += energy
	                    flag2 = 0
	                    flag1 = 0
	                elif(flag1 != 1):
	                    energy += 4.09
	                    total_energy += energy
	                    flag2 = 0
	                    flag1 = 0
	                # Endifelse
	            flag3 = 0
	        #Endif
	    #Endelse
	#Endfor
	if (flag4 != 2):            
	    if (flag3 == 1):
	        if (((sequence[infoEnergy[len(infoEnergy)-1][0]] == 'A') or (sequence[infoEnergy[len(infoEnergy) - 1][0]] == 'U') or (sequence[infoEnergy[len(infoEnergy) - 1][0]] == 'G' and sequence[infoEnergy[len(infoEnergy) - 1][1]] == 'U') or (sequence[infoEnergy[len(infoEnergy) - 1][0]] == 'U' and sequence[infoEnergy[len(infoEnergy) - 1][1]] == 'G'))):
	            energy += .45
	            energy += .43
	            energy += 4.09
	            total_energy += energy
	            flag2 = 0
	            flag1 = 0
	        else:
	            if (flag1 == 1):
	                energy += .43
	                energy += 4.09
	                total_energy += energy
	                flag2 = 0
	                flag1 = 0
	            elif (flag1 != 1):
	                energy += 4.09
	                total_energy += energy
	                flag2 = 0
	                flag1 = 0
	        flag3 = 0
	        #Endif
	    #Endif
	# Endif
	return total_energy
# end function
def Turner04Handlar(basePairs,sequence):
	for base in basePairs:
		i,j,length = base
		stem = []
		for left,right in zip(range(i,i+length),range(j,j-length,-1)):
			stem.append([left,right])
		# endfor

		energy = Turner04(stem,sequence)
		basePairs[base] = energy
	# endfor
	bp = [(k, basePairs[k]) for k in sorted (basePairs,key = basePairs.get)]
	# sorted(basePairs)
	return bp
# end function
def Turner04(stem,sequence):
	# Objective: given an stem calculate the energy using Turner model 2004
	iFlag = 0
	energy = 0
	length = len(stem)-1
	# Symmetry correction
	lh = ""
	rh = ""
	for i in range(stem[0][0],stem[0][0]+length+1):
		lh += sequence[i]
	for i in range(stem[length][1],stem[0][1]+1):
		rh += sequence[i]	
	if(lh==rh):
		energy += 0.43	# Symmetric correction
		print("+0.43 sym")

	# AU / GU per end penalty

	# starting side energy
	if((sequence[stem[0][0]] == 'A' and sequence[stem[0][1]] == 'U') or (sequence[stem[0][0]] == 'U' and sequence[stem[0][1]] == 'A')):
		energy += 0.45	# per AU end
		print("+0.45 AUstart")

	elif((sequence[stem[0][0]] == 'G' and sequence[stem[0][1]] == 'U') or (sequence[stem[0][0]] == 'U' and sequence[stem[0][1]] == 'G')):
		energy += 0.45	# per GU end
		print("+0.45 GUstart")

	# ending side energy
	if((sequence[stem[length][0]] == 'U' and sequence[stem[length][1]] == 'A') or (sequence[stem[length][0]] == 'A' and sequence[stem[length][1]] == 'U')):
		energy += 0.45	# per AU end
		print("+0.45 AUend")
	elif((sequence[stem[length][0]] == 'U' and sequence[stem[length][1]] == 'G') or (sequence[stem[length][0]] == 'G' and sequence[stem[length][1]] == 'U')):
		energy += 0.45	# per GU end
		print("+0.45 GUend")

	for i in range(length):
		# intermolecular initiation for AU or GC
		if(iFlag==0 and ((sequence[stem[i][0]] == 'A' and sequence[stem[i][1]] == 'U') or (sequence[stem[i][0]] == 'U' and sequence[stem[i][1]] == 'A') or (sequence[stem[i][0]] == 'G' and sequence[stem[i][1]] == 'C') or (sequence[stem[i][0]] == 'C' and sequence[stem[i][1]] == 'G'))):
			energy += 4.09	# Intermolecular initiation
			iFlag = 1		# Initiation complete
			print("+4.09 II")

		# Regular energy calculation
		# print((sequence[stem[i][0]], sequence[stem[i][1]], sequence[stem[i+1][0]], sequence[stem[i+1][1]]))
		temp = CalculateEnergy(sequence[stem[i][0]], sequence[stem[i][1]], sequence[stem[i+1][0]], sequence[stem[i+1][1]])
		energy += temp
		forEnergy = ""
		forEnergy += sequence[stem[i][0]] 
		forEnergy += sequence[stem[i][1]]
		forEnergy += sequence[stem[i+1][0]]
		forEnergy += sequence[stem[i+1][1]]
		print(temp,forEnergy)
	print(energy,"total ")
	return energy
# end function
# Calclates the Gibbs free energy of a molecule on INN-HB model
def CalculateEnergy(p1, p2, p3, p4):
        
    ene = 0
    if ((p1 == 'A' and p2 == 'U' and p3 == 'A' and p4 == 'U') or (p1 == 'U' and p2 == 'A' and p3 == 'U' and p4 == 'A')):
    
        ene = -.93
        return ene
    
    if ((p1 == 'A' and p2 == 'U' and p3 == 'U' and p4 == 'A')):
    
        ene = -1.10
        return ene
    
    if ((p1 == 'A' and p2 == 'U' and p3 == 'G' and p4 == 'U') or (p1 == 'U' and p2 == 'G' and p3 == 'U' and p4 == 'A')):
    
        ene = -.55
        return ene
    
    if ((p1 == 'A' and p2 == 'U' and p3 == 'U' and p4 == 'G') or (p1 == 'G' and p2 == 'U' and p3 == 'U' and p4 == 'A')):
    
        ene = -1.36
        return ene
    
    if ((p1 == 'A' and p2 == 'U' and p3 == 'G' and p4 == 'C') or (p1 == 'C' and p2 == 'G' and p3 == 'U' and p4 == 'A')):
    
        ene = -2.08
        return ene
    
    if ((p1 == 'A' and p2 == 'U' and p3 == 'C' and p4 == 'G') or (p1 == 'G' and p2 == 'C' and p3 == 'U' and p4 == 'A')):
    
        ene = -2.24
        return ene
    
    if ((p1 == 'U' and p2 == 'A' and p3 == 'A' and p4 == 'U')):
    
        ene = -1.33
        return ene
    
    if ((p1 == 'U' and p2 == 'A' and p3 == 'G' and p4 == 'U') or (p1 == 'U' and p2 == 'G' and p3 == 'A' and p4 == 'U')):
    
        ene = -1.0
        return ene
    
    if ((p1 == 'U' and p2 == 'A' and p3 == 'U' and p4 == 'G') or (p1 == 'G' and p2 == 'U' and p3 == 'A' and p4 == 'U')):
    
        ene = -1.27
        return ene
    
    if ((p1 == 'U' and p2 == 'A' and p3 == 'C' and p4 == 'G') or (p1 == 'G' and p2 == 'C' and p3 == 'A' and p4 == 'U')):
    
        ene = -2.35
        return ene
    
    if ((p1 == 'A' and p2 == 'U' and p3 == 'A' and p4 == 'U') or (p1 == 'U' and p2 == 's' and p3 == 'U' and p4 == 's')):
    
        ene = -.93
        return ene
    
    if ((p1 == 'U' and p2 == 'A' and p3 == 'G' and p4 == 'C') or (p1 == 'C' and p2 == 'G' and p3 == 'A' and p4 == 'U') or (p1 == 'G' and p2 == 'U' and p3 == 'G' and p4 == 'C') or (p1 == 'C' and p2 == 'G' and p3 == 'U' and p4 == 'G')):
    
        ene = -2.11
        return ene
    
    if ((p1 == 'G' and p2 == 'U' and p3 == 'C' and p4 == 'G') or (p1 == 'G' and p2 == 'C' and p3 == 'U' and p4 == 'G')):
    
        ene = -2.51
        return ene
    
    if ((p1 == 'G' and p2 == 'U' and p3 == 'G' and p4 == 'U') or (p1 == 'U' and p2 == 'G' and p3 == 'U' and p4 == 'G')):
    
        ene = -.5
        return ene
    
    if ((p1 == 'G' and p2 == 'U' and p3 == 'U' and p4 == 'G')):
    
        ene = +1.29
        return ene
    
    if ((p1 == 'U' and p2 == 'G' and p3 == 'G' and p4 == 'C') or (p1 == 'C' and p2 == 'G' and p3 == 'G' and p4 == 'U')):
    
        ene = -1.41
        return ene
    
    if ((p1 == 'U' and p2 == 'G' and p3 == 'C' and p4 == 'G') or (p1 == 'G' and p2 == 'C' and p3 == 'G' and p4 == 'U')):
    
        ene = -1.53
        return ene
    
    if ((p1 == 'U' and p2 == 'G' and p3 == 'G' and p4 == 'U')):
    
        ene = +.3
        return ene
    
    if ((p1 == 'C' and p2 == 'G' and p3 == 'G' and p4 == 'C')):
    
        ene = -2.36
        return ene
    
    if ((p1 == 'G' and p2 == 'C' and p3 == 'C' and p4 == 'G')):
    
        ene = -3.42
        return ene
    
    if ((p1 == 'G' and p2 == 'C' and p3 == 'G' and p4 == 'C') or (p1 == 'C' and p2 == 'G' and p3 == 'C' and p4 == 'G')):
    
        ene = -3.26
        return ene
    
    return ene

# End function



stem = []
# Test 1
# ∆G°37 = –7.94 kcal/mol
#	AGCGCU
#	||||||
#	UCGCGA
# sequence="AGCGCUAGCGCU"
# stem.append([0,11])
# stem.append([1,10])
# stem.append([2,9])
# stem.append([3,8])
# stem.append([4,7])
# stem.append([5,6])

# Test 2
# ∆G°37 = –6.04 kcal/mol
#	GCACG
#	|||||
#	CGUGC
# sequence="GCACGCGUGC"
# stem.append([0,9])
# stem.append([1,8])
# stem.append([2,7])
# stem.append([3,6])
# stem.append([4,5])

# Test 3
# ∆G°37 = –3.62 kcal/mol
#	GGUCGUGU
#	||||||||
#	CUGGUGCG
# sequence="GGUCGUGUGCGUGGUC"
# stem.append([0,15])
# stem.append([1,14])
# stem.append([2,13])
# stem.append([3,12])
# stem.append([4,11])
# stem.append([5,10])
# stem.append([6,9])
# stem.append([7,8])


# Test 4 (Coaxial stacking test with INN-HB)
# ∆G°37 = -2.24 kcal/mol
#	CACA
#	||||
#	GUGU
# sequence="CACAUGUG"
# stem.append([0,7])
# stem.append([1,6])
# stem.append([2,5])
# stem.append([3,4])


# Test 5 (DotPlot)
# ∆G°37 = -0.20 kcal/mol
#	UGAA
#	||||
#	ACUU
# sequence="CAAUUUUCUGAAAAUUUUCAC"
# stem.append([8,19])
# stem.append([9,18])
# stem.append([10,17])
# stem.append([11,16])

# Test 6 (TMV)
sequence ="GGGGUUCGAAUCCCCCCGUUACCCCCGGUAGGGGCCCA"
sequence = sequence.upper()
stem.append([0,14])
stem.append([1,13])
stem.append([2,12])
stem.append([3,11])

# Implemented by nabid
print(Turner(stem,sequence))
# Implemented by shahid
print(Turner04(stem,sequence))