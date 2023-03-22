import numpy as np

def rec(seq):
    M = [[float('-inf') for i in range(len(seq))] for j in range(len(seq))]
    MemorizadoRecursivo(seq,0,len(seq)-1,M)
    return M

def MemorizadoRecursivo(sec,i,j,M):
    if i==j:
        return sec[i]
    if M[i][j]!=float('-inf'):
        return M[i][j]
    max_product = 1
    for k in range(i,j+1):
        if sec[k]!=0:
            max_product *= sec[k]
        else:
            break
    M[i][j] = max(max_product,MemorizadoRecursivo(sec,i,j-1,M),MemorizadoRecursivo(sec,i+1,j,M))
    return M[i][j]

def find_max_product_subsequence(X, memo):
    max_val = memo[0][len(X)-1]
    i, j = 0, len(X)-1
    for x in range(len(X)):
        for y in range(x, len(X)):
            if memo[x][y] == max_val:
                i, j = x, y
                print(i,j)
                break
    return X[i:j+1]


seq=[-7,12,-7,0,14,-7,5]
M = rec(seq)
Splt= str(M).split("[")
for ln in Splt:
   ln = ln.replace(",","\t")
   if ln !="":
       print("["+ln)
print(find_max_product_subsequence(seq,memo=M))



