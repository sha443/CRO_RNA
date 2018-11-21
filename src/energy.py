import math
import os
accEne = -10.0
# Loop entropy for loop L1 and stem S2 (deep groove)
# First entry is loop size, second entry is stem size    
loop1_dic_cc ={
(1,3): 100.0, (1,4) : 4.4 , (1,5) : 2.3 , (1,6) : 2.3 , (1,7) : 2.3 , (1,8) : 4.4 , (1,9) : 5.5 , (1,10) : 6.9 , (1,11) : 8.7 , (1,12) : 9.8 ,
(2,3) : 6.4 , (2,4) : 4.4 , (2,5) : 4.4 , (2,6) : 4.4 , (2,7) : 4.4 , (2,8) : 4.4 , (2,9) : 5.5 , (2,10) : 6.9 , (2,11) : 8.7 , (2,12) : 9.8 , 
(3,3) : 6.4 , (3,4) : 4.5 , (3,5) : 4.6 , (3,6) : 4.8 , (3,7) : 5.0 , (3,8) : 5.2 , (3,9) : 5.5 , (3,10) : 6.9 , (3,11) : 8.7 , (3,12) : 9.8 ,
(4,3) : 6.4 , (4,4) : 5.4 , (4,5) : 5.7 , (4,6) : 5.8 , (4,7) : 5.9 , (4,8) : 5.7 , (4,9) : 6.4 , (4,10) : 6.9 , (4,11) : 8.7 , (4,12) : 9.8 ,
(5,3) : 6.6 , (5,4) : 5.6 , (5,5) : 6.0 , (5,6) : 6.0 , (5,7) : 6.2 , (5,8) : 6.4 , (5,9) : 6.7 , (5,10) : 7.5 , (5,11) : 8.7 , (5,12) : 9.8 ,
(6,3) : 6.6 , (6,4) : 6.0 , (6,5) : 6.5 , (6,6) : 6.5 , (6,7) : 6.8 , (6,8) : 6.7 , (6,9) : 7.2 , (6,10) : 7.7 , (6,11) : 8.8 , (6,12) : 9.2 ,
(7,3) : 6.8 , (7,4) : 6.3 , (7,5) : 6.9 , (7,6) : 6.8 , (7,7) : 7.0 , (7,8) : 7.1 , (7,9) : 7.5 , (7,10) : 8.1 , (7,11) : 8.9 , (7,12) : 9.5 ,
(8,3) : 6.9 , (8,4) : 6.6 , (8,5) : 7.2 , (8,6) : 7.1 , (8,7) : 7.3 , (8,8) : 7.3 , (8,9) : 7.9 , (8,10) : 8.3 , (8,11) : 9.1 , (8,12) : 9.6 ,
(9,3) : 7.1 , (9,4) : 6.9 , (9,5) : 7.5 , (9,6) : 7.4 , (9,7) : 7.6 , (9,8) : 7.5 , (9,9) : 8.1 , (9,10) : 8.6 , (9,11) : 9.2 , (9,12) : 9.7 ,
(10,3): 7.3 , (10,4): 7.1 , (10,5): 7.8 , (10,6): 7.6 , (10,7): 7.8 , (10,8): 7.7 , (10,9): 8.3 , (10,10): 8.8 , (10,11): 9.3 , (10,12): 9.8 ,
(11,3): 7.5 , (11,4): 7.3 , (11,5): 8.0 , (11,6): 7.8 , (11,7): 8.0 , (11,8): 7.9 , (11,9): 8.5 , (11,10): 8.9 , (11,11): 9.3 , (11,12): 9.8 }

