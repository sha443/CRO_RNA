import random
from operators import Operators
from molecule import Molecule
class CRO():

	# Variables
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
	mol = None

	######################################################################
	# CRO Init
	######################################################################
	def Init(self,popSize, KELossRate, MoleColl, InitialKE, alpha, beta, buffer, sequence, molecule):
		self.popSize = popSize
		self.KELossRate = KELossRate
		self.MoleColl = MoleColl
		self.InitialKE = InitialKE
		self.alpha = alpha
		self.beta = beta
		self.buffer = buffer
		self.sequence = sequence
		self.mol = molecule

	######################################################################
	# OnWall Ineffective Colision handler
	######################################################################
	def OnwallIneffectiveCollision(self,oldMol, index):
		operator = Operators()
		newMol = operator.OnWall(oldMol)
		PEnew = CRO().CalculatePE(newMol)
		KEnew = 0.0
		mol.numHit[index] = mol.numHit[index] + 1
		t = mol.PE1[index] + mol.KE1[index]
		if (t>=PEnew):
			a = (random.uniform(0,1) * (1-KELossRate))+KELossRate
			KEnew = (mol.PE1[index] - PEnew + mol.KE1[index])*a
			mol.Molecule_list[index] = newMol
			mol.PE1[index] = PEnew
			mol.KE1[index] = KEnew
			if(mol.PE1[index]<mol.minPE[index]):
			    mol.minStruct[index] = mol
			    mol.minPE[index] = mol.PE1[index]
			    mol.minHit[index] = mol.numHit[index]
			#endif
		#endif
	#end

	######################################################################
	# Main CRO handler
	######################################################################
	def CRO(self,popSize, KELossRate, MoleColl, InitialKE, alpha, beta, buffer, sequence, mol,iteration,fileName):
		b = 0
		i = 0
		w = None
		w1 = None
		w2 = None
		index, index1, index2 = None,None,None
		minEnrg = 1000
		tt=0

		for j in range(len(mol.PE)):
		    if (mol.PE1[j] < minEnrg):
		        minEnrg = mol.PE1[j]
		        tt = j
		    #endif
		#endfor
		energyBefore = open("..\data\energy_before_"+fileName+".txt","w+")
		energyBefore.write(str(minEnrg))
		energyBefore.write(str(tt))

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
				index = random.randint(0, len(mol.PE1)-1)

				if ((mol.numHit[index]-mol.minHit[index])>alpha):
					++dec
					#Decomposition(mol.moleculeTable[index], index)
	            #endif
				else:
					++on
					CRO().OnwallIneffectiveCollision(mol.moleculeTable[index], index)
	            #end else
	        #endif

	        # Synthesis or IntermolecularIneffectiveCollision
			else:
				index1 = random.randint(0, len(mol.PE1)-1)
				index2 = random.randint(0, len(mol.PE1)-1)
				if ((mol.KE1[index1]+mol.KE1[index2])<beta):
				    ++syn
				    #CRO().Synthesis(mol.moleculeTable[index1], mol.moleculeTable[index2], index1, index2)
				#endif
				else:
				    ++inef
				    #IntermolecularIneffectiveCollision(mol.moleculeTable[index1], mol.moleculeTable[index2], index1, index2)
				#endelse
			#end else

			# Finding minimum energy
			minEnrg = 1000
			mol.PE1 = mol.PE1
			minEnrgIndex = None

			for j in range(len(mol.PE)):
			    if (mol.PE1[j]<minEnrg):
			        minEnrg = mol.PE1[j]
			        minEnrgIndex = j
			    #endif
			#endfor
		#end for i
	#end cro
	def CalculatePE():
		pass
	def CalculateEnergy(p1,p2,p3,p4):
        
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

C  = CRO()
mol = Molecule()
mol.Mol("CAAUUUUCUGAAAAUUUUCAC", 10, 1)
C.Init(10, .5, .4, 1, 1, 5, 0, "AUGC", mol)
C.CRO(10, .5, .4, 1, 1, 5, 0, "AUGC", mol,10,"output")