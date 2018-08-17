import random

def OnWall (molecule):
        
    moleculeNew = molecule

    i = random.randint(0, len(molecule)-1)
    j = random.randint(0, len(molecule)-1)

    if (molecule[i] + j <= len(molecule)):
        moleculeNew[i] = molecule[i] + j
    else:
        if(molecule[i]>j):
            moleculeNew[i] = molecule[i] - j
        else:
            moleculeNew[i] =  j - molecule[i]
        # Endif
    #Endif
    #print(moleculeNew)
    
    return moleculeNew

#Module Test
#OnWall([3, 2, 0, 5, 8, 10, 5, 2, 5, 1])