# Loop entropy for loop L2 (L3) and stem S1 (shallow groove)
# First entry is loop size, second entry is stem size
loop3_dic_cc ={
(1,3) : 100.0 , (1,4) : 100.0 , (1,5) : 100.0 , (1,6) : 100.0 , (1,7) : 100.0 , (1,8) : 100.0 , (1,9) : 100.0 , (1,10) : 100.0 , (1,11) : 100.0 , (1,12) : 100.0 ,
(2,3) : 6.5 , (2,4) : 9.2 , (2,5) : 9.8 , (2,6) : 11.9 , (2,7) : 12.4 , (2,8) : 12.1 , (2,9) : 13.7 , (2,10) : 13.7 , (2,11) : 15.9 , (2,12) : 18.7 ,
(3,3) : 6.5 , (3,4) : 9.2 , (3,5) : 9.8 , (3,6) : 11.9 , (3,7) : 12.4 , (3,8) : 12.1 , (3,9) : 13.7 , (3,10) : 13.7 , (3,11) : 15.9 , (3,12) : 18.7 ,
(4,3) : 6.5 , (4,4) : 9.2 , (4,5) : 9.8 , (4,6) : 11.9 , (4,7) : 12.4 , (4,8) : 12.1 , (4,9) : 13.7 , (4,10) : 13.7 , (4,11) : 15.9 , (4,12) : 18.7 ,
(5,3) : 6.6 , (5,4) : 9.2 , (5,5) : 9.8 , (5,6) : 11.9 , (5,7) : 12.4 , (5,8) : 12.1 , (5,9) : 13.7 , (5,10) : 13.7 , (5,11) : 15.9 , (5,12) : 18.7 ,
(6,3) : 6.7 , (6,4) : 8.9 , (6,5) : 9.8 , (6,6) : 11.9 , (6,7) : 12.4 , (6,8) : 12.1 , (6,9) : 13.7 , (6,10) : 13.7 , (6,11) : 15.9 , (6,12) : 18.7 ,
(7,3) : 6.9 , (7,4) : 8.9 , (7,5) : 9.1 , (7,6) : 11.9 , (7,7) : 12.4 , (7,8) : 12.1 , (7,9) : 13.7 , (7,10) : 13.7 , (7,11) : 15.9 , (7,12) : 18.7 ,
(8,3) : 7.1 , (8,4) : 8.9 , (8,5) : 8.9 , (8,6) : 11.0 , (8,7) : 12.4 , (8,8) : 12.1 , (8,9) : 13.7 , (8,10) : 13.7 , (8,11) : 15.9 , (8,12) : 18.7 ,
(9,3) : 7.2 , (9,4) : 9.0 , (9,5) : 8.8 , (9,6) : 10.4 , (9,7) : 11.4 , (9,8) : 11.6 , (9,9) : 13.7 , (9,10) : 12.7 , (9,11) : 15.9 , (9,12) : 18.7 ,
(10,3): 7.4 , (10,4): 9.0 , (10,5): 8.8 , (10,6): 10.1 , (10,7): 11.0 , (10,8): 11.4 , (10,9): 12.6 , (10,10): 12.2 , (10,11): 14.1 , (10,12): 15.8 ,
(11,3): 7.6 , (11,4): 9.1 , (11,5): 8.8 , (11,6) : 9.9 , (11,7): 10.7 , (11,8): 11.2 , (11,9): 12.0 , (11,10): 11.8 , (11,11): 13.0 , (11,12): 14.2 ,
(12,3): 7.7 , (12,4): 9.2 , (12,5): 8.8 , (12,6) : 9.8 , (12,7): 10.5 , (12,8): 11.1 , (12,9): 11.5 , (12,10): 11.5 , (12,11): 12.4 , (12,12): 13.2 }

# l_min dictionary for given stem length S1
# stemlength1 : (l_min, a, b, c)

# S1 for L1 and S2 for L1 [CC06 eqn. 4] 

lmin_S1 ={
2:  (4,0.95,1.84,-0.67),  3: (2,0.32,1.92,-3.9),   4: (3,1.77,1.82,-5.76), 5: (4,3.99,1.55,-5.86),
6:  (4,7.73,1.29,-12.67), 7: (5,8.38,1.16,-11.45), 8: (5,4.52,1.61,-7.58), 9: (6,9.05,1.15,-11.45),
10: (6,4.77,1.68,-6.78), 11: (9,2.74,2.05,1.38),   12: (9,4.69,1.8,-1.11) }

# l_min dictionary for given stem length S2
# stemlength2 : (l_min, a, b, c)
lmin_S2 ={
2:  (4,0.12,1.96,0.52),   3:  (2,0.39,1.92,-3.89),  4: (1,-2.14,2.15,-2.09), 5: (1,-2.22,2.11,-2.25),
6:  (1,-2.4,2.18,-2.33),  7:  (1,-2.61,2.21,-2.32), 8: (2,-1.17,2.03,-1.96), 9: (2,-1.66,2.09,-1.98),
10: (2,-1.43,2.09,-2.93), 11: (5,-0.14,2.06,0.15), 12: (5,0.77,1.84,-0.65) }

