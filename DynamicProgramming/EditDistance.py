import numpy as np
from Operation import Operation

def minimumCost(v1, v2, v3):
    comp1 = v1 if v1 < v2 else v2
    comp2 = comp1 if comp1 < v3 else v3

    return comp2

def editDistance(A, n, B, m):
    C = np.asarray([[Operation(-1,'-') for j in range(m+1)] for i in range(n+1)])
    C[0][0] = Operation(0, 'M')

    # Na primeira coluna a operação é DELETE
    for i in range(1, n+1):
        C[i, 0] = Operation(i, 'D')

    # Na primeira linha a operação é INSERT
    for j in range(1, m+1):
        C[0, j] = Operation(j, 'I')
    
    for i in range(1, n+1):
        for j in range(1, m+1):

            if A[i-1] == B[j-1]:
                matchingCost = C[i-1, j-1].cost
                C[i, j] = Operation(matchingCost, '-')
            else:
                deletingCost = C[i][j].cost + 1
                insertingCost = C[i][j-1].cost + 1
                replacingCost = C[i][j-1].cost + 2  
                minimum = minimumCost(deletingCost, insertingCost, replacingCost)
                
                if minimum == deletingCost:
                    C[i][j] = Operation(minimum, 'D')
                elif minimum == insertingCost:
                    C[i][j] = Operation(minimum, 'I')
                elif minimum == replacingCost:
                    C[i][j] = Operation(minimum, 'R')

    LCS = 0
    for i in range(1,n):
        for j in range(1,m):
            if C[i][j].operation == '-':
                LCS += 1
        
    return LCS

if __name__ == "__main__":
    A = "ephrem"
    B = "benyam"
    n = len(A)
    m = len(B)
    LCS = editDistance(A, n, B, m)
    print(f'A mais longa subsequencia comum entre \'{A}\' e \'{B}\' tem tamanho {LCS}')


    A = "numexpr"
    B = "numpy"
    n = len(A)
    m = len(B)
    LCS = editDistance(A, n, B,m)
    print(f'A mais longa subsequencia comum entre \'{A}\' e \'{B}\' tem tamanho {LCS}')

    A = "laranja"
    B = "toranja"
    n = len(A)
    m = len(B)
    LCS = editDistance(A, n, B,m)
    print(f'A mais longa subsequencia comum entre \'{A}\' e \'{B}\' tem tamanho {LCS}')

    A = "marcha"
    B = "carta"
    n = len(A)
    m = len(B)
    LCS = editDistance(A, n, B,m)
    print(f'A mais longa subsequencia comum entre \'{A}\' e \'{B}\' tem tamanho {LCS}')