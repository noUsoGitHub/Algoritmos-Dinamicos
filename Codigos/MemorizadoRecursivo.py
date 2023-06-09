from speedCommons import pretty

def MemorizadoRecursivo(sec,i,j,M):
        if i==j:
            return sec[i] # Sin multiplicar
        if M[i][j]!=float('-inf'): # Si ya se calculo
            return M[i][j]

        max_product = 1 # Caso Base de Multiplciar
        for k in range(i,j+1): # Subsecuencia para multiplicar
            if sec[k]!=0: # Si no es 0
                max_product *= sec[k] # Multiplicamos
            else:
                break # Si es 0 se retorna o rompe el ciclo actual de la secuencia pues despues de 0 todo dara 0 por lo cual este es el mayor
        M[i][j] =  max(max_product,MemorizadoRecursivo(sec,i,j-1,M),MemorizadoRecursivo(sec,i+1,j,M)) # Se llena la Matriz con los valores maximos
        return M[i][j] # Se retorna el valor i,j

def MemorizadoRecursivo2(sec,i,j,M):
    if i==j:
        M[i][j] = sec[i]
        return sec[i],i,j
    if M[i][j]>float('-inf'):
        return M[i][j],i,j
    max_product = 1
    for k in range(i,j+1):
        max_product *= sec[k]
    M[i][j] = max_product
    MemorizadoRecursivo2(sec,i,j-1,M)   
    MemorizadoRecursivo2(sec,i+1,j,M)    
    return M

def subSequence(X, memo):
        #max_val = memo[0][len(X)-1]
        import numpy
        max_val = numpy.max(memo)
        i, j = 0, len(X)-1
        for x in range(len(X)):
            for y in range(x, len(X)):
                if memo[x][y] == max_val:
                    i, j = x, y
                    break
        return X[i:j+1]
def rec(seq):
        M = [[float('-inf') for i in range(len(seq))] for j in range(len(seq))]
        #MemorizadoRecursivo(seq,0,len(seq)-1,M)
        MemorizadoRecursivo2(seq,0,len(M)-1,M)
        #pretty.prettyMatrix(M) # Unicamente para ver la matriz
        return subSequence(seq, M) # La subsecuencia