# Dictionary for coaxial stacking
stack_dic ={
('AU','AU') : -0.9 , ('AU','CG') : -2.2 , ('AU','GC') : -2.1 , ('AU','GU') : -0.6 , ('AU','UA') : -1.1 , ('AU','UG') : -1.4 ,
('CG','AU') : -2.1 , ('CG','CG') : -3.3 , ('CG','GC') : -2.4 , ('CG','GU') : -1.4 , ('CG','UA') : -2.1 , ('CG','UG') : -2.1 ,
('GC','AU') : -2.4 , ('GC','CG') : -3.4 , ('GC','GC') : -3.3 , ('GC','GU') : -1.5 , ('GC','UA') : -2.2 , ('GC','UG') : -2.5 ,
('GU','AU') : -1.3 , ('GU','CG') : -2.5 , ('GU','GC') : -2.1 , ('GU','GU') : -0.5 , ('GU','UA') : -1.4 , ('GU','UG') :  1.3 ,
('UA','AU') : -1.3 , ('UA','CG') : -2.4 , ('UA','GC') : -2.1 , ('UA','GU') : -1.0 , ('UA','UA') : -0.9 , ('UA','UG') : -1.3 ,
('UG','AU') : -1.0 , ('UG','CG') : -1.5 , ('UG','GC') : -1.4 , ('UG','GU') :  0.3 , ('UG','UA') : -0.6 , ('UG','UG') : -0.5 }
  
#===================================================================================
# Cao Chen 09 Energy Model
#===================================================================================
def CC06(pkCC06,seq):
	CC06Result = {}
	entropy_l1, entropy_l3 = 0.0, 0.0
	for pkStem in pkCC06:
		i, j, k, l, stemlength1, stemlength2, l1, l2, l3 = pkStem
		index = i, j, k, l, stemlength1, stemlength2, l1, l2, l3 
		stem1 = i, j
		stem1_short = i, j, stemlength1
		stack_s1, stack_s2 = 0,0

		stack_s1 = wStack(stem1_short,seq)
		         
		stem2 = k, l
		stem2_short = k, l, stemlength2

		stack_s2 = wStack(stem2_short,seq)    

		l1 = k - (i + stemlength1)
		l2 = (j - stemlength1 + 1) - (k + stemlength2)            
		l3 = (l - stemlength2) - j

		# Stem length restiction
		if stemlength1 > 12:
		    stemlength1 = 12
		if stemlength2 > 12:
		    stemlength2 = 12
		    
		# Coaxial stacking
		coaxial_stacking = 0
		if l2 == 0 or l2 == 1:
		    coaxial_stacking = CoaxialStackingCalculation(seq, stemlength1, stemlength2, i, j, k, l) 
		    # Weighting parameter              
		    coaxial_stacking = 0.75 * coaxial_stacking    
		# endif

		# Calculate loop entropy for L1 dependent on stem S2     
		loop1_stem2 = l1, stemlength2    
		         
		if loop1_stem2 in loop1_dic_cc:
		    entropy_l1 = 0.62 * loop1_dic_cc[loop1_stem2] 
		else:
		    ln_w_coil = 2.14 * l1 + 0.10
		    fitting = lmin_S2[stemlength2]
		    l_min = fitting[0]
		    # print(l1 - l_min + 1, l1,l_min,stemlength2)
		    # Occurs error due to stem length==2 for pseudoknot
		    logVal = l1 - l_min + 1
		    if(logVal<1):
		    	logVal = 1;
		    ln_w = fitting[1] * math.log(logVal) + fitting[2] * (l1 - l_min + 1) + fitting[3]
		    entropy_l1 = 0.62*(ln_w_coil - ln_w)
		# endif

		# Calculate loop entropy for L3 dependent on stem S1
		loop3_stem1 = l3, stemlength1

		if loop3_stem1 in loop3_dic_cc:
		    entropy_l3 = 0.62 * loop3_dic_cc[loop3_stem1]
		else:
		    ln_w_coil = 2.14 * l3 + 0.10
		    fitting = lmin_S1[stemlength1]
		    l_min = fitting[0]
		    logVal = l3 - l_min + 1
		    if(logVal<1):
		    	logVal = 1;
		    ln_w = fitting[1] * math.log(logVal) + fitting[2] * (l3 - l_min + 1) + fitting[3]
		    entropy_l3 = 0.62*(ln_w_coil - ln_w)
		# endif

		# Calculate free energy for pseudoknot
		# We want the loop entropy to be negative, hence + instead of - of the equation
		# Updated: no, it will be -, not + because I'm checking after the calculation
		pk_energy = stack_s1 + stack_s2 - (entropy_l1 + entropy_l3 + 1.3 + coaxial_stacking)
		# standard 0.0
		if pk_energy < accEne:
		    CC06Result[index] = pk_energy #, stack_s1, stack_s2, entropy_l1, 0.0, entropy_l3, coaxial_stacking 
		# endif

	return CC06Result 
	# endfor
