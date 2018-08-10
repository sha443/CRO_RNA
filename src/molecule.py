import population

class Molecule():
    # Molecule strcuture 
    PE = []
    PE1 = []
    KE = []
    KE1 = []
    numHit = []
    minHit = []
    minPE = []
    minStruct = []
    sequence = ""
    # Molecule table contains permuated stem info and this is the population
    moleculeTable = None 
    moleculeEnergy= None
    infoEnergy= None
    infoTable = None
    stemPool= None
    molecules= None
    def Mol(self,sequence, popSize, initialKE):
        dotplot = population.Checkerboard(sequence)
        infoTable = population.FindDiagonal(sequence,dotplot)
        self.molecules, self.stemPool, self.infoEnergy, self.moleculeEnergy, self.moleculeTable, self.infoTable = population.GenerateMolecule(sequence,len(sequence),popSize,infoTable)
        #population.PrintInfo(molecule,stemPool,infoEnergy,moleculeEnergy)

        self.PE = self.moleculeEnergy
        self.PE1 = self.moleculeEnergy
        for i in range(0,len(self.moleculeTable)):
            self.KE.append(initialKE)
            self.KE1.append(initialKE)
            self.numHit.append(0)
            self.minStruct.append(self.moleculeTable[i])
            self.minPE.append(self.moleculeEnergy[i])
            self.minHit.append(0)
            #print(self.moleculeTable[i],"--",self.moleculeEnergy[i])
        #endfor
    #end
#end class