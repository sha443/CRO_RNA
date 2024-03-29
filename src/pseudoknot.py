import energy
# Condition for loops to form a pseudoknot
L1_LOWER = 1
L1_UPPER = 100

L2_LOWER = 0 
L2_UPPER = 50

L3_LOWER = 2 
L3_UPPER = 100

# LongPK constants
INIT = 7.0
PENALTY = 0.1

def PseudoknotHandler(scElements,pkElements,seq):
    cc06,cc09,longPk = ScanList(pkElements)
    ene = 0
    if(cc06):
        CC06Result = energy.CC06(cc06,seq)
        for allEnergy in CC06Result:
            ene += CC06Result[allEnergy]
            # print(CC06Result[allEnergy])
    # if(cc09):
    #     ene = energy.CC09(cc09,scElements)
    #     print(ene)
    if(longPk):
        longPkResult= energy.LongPK(longPk, scElements, INIT, PENALTY)
        for allEnergy in longPkResult:
            ene += longPkResult[allEnergy]
            # print(longPkResult[allEnergy])
    return ene
# end function


def LoopsFulfill(l1, l2, l3):
    loops_fulfilled = False
    
    if l1 >= L1_LOWER and l1 < L1_UPPER:
        if l2 >= L2_LOWER and l2 < L2_UPPER:                               
            if l3 >= L3_LOWER and l3 < L3_UPPER:
                loops_fulfilled = True
    return True
    return loops_fulfilled
# end function

def BuildPseudoknots(moleculeShort,stemPool,infoTable):
    # Manipulate moleculeShort, stemPool


    pkList = []
    stems_shortened = {}
    for x in moleculeShort:
        i,j, stemlength1 = moleculeShort[x]
        for y in stemPool:
            k,l, stemlength2 = infoTable[y]

            #i, j = S1
            #k, l = S2

            if (l - i + 1) > 1 and (l - i + 1) < 400:
                l1 = k - (i + stemlength1)            
                l2 = (j - stemlength1 + 1) - (k + stemlength2)
                l3 = (l - stemlength2) - j
                # print( k, "-" ,"(" ,i , "+" ,stemlength1,"=",l1)
                # print("(",j, "-", stemlength1 ,"+1) - (", k, "+", stemlength2,") = ",l2)
                #print(i, j, k, l, stemlength1, stemlength2, l1, l2, l3)
                
                if LoopsFulfill(l1, l2, l3):
                    #print(i, j, k, l, stemlength1, stemlength2, l1, l2, l3) 
                    pkList.append((i, j, k, l, stemlength1, stemlength2, l1, l2, l3))
                #end  
                # Case that overlap of 1 bp or 2 bps occurs at L2
                if (l2 == -1 or l2 == -2) and (stemlength1 > 3 or stemlength2 > 3):
        
                    marker, l1, l2, l3, newStemlength1, newStemlength2 = Overlap(l1, l2, l3, stemlength1, stemlength2)

                    if marker:           
                        if LoopsFulfill(l1, l2, l3):
                        	#print(i,j,k,l,stemlength1,stemlength2,l1,l2,l3)
                            pkList.append((i, j, k, l, stemlength1, stemlength2, l1, l2, l3))

                            # Add shortened stems to dictionary                            
                            s1_shortened = i, j, stemlength1     
                            if stemlength1 != newStemlength1:
                                stems_shortened[s1_shortened] = newStemlength1, 0.0                                         
                                
                            s2_shortened = k, l, stemlength2

                            if stemlength2 != newStemlength2:
                                stems_shortened[s2_shortened] = newStemlength2, 0.0  
                        # endif
                    # endif
                # endif
            # endif
        # endfor
    # endfor
    # Make the list unique and return 
    pkList = list(set(pkList))
    return pkList,stems_shortened
# end function

def Overlap(l1, l2, l3, stemlength1, stemlength2):

    marker = True
    
    while l2 != 0:
        if l1 == 0:                
            if stemlength1 > 3:         # Cut S1
                stemlength1, l1, l2 = stemlength1 - 1, l1 + 1, l2 + 1                                    
            else:
                l2, marker = 0, False   # It is not possible to resolve the overlap
          
        elif l3 == 1: 
            if stemlength2 > 3:         # Cut S2
                stemlength2, l2, l3 = stemlength2 - 1, l2 + 1, l3 + 1                                  
            else:
                l2, marker = 0, False   # It is not possible to resolve the overlap                          

        elif l1 >= 1 and l3 >= 2:
            if stemlength1 > 3:                 # Cut S1
                stemlength1, l1, l2 = stemlength1 - 1, l1 + 1, l2 + 1                   
            elif stemlength2 > 3:               # Cut S2
                stemlength2, l2, l3 = stemlength2 - 1, l2 + 1, l3 + 1    
            else:
                l2, marker = 0, False   # It is not possible to resolve the overlap
          
        else:
            l2, marker = 0, False       # It is not possible to resolve the overlap          

    return marker, l1, l2, l3, stemlength1, stemlength2
# end function
def ScanList(pkList):
    cc06 = []
    cc09 = []
    longPk = []

    for pkStem in pkList:

        i, j, k, l, stemlength1, stemlength2, l1, l2, l3 = pkStem
        if l2 <= 1:
            cc06.append(pkStem)
        else:
            longPk.append(pkStem)

            # if l2 < 7: 
            #     cc09.append(pkStem)
            # else:
            #     longPk.append(pkStem)
        
    return cc06,cc09,longPk
# end function