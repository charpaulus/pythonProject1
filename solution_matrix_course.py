import copy
from sys import stdin


class MatrixError(BaseException):
    def __init__(self, Matrix, other):
        self.matrix1 = Matrix
        self.matrix2 = other

class Matrix:
    def __init__(self, mL):
        self.mL = copy.deepcopy(mL)

    def __add__(self, other):
        if isinstance(other, Matrix):
            if len(self.mL) == len(other.mL):
                for i in range(len(self.mL)):
                    if len(self.mL[i]) == len(other.mL[i]):
                        newL = []
                        for i in range(len(self.mL)):
                            tmpL = []
                            for j in range(len(self.mL[0])):
                                tmpL.append(self.mL[i][j] + other.mL[i][j])
                            newL.append(tmpL)
                    else:
                        raise MatrixError(self, other)
            else:
                raise MatrixError(self, other)
        else:
            raise MatrixError(self, other)
        return Matrix(newL)

    def __mul__(self, other):
        newL = []
        for i in range(len(self.mL)):
            tmpL = []
            for j in range(len(self.mL[0])):
                tmpL.append(self.mL[i][j] * other)
            newL.append(tmpL)
        return Matrix(newL)

    __rmul__ = __mul__

    def size(self):
        return (len(self.mL), len(self.mL[0]))

    def __str__(self):
        strmL = ''
        for i in range(len(self.mL)):
            strmLt = ''
            for j in range(len(self.mL[0])):
                strmLt = strmLt + str(self.mL[i][j]) + '\t'
            strmL = strmL + strmLt.strip('\t') + '\n'
        strmL = strmL.strip('\n')
        return strmL


#exec(stdin.read())
m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
print(m1 + m2)

m2 = Matrix([[0, 1, 0], [20, 0, -1]])
try:
    m = m1 + m2
    print('WA\n' + str(m))
except MatrixError as e:
    print(e.matrix1)
    print(e.matrix2)
