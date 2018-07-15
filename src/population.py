
board = []
infoTable = []
# Cheeck if it makes a valid base pair of RNA
def isPair(c1,c2):
    if((c1=="A" and c2=="U") or (c1=="U" and c2=="A")):
        return 1
    elif ((c1=="G" and c2=="C") or (c1=="C" and  c2=="G")):
        return 1
    elif ((c1=="G" and c2=="U") or (c1=="U" and c2=="G")):
        return 1
    else:
        return 0

def checkerboard(sequence, nPopulation):

    for i in range(0,len(sequence)-1):
        board.append([])
        for j in range(0,len(sequence)-1):
            if(j<i):
                if(isPair(sequence[i],sequence[j])):
                    board[i].append(1)
                else:
                    board[i].append(0)
            else:
                board[i].append(0)

    #for i in range(0,len(sequence)-1):
    #    for j in range(0,len(sequence)-1):
    #        print(board[i][j])
     #   print("\n")

def findDiagonal(sequence):
    info = []
    for i in range(len(sequence)-2,0,-1):
        for j in range(0,len(sequence)-2):
            if(board[i][j]==1 and board[i-1][j+1]==1):
                count=0
                k=0
                while True:
                    if (board[i-k][j+k] == 1):
                        count+=1
                        board[i - k][j + k] = 2
                    else:
                        break
                    k = k+1
                if(count>3):
                    info.append((j,i,count))  # start, end, length

    # sort info table
    infoTable = sorted(info, key=lambda x: x[2],reverse=True)
    print(infoTable)




checkerboard("CAAUUUUCUGAAAAUUUUCAC",1)
findDiagonal("CAAUUUUCUGAAAAUUUUCAC")