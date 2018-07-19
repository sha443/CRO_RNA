import random

# Cheeck if it makes a valid base pair of RNA
def IsPair(c1,c2):
    if((c1=="A" and c2=="U") or (c1=="U" and c2=="A")):
        return 1
    elif ((c1=="G" and c2=="C") or (c1=="C" and  c2=="G")):
        return 1
    elif ((c1=="G" and c2=="U") or (c1=="U" and c2=="G")):
        return 1
    else:
        return 0

# Make dotplot for RNA sequence
def Checkerboard(sequence):
    board = []
    for i in range(0,len(sequence)-1):
        board.append([])
        for j in range(0,len(sequence)-1):
            if(j<i):
                if(IsPair(sequence[i],sequence[j])):
                    board[i].append(1)
                else:
                    board[i].append(0)
            else:
                board[i].append(0)

    #for i in range(0,len(sequence)-1):
    #    for j in range(0,len(sequence)-1):
    #        print(board[i][j])
    #   print("\n")
    return board
# Finding consecutive 4 or more diagonal 1's in board
def FindDiagonal(sequence,dotplot):
    info = []
    infoTable = []

    for i in range(len(sequence)-2,0,-1):
        for j in range(0,len(sequence)-2):
            if(dotplot[i][j]==1 and dotplot[i-1][j+1]==1):
                count=0
                k=0
                while True:
                    if (dotplot[i-k][j+k] == 1):
                        count+=1
                        dotplot[i - k][j + k] = 2
                    else:
                        break
                    k = k+1
                if(count>3):
                    info.append((j,i,count))  # start, end, length

    # sort info table
    infoTable = sorted(info, key=lambda x: x[2],reverse=True)
    
    return infoTable
    

# Generates given number of molecules
def GenerateMolecule(sequenceLength,nPopulation,infoTable):
    molecule = []
    stemPool = []   
    


    for t in range(nPopulation):
        flag = []
        flagValid = []
        makePair = []
        infoEnergy = []
        pool = []
        mol = []    

        # Initialization
        for i in range(sequenceLength):
            flag.append(0)
            flagValid.append(0)
            mol.append(".")

        # Adding paranthesis
        pair = 0
        pairIndex=0
        stempoolIndex =0
        stem = 0

        # Randomize the infoTable for each time population generation
        random.shuffle(infoTable)
        flagStemPool=0

        # Find for new population
        for start,end,length in infoTable:
            # Search inside for making bond
            for j,k in zip(range(start,start+length,1),range(end,0,-1)):
                if(flag[j]==0 and flag[k]==0):
                    flag[j] = 2
                    flag[k] = 2
                    flagValid[j] = 1 # )
                    flagValid[k] = 2 # (
                    stem+=1
            # End for j,k

            # Can make at least 3 stems and the inside brackets are enclosed
            revoke = 0 #Take back all the actions
            if stem>=3:
                for j,k in zip(range(start,start+length,1),range(end,0,-1)):
                    if(flag[j]==2 and flag[k]==2 and Equal12(flagValid,j,k)):
                        flag[j] = 1
                        flag[k] = 1
                        mol[j] = "("
                        mol[k] = ")"
                        infoEnergy.append((j,k))  # start, end
                        makePair.append((j,k))
                    else:
                        revoke = 1
                        break
                # End for j,k

                if(revoke==1):
                    for j,k in zip(range(start,start+length,1),range(end,0,-1)):
                        if(flag[j]==2 and flag[k]==2 and Equal12(flagValid,j,k)):
                            flag[j] = 0
                            flag[k] = 0
                            flagValid[j] = 0
                            flagValid[k] = 0
                    flagStemPool = 1
            # End if stem>=3

            else:
                for j,k in zip(range(start,start+length,1),range(end,0,-1)):
                    if(flag[j]==2 and flag[k]==2 and Equal12(flagValid,j,k)):
                        flag[j] = 0
                        flag[k] = 0
                        flagValid[j] = 0
                        flagValid[k] = 0
                flagStemPool = 1

            if(flagStemPool==1):
                pool.append((start,end,length))
                flagStemPool =0

        # End start, end, length

        # Finding pseudoknot
        mol2 = mol  # make a duplicate of molecule
        for i,j,len1 in infoTable:
            for k,l,len2 in pool:

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
                    if(pseudoStem>=2):
                        extra=0
                        for u,v in zip(range(k,k+len2,1),range(l,0,-1)):
                            if(overlap2==2):
                                break
                            if (flag[u] == 2 and flag[v] == 2):
                                print("matched at:",u,v)
                                flag[u] = 3
                                mol2[u] = '['
                                flag[v] = 3
                                mol2[v] = ']'
                                extra+=1
                            elif(extra>0 and (flag[u] != 3 and flag[v] != 3)):
                                overlap2+=1
                                print("overlaped at:",u,v)

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

        # Energy calculation


        # Add molecules to the mole
        molecule.append(mol2)
        stemPool.append(pool)

    
        # Clear all    
        flagValid.clear()
        flag.clear()

        # no need to clear these, because defined in loop
        #pool.clear()
        #mol.clear()

    return molecule,stemPool,infoEnergy
def RemoveParanthesis(u,v,mol2,makePair):
    for j,k in makePair:
        if(u==j):
            mol2[k] = "."
        elif(u==k):
            mol2[j] = "."
        if(v==j):
            mol2[k] = "."
        elif(v==k):
            mol2[j] = "."
    return mol2
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


def Equal12(flagValid,j,k):

    one=0
    two=0
    if(j>k):   
        swap(j,k)
    for i in range(j,k+1):
        if(flagValid[i]==1):
            one+=1
        elif (flagValid[i]==2):
            two+=1
    
    if(one==two):
        return True
    else:
        return False
    
