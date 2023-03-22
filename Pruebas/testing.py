import numpy as np
seq=[1,12,-7,1,14,-7,5]

def max_product_subsequence_2(X):
    n = len(X)
    memo = [[float('-inf') for _ in range(n)] for _ in range(n)]

    for i in range(n):
        memo[i][i] = X[i]

    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            max_product = X[i]
            max_product_i = X[i]
            for k in range(i+1, j+1):
                product = X[k]
                for l in range(i, k):
                    product *= X[l]
                max_product_i = max(max_product_i, product)
            max_product = max(max_product, max_product_i)
            max_product = max(max_product, memo[i+1][j])
            max_product = max(max_product, memo[i][j-1])
            memo[i][j] = max_product

    return memo[0][n-1], memo

M= (max_product_subsequence_2(seq)[1])
Splt= str(M).split("[")
for ln in Splt:
    ln = ln.replace(",","\t")
    if ln !="":
        print("["+ln)

def find_max_product_subsequence(X, memo):
    n = len(X)
    max_val = float('-inf')
    for x in range(n):
        for y in range(x,n):
            if max_val<=memo[x][y]:
                max_val=memo[x][y]
    i, j = 0, n-1
    for x in range(n):
        for y in range(x, n):
            if memo[x][y] == max_val:
                i, j = x, y
                print(i,j)
                break
    subseq = [X[i]]
    curr_max = X[i]
    for k in range(i+1, j+1):
        if curr_max == 0:
            curr_max = X[k]
            subseq = [X[k]]
        else:
            curr_max *= X[k]
            subseq.append(X[k])
        if curr_max == max_val:
            break
    return subseq

print(find_max_product_subsequence(seq,M))


