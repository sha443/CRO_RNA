
# Condition for loops to form a pseudoknot
L1_LOWER = 1
L1_UPPER = 100

L2_LOWER = 0 
L2_UPPER = 50

L3_LOWER = 2 
L3_UPPER = 100


def LoopsFulfill(l1, l2, l3):
    loops_fulfilled = False
    
    if l1 >= L1_LOWER and l1 < L1_UPPER:
        if l2 >= L2_LOWER and l2 < L2_UPPER:                               
            if l3 >= L3_LOWER and l3 < L3_UPPER:
                loops_fulfilled = True
    
    return loops_fulfilled
def BuildPseudoknots(stemList):

    pkList = []
    for i,j, stemlength1 in stemList:
        for k,l, stemlength2 in stemList:
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
        
                    marker, l1, l2, l3, stemlength1, stemlength2 = Overlap(l1, l2, l3, stemlength1, stemlength2)

                    if marker:           
                        if LoopsFulfill(l1, l2, l3):
                        	#print(i,j,k,l,stemlength1,stemlength2,l1,l2,l3)
                            pkList.append((i, j, k, l, stemlength1, stemlength2, l1, l2, l3))
                        # endif
                    # endif
                # endif
            # endif
        # endfor
    # endfor
    # Make the list unique and return 
    pkList = list(set(pkList))
    return pkList

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

def ScanList(pkList):
    cc06 = []
    cc09 = []
    longPk = []

    for pkStem in pkList:
        i, j, k, l, stemlength1, stemlength2, l1, l2, l3 = pkStem
        if l2 <= 1:
            cc06.append(pkStem)
        else:
            if l2 < 7: 
                cc09.append(pkStem)
            else:
                longPk.append(pkStem)
        
    return cc06,cc09,longPk


# Calling...
# stems = []
# stems.append((21 ,38 ,6 ))
# stems.append((16 ,29 ,5 ))
# stems.append((18 ,29 ,5 ))
# stems.append((19 ,29 ,5 ))
# stems.append((1 ,17 ,5 ))
# stems.append((8 ,30 ,4 ))
# stems.append((14 ,30 ,4 ))
# stems.append((0 ,25 ,4 ))
# stems.append((2 ,34 ,4 ))
# stems.append((0 ,14 ,4 ))
# stems.append((1 ,11 ,4 ))
# stems.append((2 ,40 ,3 ))
# stems.append((10 ,37 ,3 ))
# stems.append((10 ,29 ,3 ))
# stems.append((11 ,29 ,3 ))
# stems.append((19 ,37 ,3 ))
# stems.append((17 ,29 ,3 ))
# stems.append((21 ,37 ,3 ))
# stems.append((12 ,36 ,3 ))
# stems.append((20 ,29 ,3 ))
# stems.append((21 ,29 ,3 ))
# stems.append((22 ,29 ,3 ))
# stems.append((9 ,27 ,3 ))
# stems.append((0 ,35 ,3 ))
# stems.append((1 ,23 ,3 ))
# stems.append((1 ,22 ,3 ))
# stems.append((1 ,21 ,3 ))
# stems.append((1 ,20 ,3 ))
# stems.append((1 ,19 ,3 ))
# stems.append((1 ,18 ,3 ))
# stems.append((28 ,40 ,3 ))
# stems.append((28 ,34 ,3 ))
# stems.append((1 ,12 ,3 ))
# stems.append((2 ,31 ,3 ))



# pkList = BuildPseudoknots(stems)

# cc06,cc09,longPk = ScanList(pkList)
# print(pkList)
