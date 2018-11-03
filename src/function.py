class Function():

	flag = []
	flagValid = []
	mol = []

	def Merge(self,basePairs,pseudoKnot,sequenceLength):

		# Initialization

		for i in range(sequenceLength):
		    self.flag.append(0)
		    self.flagValid.append(0)
		    self.mol.append(".")

		self.mol,pseudoEnergy = Function().AddPseudoknot(pseudoKnot,self.mol)
		self.mol,helixEnergy = Function().AddBasePairs(basePairs,self.mol)
		
		totalEnergy = pseudoEnergy + helixEnergy

		file = open("raw.txt","a")
		for i in range(1,len(self.mol)):
			print(self.mol[i],end="")
			# file.write(self.mol[i])
		# file.write("\n")
		# print(pseudoEnergy,helixEnergy,totalEnergy)

		self.flag.clear()
		self.flagValid.clear()
		self.mol.clear()
	# End function

	def AddPseudoknot(self,pseudoKnot,mol):
		energy = 0
		for pStem in pseudoKnot:
			energy += pseudoKnot[pStem]
			start,end,start2,end2,length,length2,l1,l2,l3 = pStem
			for j,k in zip(range(start,start+length,1),range(end,0,-1)):
				if(self.flag[j]==0 and self.flag[k]==0):
					self.flag[j] = 1
					self.flag[k] = 1
					self.mol[j] = "["
					self.mol[k] = "]"
		    # End for j,k
			for j,k in zip(range(start2,start2+length2,1),range(end2,0,-1)):
				if(self.flag[j]==0 and self.flag[k]==0):
					self.flag[j] = 1
					self.flag[k] = 1
					self.mol[j] = "{"
					self.mol[k] = "}"
			# End for j,k
		return self.mol,energy
	# End function
	def AddBasePairs(self,infoTable,mol):
		energy = 0
		# Find for new population
		for base,en in infoTable:

			start,end,length = base
			stem = 0
			# Search inside for making bond
			for j,k in zip(range(start,start+length,1),range(end,0,-1)):
				if(self.flag[j]==0 and self.flag[k]==0):
					if(self.flag[j]==0 and self.flag[k]==0):
						self.flag[j] = 2
						self.flag[k] = 2
						self.flagValid[j] = 1 # )
						self.flagValid[k] = 2 # (
						stem+=1
		    # End for j,k

			# Can make at least 3 stems and the inside brackets are enclosed
			revoke = 0 #Take back all the actions
			if stem>=3:
				for j,k in zip(range(start,start+length,1),range(end,0,-1)):
					if(self.flag[j]==2 and self.flag[k]==2 and Function().Equal12(self.flagValid,j,k)):
						self.flag[j] = 1
						self.flag[k] = 1
						self.mol[j] = "("
						self.mol[k] = ")"
					else:
						revoke = 1
						break
				# End for j,k
				# this is temporary; actually energy should be calculated after adding the mole; like nabid
				energy += en 	# Add this energy, since the helix is added to the mole

				if(revoke==1):
				    for j,k in zip(range(start,start+length,1),range(end,0,-1)):
				        if(self.flag[j]==2 and self.flag[k]==2 and Function().Equal12(self.flagValid,j,k)):
				            self.flag[j] = 0
				            self.flag[k] = 0
				            self.flagValid[j] = 0
				            self.flagValid[k] = 0
		    # End if stem>=3

			else:
			    for j,k in zip(range(start,start+length,1),range(end,0,-1)):
			        if(self.flag[j]==2 and self.flag[k]==2 and Function().Equal12(self.flagValid,j,k)):
			            self.flag[j] = 0
			            self.flag[k] = 0
			            self.flagValid[j] = 0
			            self.flagValid[k] = 0
			# End start, end, length
		return self.mol,energy
	# End function


	def Equal12(self,flagValid,j,k):

	    one=0
	    two=0
	    if(j>k):   
	        swap(j,k)
	    for i in range(j,k+1):
	        if(flagValid[i]==1):
	            one+=1
	        elif (flagValid[i]==2):
	            two+=1
	    
	    if(one==two):
	        return True
	    else:
	        return False
	# end function

	def Performance(predicted,benchmark):
		true_basepair = 0
		a = 0
		c = 0
		false_negative_basepair = 0
		false_positive_basepair = 0
		for i in range(len(predicted)):

		    if ((predicted[i] == '(' or predicted[i] == '[' or predicted[i] == '{') and (benchmark[i] == '(' or benchmark[i] == '[' or benchmark[i] == '{')):
		    
		        true_basepair+=1
		    
		    if ((predicted[i] != '(' and predicted[i] != '[' and predicted[i] != '{') and (benchmark[i] == '(' or benchmark[i] == '[' or benchmark[i] == '{')):
		    
		        false_negative_basepair+=1
		    
		    if ((predicted[i]=='(' or predicted[i]=='[' or predicted[i]=='{') and (benchmark[i] !='(' and benchmark[i] !='[' and benchmark[i] !='{')):
		    
		        false_positive_basepair+=1
		    # endif

		    # CLosing check
		    # if ((predicted[i] == ')' or predicted[i] == ']' or predicted[i] == '}') and (benchmark[i] == ')' or benchmark[i] == ']' or benchmark[i] == '}')):
		    
		    #     true_basepair+=1
		    
		    # if ((predicted[i] != ')' and predicted[i] != ']' and predicted[i] != '}') and (benchmark[i] == ')' or benchmark[i] == ']' or benchmark[i] == '}')):
		    
		    #     false_negative_basepair+=1
		    
		    # if ((predicted[i]==')' or predicted[i]==']' or predicted[i]=='}') and (benchmark[i] !=')' and benchmark[i] !=']' and benchmark[i] !='}')):
		    
		    #     false_positive_basepair+=1
		    # endif
		# endfor

		# Avoid null
		sensitivity = 0
		specificity = 0
		f_measure = 0

		# Avoid zero division 
		if(true_basepair>0):
			sensitivity =( true_basepair/ (true_basepair + false_negative_basepair))*100.0
			specificity =( true_basepair / (true_basepair + false_positive_basepair))*100.0
			a, c
			a = sensitivity * specificity * 2
			c = sensitivity + specificity
			f_measure = a / c
		# endif

		return sensitivity,specificity,f_measure,true_basepair,false_positive_basepair,false_negative_basepair
    #End