# end function

def wStack(stem,seq):
	stack = Turner04Handlar(stem,seq)
	return stack
# end function

def FindLength(fromList,searchBy1,searchby2):

	for stem in range(len(fromList)):
		i,j,l = fromList[stem]
		if(i==searchBy1 and j==searchby2):
			return l
		# endif
	# endfor
	# for noneType avoiding
	return 0
# end function
def CoaxialStackingCalculation(seq, stemlength1, stemlength2, i, j, k, l):

    # Example:
    
    # L2 == 0:
    # ACGGaUUGUguCCGUAAUcACA
    # (((((.[[[[)))))...]]]]
    # Stack is AU,GC = -2.10
    
    # L2 == 1:
    # ACGGaUUGUgAuCCGUAAUcACA
    # (((((.[[[[:)))))...]]]]
    # Stack is AU,GC = -2.10    
     
    pair1 = seq[((i - 1) + stemlength1 - 1)] + seq[j - stemlength1]
    pair2 = seq[((k - 1) + stemlength2 - 1)] + seq[l - stemlength2]

    stack = pair1, pair2

    if stack in stack_dic:
        coaxialStacking = stack_dic[stack]
    else:
        coaxialStacking = 0.0

    return coaxialStacking
# end function

#===================================================================================
# Cao Chen 09 Energy Model
#===================================================================================
def CC09(pk_dic_cc09, stemList):
	pk_dic_cc09_result = {}
	entropies_dic, entropies_dic_L1, entropies_dic_L3 = {}, {}, {}    

	# Store entropy parameters in dictionary in format (s1, s2, l1, l3, l2)    
	entropies = open("CaoChenParameters.txt",'r')
	for line in entropies:
		i = line.split()
		quintet = int(i[0][3:]), int(i[1][3:]), int(i[2][3:]), int(i[3][3:]), int(i[4][3:])
		entropies_dic[quintet] = float(i[5][3:])

	# For long loops L1 > 7 nt AND L3 <= 7 nt 
	# Store entropy parameters in dictionary in format (s1, s2, 'long', l3, l2)
	entropies = open("CaoChenParameters_L1.txt",'r')
	for line in entropies:
		i = line.split()
		a_b = float(i[4][7:]), float(i[5][7:])
		quintet = int(i[0][3:]), int(i[1][3:]), 'long', int(i[2][3:]), int(i[3][3:])
		entropies_dic_L1[quintet] = a_b

	# For long loops L3 > 7 nt 
	# Store entropy parameters in dictionary in format (s1, s2, l1, 'long', l2)
	entropies = open("CaoChenParameters_L3.txt",'r')
	for line in entropies:
		i = line.split()
		a_b = float(i[4][7:]), float(i[5][7:])
		quintet = int(i[0][3:]), int(i[1][3:]), int(i[2][3:]), 'long', int(i[3][3:])
		entropies_dic_L3[quintet] = a_b

	for pk_stem in pk_dic_cc09:

		i, j, k, l = pk_stem[0], pk_stem[1], pk_stem[2], pk_stem[3]

		stemlength1 = pk_stem[4]
		stack_s1 = FindLength(stemList,i,j)
		energy_s1 = 0# stemList[stem1][3]        
		    
		stemlength2 = pk_stem[5]  
		stack_s2 = FindLength(stemList,k,l)
		energy_s2 = 0# stemList[stem2][3]    
		                        
		l1 = k - (i + stemlength1)
		l2 = (j - stemlength1 + 1) - (k + stemlength2)            
		l3 = (l - stemlength2) - j

		if stemlength1 > 10:
		    stemlength1 = 10
		if stemlength2 > 10:
		    stemlength2 = 10

		# In case configuration is not defined in virtual bond model
		entropy = 0.0

		if l1 <= 7 and l3 >= 1 and l3 <= 7:     
		    quintet = stemlength1, stemlength2, l1, l3, l2
		    if quintet in entropies_dic:
		        entropy = entropies_dic[quintet]
		    
		elif l1 <= 7 and l3 > 7:                 
		    quintet = stemlength1, stemlength2, l1, 'long', l2
		    if quintet in entropies_dic_L3:
		        a_b = entropies_dic_L3[quintet]
		        entropy = a_b[0] * math.log(l3) + a_b[1]
		        
		elif l1 > 7 and l3 >= 1 and l3 <= 7:     
		    quintet = stemlength1, stemlength2, 'long', l3, l2    
		    if quintet in entropies_dic_L1:
		        a_b = entropies_dic_L1[quintet]
		        entropy = a_b[0] * math.log(l1) + a_b[1]
		        
		elif l1 > 7 and l3 > 7:                 
		    quintet = stemlength1, stemlength2, l1, 'long', l2
		    if quintet in entropies_dic_L3:
		        a_b = entropies_dic_L3[quintet]
		        entropy = a_b[0] * math.log(l3) + a_b[1]

		    
		if entropy:
		    pk_energy = stack_s1 + stack_s2 - (0.62 * entropy)
		    if pk_energy < accEne:
		        pk_dic_cc09_result[stemlength2] = pk_energy #, stack_s1, stack_s2, l1, l3, l2, 0.62 * entropy
		    else:
		    	pk_dic_cc09_result[stemlength2] = pk_energy
	return pk_dic_cc09_result #, entropies_dic, entropies_dic_L1, entropies_dic_L3
