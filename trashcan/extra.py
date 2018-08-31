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