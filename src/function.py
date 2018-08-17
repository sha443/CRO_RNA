class Function():

	flag = []
	flagValid = []
	makePair = []
	infoEnergy = []
	mol = []

	def Merge(self,basePairs,pseudoKnot,sequenceLength):
		# Initialization
		for i in range(sequenceLength):
		    self.flag.append(0)
		    self.flagValid.append(0)
		    self.mol.append(".")

		self.mol = Function().AddPseudoknot(pseudoKnot,self.mol)
		self.mol = Function().AddBasePairs(basePairs,self.mol)
		

		for i in range(1,len(self.mol)):
			print(self.mol[i],end="")
	# End function

	def AddPseudoknot(self,pseudoKnot,mol):
		for pStem in pseudoKnot:
			start,end,start1,start2,length,length2,l1,l2,l3 = pStem
			for j,k in zip(range(start,start+length,1),range(end,0,-1)):
				if(self.flag[j]==0 and self.flag[k]==0):
					self.flag[j] = 1
					self.flag[k] = 1
					self.mol[j] = "["
					self.mol[k] = "]"
		    # End for j,k
		return self.mol
	# End function
	def AddBasePairs(self,infoTable,mol):
		stem = 0
		# Find for new population
		for base in infoTable:
			start,end,length = base
			# Search inside for making bond
			for j,k in zip(range(start,start+length,1),range(end,0,-1)):
				if(self.flag[j]==0 and self.flag[k]==0):
					self.flag[j] = 1
					self.flag[k] = 1
					self.mol[j] = "("
					self.mol[k] = ")"
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
						self.infoEnergy.append((j,k))  # start, end
						self.makePair.append((j,k))
					else:
						revoke = 1
						break
					# End for j,k

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
			        if(self.flag[j]==2 and self.flag[k]==2 and Equal12(self.flagValid,j,k)):
			            self.flag[j] = 0
			            self.flag[k] = 0
			            self.flagValid[j] = 0
			            self.flagValid[k] = 0
			# End start, end, length
		return self.mol
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
