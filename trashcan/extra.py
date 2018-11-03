# From population after Finding stems 
# Finding pseudoknot
        mol2 = mol  # make a duplicate of molecule
        for i,j,len1 in infoTable:
            for k,l,len2 in pool:
               
                overlap=0
                overlap2=0
                newBond=0
                
                if(i<k and k<j and j<l):   # condiiton for H-type Pseudoknot
                    # Pseudoknot info
                    # Loop lenght calculation for energy evaluation 
                    l1 = k - (i + len1)
                    l2 = (j - len1 + 1) - (k + len2)
                    l3 = (l - len2) - j
                    #print(l1,l2,l3,"pseudoknot")
                    pseudoStem=0
                    extra=0
                    # for(u=k,v=l; u<k+len2; u++,v--)
                    for u,v in zip(range(k,k+len2,1),range(l,0,-1)):
                        if(overlap>=2):
                            break
                        if(flag[u]==0 and flag[v]==0):
                            flag[u] = 2
                            flag[v] = 2
                            extra+=1
                            pseudoStem+=1
                        elif(extra>0 and (flag[u] != 3 and flag[v] != 3)):
                            overlap+=1
                            pseudoStem+=1
                    # End for u,v
                    if(pseudoStem>=2):
                        extra=0
                        for u,v in zip(range(k,k+len2,1),range(l,0,-1)):
                            if(overlap2==2):
                                break
                            if (flag[u] == 2 and flag[v] == 2):
                               # print("matched at:",u,v)
                                flag[u] = 3
                                mol2[u] = '['
                                flag[v] = 3
                                mol2[v] = ']'
                                extra+=1
                            elif(extra>0 and (flag[u] != 3 and flag[v] != 3)):
                                overlap2+=1
                               # print("overlaped at:",u,v)

                                flag[u] = 3
                                mol2[u] = '['
                                flag[v] = 3
                                mol2[v] = ']'
                                mol2 = RemoveParanthesis(u,v,mol2,makePair)
                            # End if
                        # End for u,v
                    # End pseudostem
                    else: # Revoke the flag status
                        for u,v in zip(range(k,k+len2,1),range(l,0,-1)):
                            if(flag[u] == 2 and flag[v] == 2):
                                flag[u] = 0
                                flag[v] = 0
                            # endif
                        # End for u,v
                    #end main loop
                # end pseudo condition
            # end for k,l, l2
        # end for i,j,l1

# from main.py inside Finding pseudoknot
# for population in mol.moleculeTable:
#       stemList = []
#       pkList = []
#       for serial in population:
#               # take i,j, len form infoTable according to the gene serial
#               stemList.append(mol.infoTable[serial])
#       # endfor
#       pkList,stemShortened = pseudoknot.BuildPseudoknots(stemList)
#       # print(pkList)
#       # print(stemShortened)
# #endfor
# cc06,cc09,longPk = pseudoknot.ScanList(pkList)

