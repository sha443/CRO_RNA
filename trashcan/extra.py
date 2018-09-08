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