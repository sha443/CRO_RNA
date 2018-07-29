import population

# Molecule strcuture 
PE = []
KE = []
numHit = []
minHit = []
minPE = []
minStruct = []
sequence = ""

def Molecule(sequence, popSize, initialKE):
    dotplot = population.Checkerboard(sequence)
    infoTable = population.FindDiagonal(sequence,dotplot)
    molecule, stemPool, infoEnergy, moleculeEnergy, moleculeTable = population.GenerateMolecule(sequence,len(sequence),popSize,infoTable)
    #population.PrintInfo(molecule,stemPool,infoEnergy,moleculeEnergy)


    PE = moleculeEnergy
    for i in range(0,len(moleculeTable)):
        KE.append(initialKE)
        numHit.append(0)
        minStruct.append(moleculeTable[i])
        minPE.append(moleculeEnergy[i])
        minHit.append(0)
        #print(moleculeTable[i],"--",moleculeEnergy[i])
