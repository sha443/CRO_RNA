def CC06(pkCC06):
	CC06Result = []
	entropy_l1, entropy_l3 = 0.0, 0.0
	for pkStem in pkCC06:
		i, j, k, l, stemlength1, stemlength2, l1, l2, l3 = pkStem
		stem1 = i, j
		stem1_short = i, j, stemlength1

		stack_s1 = get_values(stem1, stem1_short, stems_shortened_dic, stem_dic)
		         
		stem2 = k, l
		stem2_short = k, l, stemlength2

		stack_s2 = get_values(stem2, stem2_short, stems_shortened_dic, stem_dic)    

		l1 = k - (i + stemlength1)
		l2 = (j - stemlength1 + 1) - (k + stemlength2)            
		l3 = (l - stemlength2) - j

		if stemlength1 > 12:
		    stemlength1 = 12
		if stemlength2 > 12:
		    stemlength2 = 12
		    
		# Coaxial stacking
		if l2 == 0 or l2 == 1:
		    coaxial_stacking = cs_calculation(seq, stemlength1, stemlength2, i, j, k, l) 
		    # Weighting parameter              
		    coaxial_stacking = 0.75 * coaxial_stacking    

		# Calculate loop entropy for L1 dependent on stem S2     
		loop1_stem2 = l1, stemlength2    
		         
		if loop1_stem2 in loop1_dic_cc:
		    entropy_l1 = 0.62 * loop1_dic_cc[loop1_stem2] 
		else:
		    ln_w_coil = 2.14 * l1 + 0.10
		    fitting = lmin_S2[stemlength2]
		    l_min = fitting[0]
		    ln_w = fitting[1] * math.log(l1 - l_min + 1) + fitting[2] * (l1 - l_min + 1) + fitting[3]
		    entropy_l1 = 0.62*(ln_w_coil - ln_w)

		# Calculate loop entropy for L3 dependent on stem S1
		loop3_stem1 = l3, stemlength1

		if loop3_stem1 in loop3_dic_cc:
		    entropy_l3 = 0.62 * loop3_dic_cc[loop3_stem1]
		else:
		    ln_w_coil = 2.14 * l3 + 0.10
		    fitting = lmin_S1[stemlength1]
		    l_min = fitting[0]
		    ln_w = fitting[1] * math.log(l3 - l_min + 1) + fitting[2] * (l3 - l_min + 1) + fitting[3]
		    entropy_l3 = 0.62*(ln_w_coil - ln_w)

		# Calculate free energy for pseudoknot
		pk_energy = stack_s1 + stack_s2 + entropy_l1 + entropy_l3 + 1.3 + coaxial_stacking

		if pk_energy < 0.0:
		    CC06Result[pk_stem] = pk_energy, stack_s1, stack_s2, entropy_l1, 0.0, entropy_l3, coaxial_stacking              
		    return CC06Result  