def Overlap(molecule,stemPool):

    # Finding pseudoknot
    mole2 = molecule  # make a duplicate of molecule
    for i,j,len1 in infoTable:
        for k,l,len2 in stemPool:
            overlap=0
            overlap2=0
            newBond=0
            
            if(i<k and k<j and j<l):   # condiiton for H-type Pseudoknot
                pseudoStem=0
                extra=0
                # for(u=k,v=l; u<k+len2; u++,v--)
                for u,v in zip(range(k,k+len2,1),range(l,0,-1)):
                    if(overlap>=2):
                        break
                    if(flag[u]==0 and flag[v]==0):
                        flag[u] = 2
                        flag[v] = 2
                        extra+=1
                        pseudoStem+=1
                    elif(extra>0 and (flag[u] != 3 and flag[v] != 3)):
                        overlap+=1
                        pseudoStem+=1
                # End for u,v
                if(pseudoStem>1):
                    extra=0
                    for u,v in zip(range(k,k+len2,1),range(l,0,-1)):
                        if(overlap2==2):
                            break
                        if (flag[u] == 2 and flag[v] == 2):
                            #echo "matched at:".$u." ".$v."<br>";
                            flag[u] = 3
                            mol2[u] = '['
                            flag[v] = 3
                            mol2[v] = ']'
                            ++extra
                        elif(extra>0 and (flag[u] != 3 and flag[v] != 3)):
                            ++overlap2
                            #echo "overlaped at:".$u." ".$v."<br>";

                            flag[u] = 3
                            mol2[u] = '['
                            flag[v] = 3
                            mol2[v] = ']'
                            mol2 = RemoveParanthesis(u,v,mol2,pair);
                        # End if
                    # End for u,v
                # End pseudostem
                else: # Revoke the flag status
                    for u,v in zip(range(k,k+len2,1),range(l,0,-1)):
                        if(flag[u] == 2 and flag[v] == 2):
                            flag[u] = 0
                            flag[v] = 0
                        # endif
                    # End for u,v
                #end main loop
            # end pseudo condition
        # end for k,l, l2
    # end for i,j,l1

pseudoStem=0
                    extra=0
                    # for(u=k,v=l; u<k+len2; u++,v--)
                    for u,v in zip(range(k,k+len2,1),range(l,0,-1)):
                        if(overlap>=2 or (len1-overlap)<=3):
                            break
                        if(flag[u]==0 and flag[v]==0):
                            flag[u] = 2
                            flag[v] = 2
                            extra+=1
                            pseudoStem+=1
                        elif(extra>0 and (flag[u] != 3 and flag[v] != 3)):
                            overlap+=1
                            pseudoStem+=1
                    # End for u,v
                    if(pseudoStem>=2):
                        extra=0
                        for u,v in zip(range(k,k+len2,1),range(l,0,-1)):
                            # Maximum allowed overlap is 2
                            if(overlap2==2):
                                break
                            if (flag[u] == 2 and flag[v] == 2):
                               # print("matched at:",u,v)
                                flag[u] = 3
                                mol2[u] = '['
                                flag[v] = 3
                                mol2[v] = ']'
                                extra+=1
                            elif(extra>0 and (flag[u] != 3 and flag[v] != 3)):
                                overlap2+=1
                               # print("overlaped at:",u,v)

                                flag[u] = 3
                                mol2[u] = '['
                                flag[v] = 3
                                mol2[v] = ']'
                                mol2 = RemoveParanthesis(u,v,mol2,makePair)
                            # End if
                        # End for u,v
                    # End pseudostem
                    else: # Revoke the flag status
                        for u,v in zip(range(k,k+len2,1),range(l,0,-1)):
                            if(flag[u] == 2 and flag[v] == 2):
                                flag[u] = 0
                                flag[v] = 0
                            # endif
                        # End for u,v
                    #endif