#===================================================================================
# LongPK Energy Model
#===================================================================================
def LongPK(pk_dic_longpk, stemList, INIT, PENALTY):

    pk_dic_longpk_result = {}    

    for pk_stem in pk_dic_longpk:
        stemlength1 = pk_stem[4]
        i, j, k, l = pk_stem[0], pk_stem[1], pk_stem[2], pk_stem[3]
        i, j, k, l, stemlength1, stemlength2, l1, l2, l3 = pk_stem
        index = i, j, k, l, stemlength1, stemlength2, l1, l2, l3
        stack_s1 = FindLength(stemList,i,j)
                                                    
        stemlength2 = pk_stem[5]
        stack_s2 = FindLength(stemList,k,l)    
          
        l1 = k - (i + stemlength1)
        l2 = (j - stemlength1 + 1) - (k + stemlength2) 
        l3 = (l - stemlength2) - j

        looplength = l1 + l2 + l3        
      
        entropy = PENALTY*(looplength) + INIT
        # delG = wS1 + wS2 - delTLooplength
        pk_energy = stack_s1 + stack_s2 - entropy
      
        if pk_energy < accEne:            
            pk_dic_longpk_result[index] = pk_energy #, stack_s1, stack_s2, l1, l2, l3, entropy, looplength
                
    return pk_dic_longpk_result

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
	i,j,length = basePairs
	stem = []
	for left,right in zip(range(i,i+length),range(j,j-length,-1)):
		stem.append([left,right])
	# endfor
	energy = Turner04(stem,sequence)
	return energy
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
		# print("+0.43 sym")
	# AU / GU per end penalty

	# starting side energy
	if((sequence[stem[0][0]] == 'A' and sequence[stem[0][1]] == 'U') or (sequence[stem[0][0]] == 'U' and sequence[stem[0][1]] == 'A')):
		energy += 0.45	# per AU end
		# print("+0.45 AUstart")

	elif((sequence[stem[0][0]] == 'G' and sequence[stem[0][1]] == 'U') or (sequence[stem[0][0]] == 'U' and sequence[stem[0][1]] == 'G')):
		energy += 0.45	# per GU end
		# print("+0.45 GUstart")

	# ending side energy
	if((sequence[stem[length][0]] == 'U' and sequence[stem[length][1]] == 'A') or (sequence[stem[length][0]] == 'A' and sequence[stem[length][1]] == 'U')):
		energy += 0.45	# per AU end
		# print("+0.45 AUend")
	elif((sequence[stem[length][0]] == 'U' and sequence[stem[length][1]] == 'G') or (sequence[stem[length][0]] == 'G' and sequence[stem[length][1]] == 'U')):
		energy += 0.45	# per GU end
		# print("+0.45 GUend")

	for i in range(length):
		# intermolecular initiation for AU or GC
		if(iFlag==0 and ((sequence[stem[i][0]] == 'A' and sequence[stem[i][1]] == 'U') or (sequence[stem[i][0]] == 'U' and sequence[stem[i][1]] == 'A') or (sequence[stem[i][0]] == 'G' and sequence[stem[i][1]] == 'C') or (sequence[stem[i][0]] == 'C' and sequence[stem[i][1]] == 'G'))):
			energy += 4.09	# Intermolecular initiation
			iFlag = 1		# Initiation complete
			# print("+4.09")

		# Regular energy calculation
		temp = CalculateEnergy(sequence[stem[i][0]], sequence[stem[i][1]], sequence[stem[i+1][0]], sequence[stem[i+1][1]])
		energy += temp
		# print(temp)
	# print(energy)
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
