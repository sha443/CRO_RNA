import random
import Operators
import Molecule

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


######################################################################
# CRO Init
######################################################################
def init(popSize, KELossRate, MoleColl, InitialKE, alpha, beta, buffer, sequence, molecule):
	popSize = popSize
	KELossRate = KELossRate
	MoleColl = MoleColl
	InitialKE = InitialKE
	alpha = alpha
	beta = beta
	buffer = buffer
	sequence = sequence
	molecule = molecule

######################################################################
# OnWall Ineffective Colision handler
######################################################################
def OnwallIneffectiveCollision(molecule, index):
	newMolecule = Operators.OnWall(molecule)
	PEnew = CalculatePE(newMolecule)
	