Was in population
Replaced by turnerHandler calling
# # Energy calculation
        # flag1 = 0   # Found au/gu penalty
        # flag2 = 0   # Check if it is the first input
        # flag3 = 0
        # flag4 = 0
        # total_energy = 0
        # energy = 0
        # infoEnergy.sort()
        # for i in range(len(infoEnergy)-1):
            
        #     if(infoEnergy[i][0]+1==infoEnergy[i+1][0]):
        #         flag3 = 1
        #         flag4 = 1
        #         if (flag2 == 0 and ((sequence[infoEnergy[i][0]] == 'A') or (sequence[infoEnergy[i][0]] == 'U') or (sequence[infoEnergy[i][0]] == 'G' and sequence[infoEnergy[i][1]] == 'U') or (sequence[infoEnergy[i][0]]== 'U' and sequence[infoEnergy[i][1]] == 'G'))):
        #             flag1 = 1
        #             flag2 = 1
        #             energy += .45
        #             energy += CalculateEnergy(sequence[infoEnergy[i][0]], sequence[infoEnergy[i][1]], sequence[infoEnergy[i+1][0]], sequence[infoEnergy[i+1][1]])
        #         else:
        #             energy += CalculateEnergy(sequence[infoEnergy[i][0]], sequence[infoEnergy[i][1]], sequence[infoEnergy[i+1][0]], sequence[infoEnergy[i+1][1]])
        #     else:
        #         flag4 = 2
        #         if(flag3==1):
        #             if (((sequence[infoEnergy[i][0]] == 'A') or (sequence[infoEnergy[i][0]] == 'U') or (sequence[infoEnergy[i][0]] == 'G' and sequence[infoEnergy[i][1]] == 'U') or (sequence[infoEnergy[i][0]] == 'U' and sequence[infoEnergy[i][1]] == 'G'))):
        #                 energy += .45
        #                 energy += .43
        #                 energy += 4.09
        #                 total_energy += energy
        #                 flag2 = 0
        #                 flag1 = 0
        #             else:
        #                 if(flag1==1):
        #                     energy += .43
        #                     energy += 4.09
        #                     total_energy += energy
        #                     flag2 = 0
        #                     flag1 = 0
        #                 elif(flag1 != 1):
        #                     energy += 4.09
        #                     total_energy += energy
        #                     flag2 = 0
        #                     flag1 = 0
        #                 # Endifelse
        #             flag3 = 0
        #         #Endif
        #     #Endelse
        # #Endfor
        # if (flag4 != 2):            
        #     if (flag3 == 1):
        #         if (((sequence[infoEnergy[len(infoEnergy)-1][0]] == 'A') or (sequence[infoEnergy[len(infoEnergy) - 1][0]] == 'U') or (sequence[infoEnergy[len(infoEnergy) - 1][0]] == 'G' and sequence[infoEnergy[len(infoEnergy) - 1][1]] == 'U') or (sequence[infoEnergy[len(infoEnergy) - 1][0]] == 'U' and sequence[infoEnergy[len(infoEnergy) - 1][1]] == 'G'))):
        #             energy += .45
        #             energy += .43
        #             energy += 4.09
        #             total_energy += energy
        #             flag2 = 0
        #             flag1 = 0
        #         else:
        #             if (flag1 == 1):
        #                 energy += .43
        #                 energy += 4.09
        #                 total_energy += energy
        #                 flag2 = 0
        #                 flag1 = 0
        #             elif (flag1 != 1):
        #                 energy += 4.09
        #                 total_energy += energy
        #                 flag2 = 0
        #                 flag1 = 0
        #         flag3 = 0
        #         #Endif
        #     #Endif
        # # Endif

        cro.py
        # Energy calculation

        flag1 = 0   # Found au/gu penalty
        flag2 = 0   # Check if it is the first input
        flag3 = 0
        flag4 = 0
        total_energy = 0
        energy = 0
        infoEnergy.sort()
        for i in range(len(infoEnergy)-1):

            if(infoEnergy[i][0]+1==infoEnergy[i+1][0]):
                flag3 = 1
                flag4 = 1
                if (flag2 == 0 and ((sequence[infoEnergy[i][0]] == 'A') or (sequence[infoEnergy[i][0]] == 'U') or (sequence[infoEnergy[i][0]] == 'G' and sequence[infoEnergy[i][1]] == 'U') or (sequence[infoEnergy[i][0]]== 'U' and sequence[infoEnergy[i][1]] == 'G'))):
                    flag1 = 1
                    flag2 = 1
                    energy += .45
                    energy += CRO().CalculateEnergy(sequence[infoEnergy[i][0]], sequence[infoEnergy[i][1]], sequence[infoEnergy[i+1][0]], sequence[infoEnergy[i+1][1]])
                else:
                    energy += CRO().CalculateEnergy(sequence[infoEnergy[i][0]], sequence[infoEnergy[i][1]], sequence[infoEnergy[i+1][0]], sequence[infoEnergy[i+1][1]])
            else:
                flag4 = 2
                if(flag3==1):
                    if (((sequence[infoEnergy[i][0]] == 'A') or (sequence[infoEnergy[i][0]] == 'U') or (sequence[infoEnergy[i][0]] == 'G' and sequence[infoEnergy[i][1]] == 'U') or (sequence[infoEnergy[i][0]] == 'U' and sequence[infoEnergy[i][1]] == 'G'))):
                        energy += .45
                        energy += .43
                        energy += 4.09
                        total_energy += energy
                        flag2 = 0
                        flag1 = 0
                    else:
                        if(flag1==1):
                            energy += .43
                            energy += 4.09
                            total_energy += energy
                            flag2 = 0
                            flag1 = 0
                        elif(flag1 != 1):
                            energy += 4.09
                            total_energy += energy
                            flag2 = 0
                            flag1 = 0
                        # Endifelse
                    flag3 = 0
                #Endif
            #Endelse
        #Endfor
        if (flag4 != 2):            
            if (flag3 == 1):
                if (((sequence[infoEnergy[len(infoEnergy)-1][0]] == 'A') or (sequence[infoEnergy[len(infoEnergy) - 1][0]] == 'U') or (sequence[infoEnergy[len(infoEnergy) - 1][0]] == 'G' and sequence[infoEnergy[len(infoEnergy) - 1][1]] == 'U') or (sequence[infoEnergy[len(infoEnergy) - 1][0]] == 'U' and sequence[infoEnergy[len(infoEnergy) - 1][1]] == 'G'))):
                    energy += .45
                    energy += .43
                    energy += 4.09
                    total_energy += energy
                    flag2 = 0
                    flag1 = 0
                else:
                    if (flag1 == 1):
                        energy += .43
                        energy += 4.09
                        total_energy += energy
                        flag2 = 0
                        flag1 = 0
                    elif (flag1 != 1):
                        energy += 4.09
                        total_energy += energy
                        flag2 = 0
                        flag1 = 0
                flag3 = 0
                #Endif
            #Endif
        # Endif

