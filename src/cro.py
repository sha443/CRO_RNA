import random
from operators import Operators
from molecule import Molecule
import pseudoknot as pk
import population
import energy
from function import Function as func
import tictoc
class CRO():

	# Variables
	structureFound = ""
	sensitivity = 0
	specificity = 0
	f_measure = 0
	true_basepair = 0
	false_negative_basepair = 0
	false_positive_basepair = 0

	# CRO parameters
	popSize = 0
	KELossRate = 0
	MoleColl = 0
	InitialKE = 0
	buffer = 0
	alpha = 0
	beta = 0
	sequence = ''
	mole = None


	######################################################################
	# CRO Init
	######################################################################
	# def Init(self,popSize, KELossRate, MoleColl, InitialKE, alpha, beta, buffer, sequence, mole):
	# 	self.popSize = popSize
	# 	self.KELossRate = KELossRate
	# 	self.MoleColl = MoleColl
	# 	self.InitialKE = InitialKE
	# 	self.alpha = alpha
	# 	self.beta = beta
	# 	self.self.buffer = self.buffer
	# 	self.sequence = sequence
	# 	self.mole = mole
	# # end function

	######################################################################
	# OnWall Ineffective Colision handler
	######################################################################
	def OnwallIneffectiveCollision(self,mole,oldMol, index):
		operator = Operators()
		newMol = operator.OnWall(oldMol)
		PEnew = CRO().CalculatePE(mole,newMol)
		KEnew = 0.0
		mole.numHit[index] = mole.numHit[index] + 1
		t = mole.PE1[index] + mole.KE1[index]
		if (t>=PEnew):
			a = (random.uniform(0,1) * (1-self.KELossRate))+self.KELossRate
			KEnew = (mole.PE1[index] - PEnew + mole.KE1[index])*a
			mole.moleculeTable[index] = newMol
			mole.PE1[index] = PEnew
			mole.KE1[index] = KEnew
			if(mole.PE1[index]<mole.minPE[index]):
				mole.minStruct[index] = mole
				mole.minPE[index] = mole.PE1[index]
				mole.minHit[index] = mole.numHit[index]
			#endif
		#endif
	#end function

	######################################################################
	# Decomposition handler
	######################################################################
	def Decomposition(self,mole,oldMol,index):
		operator = Operators()
		newMol1, newMol2 = operator.Decomposition(oldMol)
		pe1 = CRO().CalculatePE(mole,newMol1)
		pe2 = CRO().CalculatePE(mole,newMol2)

		e_dec = 0
		gamma1 = 0
		gamma2 = 0
		gamma3 = 0
		gamma1 = random.uniform(0,1)
		gamma2 = random.uniform(0,1)

		if ((mole.PE1[index] + mole.KE1[index]) >= (pe1+pe2)):
			e_dec = (mole.PE1[index] + mole.KE1[index]) - (pe1 + pe2)
		else:
		   e_dec = (mole.PE1[index] + mole.KE1[index]) + gamma1 * gamma2 * self.buffer - (pe1 + pe2)
		# endif

		if (e_dec>=0):
		   self.buffer = self.buffer * (1 -( gamma1*gamma2))
		   gamma3 = random.uniform(0,1)

		   mole.moleculeTable[index] = newMol1
		   mole.PE1[index] = pe1
		   mole.KE1[index] = e_dec * gamma3
		   mole.numHit[index] = 0
		   mole.minHit[index] = 0
		   mole.minStruct[index] = newMol1
		   mole.minPE[index] = pe1

		   mole.moleculeTable.append(newMol1)
		   mole.PE1.append(pe1)
		   mole.KE1.append(e_dec * gamma3)
		   mole.numHit.append(0)
		   mole.minHit.append(0)
		   mole.minStruct.append(newMol1)
		   mole.minPE.append(pe1)

		else:
		   mole.numHit[index] = mole.numHit[index] + 1
		# endif
	# end function

	######################################################################
	# IntermolecularIneffectiveCollision handler
	######################################################################
	def IntermolecularIneffectiveCollision(self,mole,oldMol1,oldMol2,index1,index2):
		operator = Operators()
		newMol1, newMol2 = operator.Intermolecular(oldMol1, oldMol2)
		pe1 = CRO().CalculatePE(mole,newMol1)
		pe2 = CRO().CalculatePE(mole,newMol2)
		
		e_inter = 0
		gamma4 = random.uniform(0,1)

		mole.numHit[index1] = mole.numHit[index1] + 1
		mole.numHit[index2] = mole.numHit[index2] + 1
		e_inter = (mole.PE1[index1] + mole.PE1[index2] + mole.KE1[index1] + mole.KE1[index2]) - (pe1 + pe2)
		if (e_inter>=0):
			mole.moleculeTable[index1] = newMol1
			mole.moleculeTable[index2] = newMol2
			mole.PE1[index1] = pe1
			mole.PE1[index2] = pe2
			mole.KE1[index1] = e_inter * gamma4
			mole.KE1[index2] = e_inter * (1 - gamma4)

			if (mole.PE1[index1]<mole.minPE[index1]):
				mole.minStruct[index1] = mole.moleculeTable[index1]
				mole.minPE[index1] = mole.PE1[index1]
				mole.minHit[index1] = mole.numHit[index1]
			# endif

			if (mole.PE1[index2]<mole.minPE[index2]):
				mole.minStruct[index2] = mole.moleculeTable[index2]
				mole.minPE[index2] = mole.PE1[index2]
				mole.minHit[index2] = mole.numHit[index2]
			# endif
		# endif
	# end function

	def Synthesis (self,mole,oldMol1,oldMol2,index1,index2):
		operator = Operators()
		newMol = operator.Synthesis(oldMol1, oldMol2)
		pe_new = CRO().CalculatePE(mole,newMol)

		if((mole.PE1[index1]+mole.PE1[index2] + mole.KE1[index1]+mole.KE1[index2])>=pe_new):
			
			ke_new = (mole.PE1[index1] + mole.PE1[index2] + mole.KE1[index1] + mole.KE1[index2]) - pe_new

			del mole.moleculeTable[index1]
			del mole.PE1[index1]
			del mole.KE1[index1]
			del mole.numHit[index1]
			del mole.minHit[index1]
			del mole.minStruct[index1]
			del mole.minPE[index1]

			if(index2>=index1):
				# position of index2 is decreased by 1
				index2 = index2 -1

			del mole.moleculeTable[index2]
			del mole.PE1[index2]
			del mole.KE1[index2]
			del mole.numHit[index2]
			del mole.minHit[index2]
			del mole.minStruct[index2]
			del mole.minPE[index2]

			mole.moleculeTable.append(newMol)
			mole.PE1.append(pe_new)
			mole.KE1.append(ke_new)
			mole.numHit.append(0)
			mole.minHit.append(0)
			mole.minStruct.append(newMol)
			mole.minPE.append(pe_new)
		else:
			mole.numHit[index1] = mole.numHit[index1] + 1
			mole.numHit[index1] = mole.numHit[index1] + 1
		# endif
	# end function

	######################################################################
	# Main CRO handler
	######################################################################
	def CRO(self,popSize, KELossRate, MoleColl, InitialKE, alpha, beta, buffer, sequence, mole,iteration, path,fileName):
		b = 0
		i = 0
		w = None
		oldMol1 = None
		oldMol2 = None
		index, index1, index2 = 0,0,0
		minEnrg = 1000
		sl=0

		for j in range(len(mole.PE)):
			if (mole.PE1[j] < minEnrg):
				minEnrg = mole.PE1[j]
				sl = j+1
			#endif
		#endfor

		# Save Initials
		# energyBefore = open(path+"output/initial_population_"+fileName,"a")
		# energyBefore.write("Minimum energy: "+str(minEnrg))
		# energyBefore.write(" at position: "+str(sl))
		# energyBefore.write("\n======================================================\n")

		# Oprators hit counter
		on = 0
		dec = 0
		inef = 0
		syn = 0

		# Main iteration starts
		for i in range(iteration):

			b = random.uniform(0,1)
			# Decomposition or OnwallIneffectiveCollision
			if (b>MoleColl):
				index = random.randint(0, len(mole.KE1)-1)
				# print(index)
				if ((mole.numHit[index]-mole.minHit[index])>alpha):
					dec+=1
					CRO().Decomposition(mole,mole.moleculeTable[index], index)
				#endif
				else:
					on+=1
					CRO().OnwallIneffectiveCollision(mole,mole.moleculeTable[index], index)
				#end else
			#endif

			# Synthesis or IntermolecularIneffectiveCollision
			else:
				index1 = random.randint(0, len(mole.KE1)-1)
				index2 = random.randint(0, len(mole.KE1)-1)
				# print(index1,index2)
				if ((mole.KE1[index1]+mole.KE1[index2])<beta):
					syn+=1
					CRO().Synthesis(mole,mole.moleculeTable[index1], mole.moleculeTable[index2], index1, index2)
				#endif
				else:
					inef+=1
					CRO().IntermolecularIneffectiveCollision(mole, mole.moleculeTable[index1], mole.moleculeTable[index2], index1, index2)
				#endelse
			#end else
		# Endfor iteration

		# End timer
		tm = tictoc.toc()
		
		# Finding minimum energy
		minEnrg = 1000
		mole.PE1 = mole.PE1
		minEnrgIndex = None


		for j in range(len(mole.PE)):
			if (mole.PE1[j]<minEnrg):
				minEnrg = mole.PE1[j]
				minEnrgIndex = j
			#endif
		#endfor
		hits = "Onwall= "+str(on) +"\tDec = "+str(dec)+"\tSyn = "+str(syn)+"\tIntermolecular = "+str(inef)+"\n"
		sen,sp,f_m,tp,fp,fn,structureFound,totalEnergy = CRO().FindMinimumStructure(mole,minEnrg,minEnrgIndex,path,fileName,sequence)

		# Save information 
		energyAfter = open(path+"output/final_population_"+fileName,"a")

		energyAfter.write("\n======================================================\n")
		energyAfter.write(hits)
		outputString = "sen=%.2f \tsp=%.2f \tf_measure=%.2f \ttp=%d \tfp=%d \tfn=%d \n" %(sen,sp,f_m,tp,fp,fn)
		energyAfter.write(outputString)
		strucreNenergy = structureFound+"\t%.2f" % (totalEnergy)
		energyAfter.write(strucreNenergy)
		energyAfter.write("\n"+tm)
		
		# Log:
		print("[sen,sp,f-measure]")
		print([sen,sp,f_m])
		print([structureFound,totalEnergy])

		return sen,sp,f_m,tp,fp,fn

	#end function

	def FindMinimumStructure(self,mole,minEnrg,minEnrgIndex,path,fileName,sequence):		
		flag = []
		mol = []
		flagValid = []
		infoEnergy = []
		moleculeSequence = []
		scElements = []
		pkElements = []
		# Initialization
		for i in range(len(mole.sequence)):
			flag.append(0)
			mol.append(".")
			flagValid.append(0)
		# endfor

		tempInfo = []
		# Retrive info and sort according to the length
		for i in mole.moleculeTable[minEnrgIndex]:
			tempInfo.append(mole.infoTable[i])
		# endfor
		# sort
		tempInfo = sorted(tempInfo, key=lambda x: x[2],reverse=True)
		# print(tempInfo)

		# Construction of secondary structure
		for base in tempInfo:
			start,end,length = base

			# Search inside for making bond
			for j,k in zip(range(start,start+length,1),range(end,0,-1)):
				if(flag[j]==0 and flag[k]==0):
					flag[j] = 2
					flag[k] = 2
					flagValid[j] = 1 # (
					flagValid[k] = 2 # )
				# endif
			# End for j,k

			# Search for 3 or more bp
			startPair = None
			endPair = None

			for j,k in zip(range(start,start+length,1),range(end,0,-1)):
				# Check if first valid bond is found
				stem = 0
				short = 0

				if(flag[j]==2 and flag[k]==2 and CRO().Equal12(flagValid,j,k)):
					startPair = (j,k)
					while(flag[j]==2 and flag[k]==2 and CRO().Equal12(flagValid,j,k) and j<=k):
						stem+=1
						j+=1
						k-=1
						# May not needed
						endPair = (j,k)
					# endwhile

					# Revoke if not found enough stems
					# Or like this :-P   ...((()))..
                    # Leave out kissing hairpin loop
					f,t = startPair
					khp = ((t-stem+1) - (f+stem))
					if(stem<3 and stem>0 or (khp==0 and stem<4)):
						f,t = startPair
						for x,y in zip(range(f,f+stem,1),range(t,t-stem,-1)):
							flag[x] = 0
							flag[y] = 0
							flagValid[x] = 0
							flagValid[y] = 0
						# endfor

					# Else add to mol and info
					else:
						f,t = startPair
						# Leave khp first then bond
						if(khp==0):
							stem-= 1
                        # endif

						scElements.append([f,t,stem]) # start,end,length
						for x,y in zip(range(f,f+stem,1),range(t,0,-1)):
							flag[x] = 1
							flag[y] = 1
							mol[x] = "("
							mol[y] = ")"
							infoEnergy.append((x,y))  # start, end
						# endfor

					# endif stem

				# endif
			# Endfor j,k
		# Endfor basepair = start, end, length
		# print(scElements)
		# print(population.PrintableMolecule(mol))
		# print(scElements)
		# Finding pseudoknot
		mol2 = mol[:]  # make a duplicate of molecule
		for i,j,len1 in tempInfo:
			for base in tempInfo:
				k,l,len2 = base

				if(i<k and k<j and j<l):   # condiiton for H-type Pseudoknot

					# Pseudoknot info
					# Loop lenght calculation for energy evaluation
					l1 = k - (i + len1)
					l2 = (j - len1 + 1) - (k + len2)
					l3 = (l - len2) - j
					if(pk.LoopsFulfill(l1, l2, l3)):

						# Search inside for making pk
						for u,v in zip(range(k,k+len2,1),range(l,0,-1)):
							if(flag[u]==0 and flag[v]==0):
								flag[u] = 2
								flag[v] = 2
								flagValid[u] = 3 # [
								flagValid[v] = 4 # ]
							# endif
						# endfor

						# Search for 2 or more bp for making pk
						startPk = None
						endPk = None

						for u,v in zip(range(k,k+len2,1),range(l,0,-1)):
							# Checy if first valid bond is found
							stem = 0
							if(flag[u]==2 and flag[v]==2 and CRO().Equal34(flagValid,u,v)):
								startPair = (u,v)
								uu = u
								vv = v
								while(flag[u]==2 and flag[v]==2 and CRO().Equal34(flagValid,u,v) and u<=v):

									# Check if it is still valid counting the future stem
									l1 = uu - (i + len1)
									l2 = (j - len1 + 1) - (uu + stem+1)
									l3 = (vv - stem-1) - j
									stillValid = pk.LoopsFulfill(l1, l2, l3)
									if(stillValid):
										stem+=1
										u+=1
										v-=1
										# May not needed
										endPair = (u,v)
									else:
										break
								# endwhile


								# Revoke if not found enough stems (at least 2)
								if(stem<2 and stem>0): # or (not stillValid)
									f,t = startPair
									for x,y in zip(range(f,f+stem,1),range(t,t-stem,-1)):
										flag[x] = 0
										flag[y] = 0
										flagValid[x] = 0
										flagValid[y] = 0
									# endfor

								# add to mol and info
								elif(stillValid):
									f,t = startPair
									# print(i,j,f,t,len1,stem,l1,l2,l3)
									pkElements.append([i,j,f,t,len1,stem,l1,l2,l3])
									scElements.append([j,k,stem])
									for x,y in zip(range(f,f+stem,1),range(t,0,-1)):
										flag[x] = 1
										flag[y] = 1
										mol2[x] = "["
										mol2[y] = "]"

										# Must be removed later
										infoEnergy.append((x,y))
									# endfor
								# endif stem

							# endif
						# Endfor x,y
					else:
						marker =0 #, l1, l2, l3,len1,len2= pk.Overlap(l1, l2, l3, len1, len2)
						if(marker):
						# Resolvable overlap
							# print(l1,l2,l3,"pk-OL",len1,len2)
							pass

				# end pseudo condition
			# end for k,l, l2
		# end for i,j,l1
		# Energy evaluation
		turnerEnergy = 0
		for stem in scElements:
			turnerEnergy+= energy.Turner04Handlar(stem,sequence)
		# endfor

        # Pseudoknot energy
		pkEnergy = 0
		if(pkElements):
			pkEnergy = pk.PseudoknotHandler(scElements,pkElements,sequence)
            # print(pkEnergy)

		totalEnergy = turnerEnergy+pkEnergy

		self.structureFound = population.PrintableMolecule(mol2)
		# print(self.structureFound,"\t",totalEnergy)
		benchmark = open(path+"benchmark/"+fileName,"r").read()

		sen,sp,f_m,tp,fp,fn = func.Performance(self.structureFound,benchmark)
		return sen,sp,f_m,tp,fp,fn,self.structureFound,totalEnergy

		
	# end function
	def IsPair(c1,c2):
		if((c1=="A" and c2=="U") or (c1=="U" and c2=="A")):
			return 1
		elif ((c1=="G" and c2=="C") or (c1=="C" and  c2=="G")):
			return 1
		elif ((c1=="G" and c2=="U") or (c1=="U" and c2=="G")):
			return 1
		else:
			return 0
	#end function
	def Checkerboard(self,sequence):
		board = []
		for i in range(len(sequence)-1):
			board.append([])
			for j in range(0,len(sequence)-1):
				if(j<i):
					if(IsPair(sequence[i],sequence[j])):
						board[i].append(1)
					else:
						board[i].append(0)
				else:
					board[i].append(0)
		return board
	#End function

	def FindDiagonal(self,size,dotplot):
		info = []
		infoTable = []
		for i in range(size-1,0,-1):
			for j in range(size-2):
				if(dotplot[i][j]==1 and dotplot[i-1][j+1]==1):
					count=0
					k=0
					while True:
						if (dotplot[i-k][j+k] == 1):
							count+=1
							dotplot[i - k][j + k] = 2
						else:
							break
						k = k+1
					if(count>2):
						info.append((j,i,count))  # start, end, length

		# sort info table
		infoTable = sorted(info, key=lambda x: x[2],reverse=True)
		return infoTable
	#End function

	def CalculatePE(self,mole,w):
		infoTable = []
		sequence = mole.sequence[:]
		size = len(sequence)

		# Declaration of Variables
		flag = []
		flagValid = []
		infoEnergy = []
		mol = []
		scElements = []
		pkElements = []

		# Initialization
		for i in range(size):
			flag.append(0)
			flagValid.append(0)
			mol.append(".")


		# Retrive infotale using w
		for i in w:
			infoTable.append(mole.infoTable[i])

		# Adding paranthesis
		pair = 0
		pairIndex=0
		stempoolIndex =0
		stem = 0

		# infoTable = mole.infoTable[:]
		# Find for new population
		index = 0
		for base in infoTable:
			start,end,length = base

			# Search inside for making bond
			for j,k in zip(range(start,start+length,1),range(end,0,-1)):
				if(flag[j]==0 and flag[k]==0):
					flag[j] = 2
					flag[k] = 2
					flagValid[j] = 1 # (
					flagValid[k] = 2 # )
				# endif
			# End for j,k

			# Search for 3 or more bp
			startPair = None
			endPair = None

			for j,k in zip(range(start,start+length,1),range(end,0,-1)):
				# Check if first valid bond is found
				stem = 0
				short = 0

				if(flag[j]==2 and flag[k]==2 and CRO().Equal12(flagValid,j,k)):
					startPair = (j,k)
					while(flag[j]==2 and flag[k]==2 and CRO().Equal12(flagValid,j,k) and j<=k):
						stem+=1
						j+=1
						k-=1
						# May not needed
						endPair = (j,k)
					# endwhile

					# Revoke if not found enough stems
					if(stem<3 and stem>0):
						f,t = startPair
						for x,y in zip(range(f,f+stem,1),range(t,t-stem,-1)):
							flag[x] = 0
							flag[y] = 0
							flagValid[x] = 0
							flagValid[y] = 0
						# endfor

					# Else add to mol and info
					else:
						f,t = startPair
						scElements.append([f,t,stem]) # start,end,length
						for x,y in zip(range(f,f+stem,1),range(t,0,-1)):
							flag[x] = 1
							flag[y] = 1
							mol[x] = "("
							mol[y] = ")"
							infoEnergy.append((x,y))  # start, end
						# endfor

					# endif stem

				# endif
			# Endfor j,k
		# Endfor basepair = start, end, length

		# print(PrintableMolecule(mol))
		# print(scElements)
		# Finding pseudoknot
		mol2 = mol[:]  # make a duplicate of molecule
		for i,j,len1 in scElements:
			for k,l,len2 in infoTable:
				if(i<k and k<j and j<l):   # condiiton for H-type Pseudoknot
					# Pseudoknot info
					# Loop lenght calculation for energy evaluation
					l1 = k - (i + len1)
					l2 = (j - len1 + 1) - (k + len2)
					l3 = (l - len2) - j
					if(pk.LoopsFulfill(l1, l2, l3)):
						# print(j,k,len2,"pk")

						# Search inside for making pk
						for u,v in zip(range(k,k+len2,1),range(l,0,-1)):
							if(flag[u]==0 and flag[v]==0):
								flag[u] = 2
								flag[v] = 2
								flagValid[u] = 3 # [
								flagValid[v] = 4 # ]
							# endif
						# endfor

						# Search for 2 or more bp for making pk
						startPk = None
						endPk = None

						for u,v in zip(range(k,k+len2,1),range(l,0,-1)):
							# Checy if first valid bond is found
							stem = 0
							if(flag[u]==2 and flag[v]==2 and CRO().Equal34(flagValid,u,v)):
								startPair = (u,v)
								uu = u
								vv = v
								while(flag[u]==2 and flag[v]==2 and CRO().Equal34(flagValid,u,v) and u<=v):

									# Check if it is still valid counting the future stem
									l1 = uu - (i + len1)
									l2 = (j - len1 + 1) - (uu + stem+1)
									l3 = (vv - stem-1) - j
									stillValid = pk.LoopsFulfill(l1, l2, l3)
									if(stillValid):
										stem+=1
										u+=1
										v-=1
										# May not needed
										endPair = (u,v)
									else:
										break
								# endwhile


								# Revoke if not found enough stems (at least 2)
								if(stem<2 and stem>0): # or (not stillValid)
									f,t = startPair
									for x,y in zip(range(f,f+stem,1),range(t,t-stem,-1)):
										flag[x] = 0
										flag[y] = 0
										flagValid[x] = 0
										flagValid[y] = 0
									# endfor

								# add to mol and info
								elif(stillValid):
									f,t = startPair
									# print(i,j,f,t,len1,stem,l1,l2,l3)
									pkElements.append([i,j,f,t,len1,stem,l1,l2,l3])
									scElements.append([f,t,stem])
									for x,y in zip(range(f,f+stem,1),range(t,0,-1)):
										flag[x] = 1
										flag[y] = 1
										mol2[x] = "["
										mol2[y] = "]"

										# Must be removed later
										infoEnergy.append((x,y))
									# endfor
								# endif stem

							# endif
						# Endfor x,y
					else:
						marker =0 #, l1, l2, l3,len1,len2= pk.Overlap(l1, l2, l3, len1, len2)
						if(marker):
						# Resolvable overlap
							# print(l1,l2,l3,"pk-OL",len1,len2)
							pass

				# end pseudo condition
			# end for k,l, l2
		# end for i,j,l1

		# print(PrintableMolecule(mol2))

		# Energy evaluation

		turnerEnergy = 0
		for stem in scElements:
		    turnerEnergy+= energy.Turner04Handlar(stem,sequence)
        # endfor

        # Pseudoknot energy
		pkEnergy = pk.PseudoknotHandler(scElements,pkElements,sequence)
	
		return turnerEnergy

	def Equal12(self,flagValid,j,k):
		one=0
		two=0
		if(j>k):   
			#swap(j,k)
			t = j
			j = k
			k = t

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

	def Equal34(self,flagValid,j,k):
		three=0
		four=0
		if(j>k):   
			#swap(j,k)
			t = j
			j = k
			k = t

		for i in range(j,k+1):
			if(flagValid[i]==3):
				three+=1
			elif (flagValid[i]==4):
				four+=1

		if(three==four):
			return True
		else:
			return False
	# end function
	def CalculateEnergy(self,p1,p2,p3,p4):
		ene = 0
		if ((p1 == 'a' and p2 == 'u' and p3 == 'a' and p4 == 'u') or (p1 == 'u' and p2 == 'a' and p3 == 'u' and p4 == 'a')):
			ene = -.93
			return ene

		if ((p1 == 'a' and p2 == 'u' and p3 == 'u' and p4 == 'a')):

			ene = -1.10
			return ene

		if ((p1 == 'a' and p2 == 'u' and p3 == 'g' and p4 == 'u') or (p1 == 'u' and p2 == 'g' and p3 == 'u' and p4 == 'a')):

			ene = -.55
			return ene

		if ((p1 == 'a' and p2 == 'u' and p3 == 'u' and p4 == 'g') or (p1 == 'g' and p2 == 'u' and p3 == 'u' and p4 == 'a')):

			ene = -1.36
			return ene

		if ((p1 == 'a' and p2 == 'u' and p3 == 'g' and p4 == 'c') or (p1 == 'c' and p2 == 'g' and p3 == 'u' and p4 == 'a')):

			ene = -2.08
			return ene

		if ((p1 == 'a' and p2 == 'u' and p3 == 'c' and p4 == 'g') or (p1 == 'g' and p2 == 'c' and p3 == 'u' and p4 == 'a')):

			ene = -2.24
			return ene

		if ((p1 == 'u' and p2 == 'a' and p3 == 'a' and p4 == 'u')):

			ene = -1.33
			return ene

		if ((p1 == 'u' and p2 == 'a' and p3 == 'g' and p4 == 'u') or (p1 == 'u' and p2 == 'g' and p3 == 'a' and p4 == 'u')):

			ene = -1.0
			return ene

		if ((p1 == 'u' and p2 == 'a' and p3 == 'u' and p4 == 'g') or (p1 == 'g' and p2 == 'u' and p3 == 'a' and p4 == 'u')):

			ene = -1.27
			return ene

		if ((p1 == 'u' and p2 == 'a' and p3 == 'c' and p4 == 'g') or (p1 == 'g' and p2 == 'c' and p3 == 'a' and p4 == 'u')):

			ene = -2.35
			return ene

		if ((p1 == 'a' and p2 == 'u' and p3 == 'a' and p4 == 'u') or (p1 == 'u' and p2 == 's' and p3 == 'u' and p4 == 's')):

			ene = -.93
			return ene

		if ((p1 == 'u' and p2 == 'a' and p3 == 'g' and p4 == 'c') or (p1 == 'c' and p2 == 'g' and p3 == 'a' and p4 == 'u') or (p1 == 'g' and p2 == 'u' and p3 == 'g' and p4 == 'c') or (p1 == 'c' and p2 == 'g' and p3 == 'u' and p4 == 'g')):

			ene = -2.11
			return ene

		if ((p1 == 'g' and p2 == 'u' and p3 == 'c' and p4 == 'g') or (p1 == 'g' and p2 == 'c' and p3 == 'u' and p4 == 'g')):

			ene = -2.51
			return ene

		if ((p1 == 'g' and p2 == 'u' and p3 == 'g' and p4 == 'u') or (p1 == 'u' and p2 == 'g' and p3 == 'u' and p4 == 'g')):

			ene = -.5
			return ene

		if ((p1 == 'g' and p2 == 'u' and p3 == 'u' and p4 == 'g')):

			ene = +1.29
			return ene

		if ((p1 == 'u' and p2 == 'g' and p3 == 'g' and p4 == 'c') or (p1 == 'c' and p2 == 'g' and p3 == 'g' and p4 == 'u')):

			ene = -1.41
			return ene

		if ((p1 == 'u' and p2 == 'g' and p3 == 'c' and p4 == 'g') or (p1 == 'g' and p2 == 'c' and p3 == 'g' and p4 == 'u')):

			ene = -1.53
			return ene

		if ((p1 == 'u' and p2 == 'g' and p3 == 'g' and p4 == 'u')):

			ene = +.3
			return ene

		if ((p1 == 'c' and p2 == 'g' and p3 == 'g' and p4 == 'c')):

			ene = -2.36
			return ene

		if ((p1 == 'g' and p2 == 'c' and p3 == 'c' and p4 == 'g')):

			ene = -3.42
			return ene

		if ((p1 == 'g' and p2 == 'c' and p3 == 'g' and p4 == 'c') or (p1 == 'c' and p2 == 'g' and p3 == 'c' and p4 == 'g')):

			ene = -3.26
			return ene

		return ene
	#End

	
# End class