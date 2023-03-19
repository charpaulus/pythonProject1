def MakeList(ListNum, Num):
    TmpList = []
    for i in range(1, Num+1):
        TmpTuple = (ListNum[i-1], i)
        TmpList.append(TmpTuple)
    TmpList.sort()
    return (TmpList)


def di1(List1, List2, x, y):
    return abs(List1[x][0] - List2[y][0])


def di2(List1, List2, x, y):
    return abs(List1[x-1][0] - List2[y][0])

n = int(input())
PlaceDist = tuple(map(int, input().split()))
m = int(input())
BombDist = tuple(map(int, input().split()))
PlaceN = MakeList(PlaceDist, n)
BombM = MakeList(BombDist, m)
NumBombPl = []
BombPl = []
TmpTuple = ()
j = 0
k = 1
for i in range(len(PlaceN)):
    k = 1
    print('j=', j, 'i=', i)
    while j < len(BombM) and k != 0:
        print(' j=', j, ' i=', i)
        if PlaceN[i][0] <= BombM[j][0]:
            if j == 0 or j == (len(BombM) - 1):
                TmpTuple = (PlaceN[i][1], BombM[j][1])
                NumBombPl.append(TmpTuple)
                k = 0
            elif di1(BombM, PlaceN, j, i) < di2(BombM, PlaceN, j, i):
                TmpTuple = (PlaceN[i][1], BombM[j][1])
                NumBombPl.append(TmpTuple)
 #               j += 1
                k = 0
            else:
                TmpTuple = (PlaceN[i][1], BombM[j - 1][1])
                NumBombPl.append(TmpTuple)
                j += 1
                k = 0
        elif j < len(BombM) - 1 and PlaceN[i][0] <= BombM[j+1][0]:
            if di1(BombM, PlaceN, j, i) < abs(BombM[j+1][0] - PlaceN[i][0]):
                if BombM[j][0] == BombM[j-1][0]:
                    TmpTuple = (PlaceN[i][1], BombM[j - 1][1])
                    NumBombPl.append(TmpTuple)
                    k = 0
                else:
                    TmpTuple = (PlaceN[i][1], BombM[j][1])
                    NumBombPl.append(TmpTuple)
                    k = 0
            elif di1(BombM, PlaceN, j, i) > abs(BombM[j+1][0] - PlaceN[i][0]):
                TmpTuple = (PlaceN[i][1], BombM[j+1][1])
                NumBombPl.append(TmpTuple)
                j += 1
                k = 0
            else:
                if BombM[j][1] < BombM[j+1][1]:
                    TmpTuple = (PlaceN[i][1], BombM[j][1])
                    NumBombPl.append(TmpTuple)
                    k = 0
                else:
                    TmpTuple = (PlaceN[i][1], BombM[j + 1][1])
                    NumBombPl.append(TmpTuple)
                    j += 1
                    k = 0
        elif j == len(BombM) - 1:
            if BombM[j][0] == BombM[j-1][0]:
                TmpTuple = (PlaceN[i][1], BombM[j-1][1])
                NumBombPl.append(TmpTuple)
                k = 0
            else:
                TmpTuple = (PlaceN[i][1], BombM[j][1])
                NumBombPl.append(TmpTuple)
                k = 0
        else:
            j += 1
NumBombPl.sort()
for i in range(len(NumBombPl)):
    print(NumBombPl[i][1], end=' ')
