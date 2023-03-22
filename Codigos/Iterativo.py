def rec(X):
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