# Calclates the Gibbs free energy of a molecule on INN-HB model
def CalculateEnergy(p1, p2, p3, p4):
        
    ene = 0
    if ((p1 == 'a' and p2 == 'u' and p3 == 'a' and p4 == 'u') or (p1 == 'u' and p2 == 'a' and p3 == 'u' and p4 == 'a')):
    
        ene = -.93
        return ene
    
    if ((p1 == 'a' and p2 == 'u' and p3 == 'u' and p4 == 'a')):
    
        ene = -1.10
        return ene
    
    if ((p1 == 'a' and p2 == 'u' and p3 == 'g' and p4 == 'u') or (p1 == 'u' and p2 == 'g' and p3 == 'u' and p4 == 'a')):
    
        ene = -.55
        return ene
    
    if ((p1 == 'a' and p2 == 'u' and p3 == 'u' and p4 == 'g') or (p1 == 'g' and p2 == 'u' and p3 == 'u' and p4 == 'a')):
    
        ene = -1.36
        return ene
    
    if ((p1 == 'a' and p2 == 'u' and p3 == 'g' and p4 == 'c') or (p1 == 'c' and p2 == 'g' and p3 == 'u' and p4 == 'a')):
    
        ene = -2.08
        return ene
    
    if ((p1 == 'a' and p2 == 'u' and p3 == 'c' and p4 == 'g') or (p1 == 'g' and p2 == 'c' and p3 == 'u' and p4 == 'a')):
    
        ene = -2.24
        return ene
    
    if ((p1 == 'u' and p2 == 'a' and p3 == 'a' and p4 == 'u')):
    
        ene = -1.33
        return ene
    
    if ((p1 == 'u' and p2 == 'a' and p3 == 'g' and p4 == 'u') or (p1 == 'u' and p2 == 'g' and p3 == 'a' and p4 == 'u')):
    
        ene = -1.0
        return ene
    
    if ((p1 == 'u' and p2 == 'a' and p3 == 'u' and p4 == 'g') or (p1 == 'g' and p2 == 'u' and p3 == 'a' and p4 == 'u')):
    
        ene = -1.27
        return ene
    
    if ((p1 == 'u' and p2 == 'a' and p3 == 'c' and p4 == 'g') or (p1 == 'g' and p2 == 'c' and p3 == 'a' and p4 == 'u')):
    
        ene = -2.35
        return ene
    
    if ((p1 == 'a' and p2 == 'u' and p3 == 'a' and p4 == 'u') or (p1 == 'u' and p2 == 's' and p3 == 'u' and p4 == 's')):
    
        ene = -.93
        return ene
    
    if ((p1 == 'u' and p2 == 'a' and p3 == 'g' and p4 == 'c') or (p1 == 'c' and p2 == 'g' and p3 == 'a' and p4 == 'u') or (p1 == 'g' and p2 == 'u' and p3 == 'g' and p4 == 'c') or (p1 == 'c' and p2 == 'g' and p3 == 'u' and p4 == 'g')):
    
        ene = -2.11
        return ene
    
    if ((p1 == 'g' and p2 == 'u' and p3 == 'c' and p4 == 'g') or (p1 == 'g' and p2 == 'c' and p3 == 'u' and p4 == 'g')):
    
        ene = -2.51
        return ene
    
    if ((p1 == 'g' and p2 == 'u' and p3 == 'g' and p4 == 'u') or (p1 == 'u' and p2 == 'g' and p3 == 'u' and p4 == 'g')):
    
        ene = -.5
        return ene
    
    if ((p1 == 'g' and p2 == 'u' and p3 == 'u' and p4 == 'g')):
    
        ene = +1.29
        return ene
    
    if ((p1 == 'u' and p2 == 'g' and p3 == 'g' and p4 == 'c') or (p1 == 'c' and p2 == 'g' and p3 == 'g' and p4 == 'u')):
    
        ene = -1.41
        return ene
    
    if ((p1 == 'u' and p2 == 'g' and p3 == 'c' and p4 == 'g') or (p1 == 'g' and p2 == 'c' and p3 == 'g' and p4 == 'u')):
    
        ene = -1.53
        return ene
    
    if ((p1 == 'u' and p2 == 'g' and p3 == 'g' and p4 == 'u')):
    
        ene = +.3
        return ene
    
    if ((p1 == 'c' and p2 == 'g' and p3 == 'g' and p4 == 'c')):
    
        ene = -2.36
        return ene
    
    if ((p1 == 'g' and p2 == 'c' and p3 == 'c' and p4 == 'g')):
    
        ene = -3.42
        return ene
    
    if ((p1 == 'g' and p2 == 'c' and p3 == 'g' and p4 == 'c') or (p1 == 'c' and p2 == 'g' and p3 == 'c' and p4 == 'g')):
    
        ene = -3.26
        return ene
    
    return ene
        
# Generates an array of given size and return them with shuffling
def SequenceGenerator(size):

    numbers = []
    for i in range(0,size):
        numbers.append(i)
    random.shuffle(numbers)
    return numbers

def PrintInfo(molecule,stemPool,infoEnergy):
    file = open("output.txt","w+")
    print("Stempool")
    for pools in stemPool:
        for start,end,length in pools:
           print(start,end,length)
        print("\n")

    print("Molecule")
    for mol in molecule:
        for i in range(len(mol)):
            print(mol[i],end="")
            file.write(mol[i])
        file.write("\n")
        print("\n")

    print("infoEnergy")
    for j,k in infoEnergy:
        print(j,k)
    print("\n")