
def iterativo(X):
    maxV= float('-inf')
    x,y=0,0
    for i in range(0,len(X)):
        for j in range(0,len(X)):
            val=1
            for k in range(i,j+1):
                val=val*X[k]
            if val>maxV:
                maxV=val
                x,y=i,j
    return X[x:y+1]

def bottomUp(X):
    n = len(X)
    maxV = float('-inf')
    x, y = 0, 0
    dp = [1] * n
    for i in range(n):
        for j in range(i, n):
            dp[j] = dp[j - 1] * X[j]
            if dp[j] > maxV:
                maxV = dp[j]
                x, y = i, j
    return X[x:y+1]

seq=[0,-7,12,-7,0,14,-7,5]
print(iterativo(seq))