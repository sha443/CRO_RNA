import random

def Decomposition (molecule):
        
    length = len(molecule)
    m1 = list(range(length))
    m2 = list(range(length))
    mid =int(length/2)


    # First half goes to the first half of the new molecule1
    for i in range(0,mid):
        m1[i] = molecule[i]
    #Endfor
    # Second half goes to the second half of the new molecule2
    for i in range(mid,length):
        m2[i] = molecule[i]
    #Endfor

    # Molecule1 second half randomly chosen
    for i in range(mid,length):
        for j in range(4000):
            for k in range(200):
                pass
            #Endfor
        #Endfor
        m1[i] = random.randint(0, length)
    #Endfor

    # Molecule2 first half randomly chosen
    for i in range(0,mid):
        for j in range(4000):
            for k in range(200):
                pass
            #Endfor
        #Endfor
        m2[i] = random.randint(0, length)
    #Endfor
        
    #test
    # print(m1)
    # print(m2)
    # Return 2 new molecule
    return m1,m2

#Module Test
#Decomposition([3, 2, 0, 5, 8, 10, 5, 2, 5, 1])