Operators befor modified the length of modecules

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
        unique = []
        for n in molecule:
            if n not in unique:
                unique.append(n)
        return unique
        # return molecule
    # end function

    def RepairKHP(self,infoTable):
        removeIndex = []
        size = len(infoTable)
        for index in range(size):
            start,end,length = infoTable[index]
            khp = ((end-length+1) - (start+length))
            if(khp<1):
                # Cut 2nt
                length = length-1
                # print(infoTable[index])
                infoTable[index] =  start,end,length
                # print(infoTable[index])

                # But length may less than 3 which is remained unchekced. Fix this later
            # endif
        # Endfor
        return infoTable
    # end function
# end class

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


infoTable = [(7, 22, 7), 
(19, 41, 6), 
(14, 44, 5), 
(28, 40, 5), 
(18, 37, 5), 
(10, 44, 4), 
(21, 43, 4), 
(16, 38, 4), 
(21, 32, 4), 
(0, 29, 4), 
(13, 21, 4), 
(2, 14, 4), 
(35, 44, 3), 
(3, 42, 3),
(3, 38, 3), 
(6, 37, 3),
(24, 37, 3),
(28, 35, 3),
(3, 31, 3),
(16, 31, 3),
(7, 30, 3), 
(19, 30, 3), 
(25, 30, 3), 
(2, 29, 3), 
(12, 28, 3), 
(20, 27, 3), 
(3, 23, 3), 
(16, 23, 3), 
(10, 20, 3), 
(9, 19, 3), 
(14, 19, 3), 
(3, 17, 3), 
(0, 14, 3)]
# print(infoTable,"befor")
# newTable = Operators().RepairKHP(infoTable)
# print(newTable,"after")
