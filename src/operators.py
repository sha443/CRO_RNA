import random
class Operators():

    ######################################################################
    # OnWall Ineffective Colision
    ######################################################################
    def OnWall (self,molecule):
        m = molecule
        i = random.randint(0, len(molecule)-1)
        j = random.randint(0, len(molecule)-1)

        if (molecule[i] + j <= len(molecule)):
            m[i] = molecule[i] + j
        else:
            if(molecule[i]>j):
                m[i] = molecule[i] - j
            else:
                m[i] =  j - molecule[i]
            # Endif
        #Endif
        # print(m)
        m = Operators().Repair(m)

        return m

    ######################################################################
    # Decomposition
    ######################################################################
    def Decomposition (self,molecule):
            
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
        m1 = Operators().Repair(m1)
        m2 = Operators().Repair(m2)

        return m1,m2

    ######################################################################
    # Intermolecular Ineffective Colision
    ######################################################################

    def Intermolecular(self,molecule1, molecule2):
        length1 = len(molecule1)
        length2 = len(molecule2)
        m1 = list(range(length1))
        m2 = list(range(length2))

        #Random numbers x1, x2 generation
        x1 = random.randint(0, length1)
        for j in range(4000):
            for k in range(200):
                pass
            #Endf
        #Endf
        x2 = random.randint(0, length2)

        # Randormly choose form molecule1 or molecule2
        for i in range(0,length1):
            if (i<x1 or i>x2):  #if odd segments
                m1[i] = molecule1[i]
                m2[i] = molecule2[i]
            elif (i>=x1 and x2>=i): # if even segment
                m1[i] = molecule2[i]
                m2[i] = molecule1[i]

        #test
        # print(m1)
        # print(m2)
        # Return 2 new molecule
        m1 = Operators().Repair(m1)
        m2 = Operators().Repair(m2)

        return m1,m2


    ######################################################################
    # Synthesis
    ######################################################################
    def Synthesis(self,molecule1, molecule2):

        length = len(molecule1)
        m = list(range(length))
        for i in range(0,length):
            r = random.uniform(0, 1)
            if (r<.5):
                m[i] = molecule1[i]
            else:
               m[i] = molecule2[i]

        #test
        # print(m)

        m = Operators().Repair(m)
        return m

    ######################################################################
    # Repair operator
    ######################################################################
    def Repair(self,molecule):
        # unique = []
        # for n in molecule:
        #     if n not in unique:
        #         unique.append(n)
        # return unique
        return molecule

######################################################################
#Module Test
######################################################################
# op = Operators()
# mol = [3, 2, 0, 5, 8, 10, 5, 2, 5, 1]
# mol2 = [1, 2, 4, 5, 8, 10, 0, 3, 5, 1]
# op.OnWall(mol)
# op.OnWall(mol2)
# op.Decomposition(mol)
# op.Intermolecular(mol,mol2)
# op.Synthesis(mol,mol2)