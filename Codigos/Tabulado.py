from speedCommons import pretty
def bottomUp(sec,M):
    for i in range(len(sec)):
        for j in range(i,len(sec)):
            max_product = 1
            for k in range(i,j+1):
                if sec[k]!=0:
                    max_product *= sec[k]
                else:
                     break
            M[i][j] = int(max_product)
    return M
def subSequence(X, memo):
        import numpy
        max_val = numpy.max(memo)
        print(max_val)
        i, j = 0, len(X)-1
        for x in range(len(X)):
            for y in range(x, len(X)):
                if memo[x][y] == max_val:
                    i, j = x, y
                    break
        return X[i:j+1]
def rec(seq):
        M = [[float('-inf') for i in range(len(seq))] for j in range(len(seq))]
        bottomUp(seq,M)
        #pretty.prettyMatrix(M) # Unicamente para ver la matriz
        return subSequence(seq, M) # La subsecuencia