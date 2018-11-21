import population
from operators import Operators
class Molecule():
    # Molecule strcuture 
    PE = []             # PE of molecule during initial population generation
    PE1 = []            # PE of final molecule after optimization with CRO
    KE = []
    KE1 = []
    numHit = []
    minHit = []
    minPE = []
    minStruct = []
    sequence = ""
    basePairs = {}       # Unique stemlist; size = molSize; Sorted by energy in ascending order
    # Molecule table contains permuated stem info and it is the population
    moleculeTable = None # Stem list of slide; size = popSize
    moleculeEnergy= None # Stem list molecule energy; size = popSize
    infoEnergy= None     # i,j stored for energy evaluation
    stemTable = []       # Stem information; size = stemNo; base of the molecule generation
    infoTable = []       # Stem information; size = stemNo; base of the molecule generation
    stemPool= {}         # Dictionary of unused stems during molecule generation; size = popSize (baseSize - molSize)
    molecules= None      # Vienna RNA notation; no use in the program except showing structure
    moleculeShort = []   # Shortened molecule list of dictionary indexed with original length; size = popSize
    scElements = []      # A list of stems (may be shortened) take participate in secondary structure
    pkElements = []      # A list of stems (pseudoknotted) take participate in making pseudoknot
    elements = []        # scElements + pkElements = uniqueElements
    def Mol(self,sequence, popSize, initialKE,minStem):
        self.sequence = sequence
        dotplot = population.Checkerboard(sequence)
        self.stemTable = population.FindDiagonal(sequence,dotplot,minStem)
        self.infoTable = self.stemTable[:]  # Copying the varible to keep original one
        # print(self.infoTable,'before')

        # RepairKHP operator
        Op = Operators()
        self.infoTable = Op.RepairKHP(self.infoTable)
        # print(self.infoTable,'after')

        self.molecules, self.stemPool, self.infoEnergy, self.moleculeEnergy, self.moleculeTable, self.basePairs,self.infoTable,self.moleculeShort,self.elements = population.GenerateMolecule(sequence,len(sequence),popSize,self.infoTable)
        #population.PrintInfo(molecule,stemPool,infoEnergy,moleculeEnergy)
        self.PE = self.moleculeEnergy
        self.PE1 = self.moleculeEnergy
        for i in range(len(self.moleculeTable)):
            self.KE.append(initialKE)
            self.KE1.append(initialKE)
            self.numHit.append(0)
            self.minStruct.append(self.moleculeTable[i])
            self.minPE.append(self.moleculeEnergy[i])
            self.minHit.append(0)
        #endfor
    #end
#endclass

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# IMPORTANT
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Need to uniquify: moleculeTable