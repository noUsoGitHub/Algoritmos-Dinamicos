def rec(seq):
    val,x,y= Rec_2(seq,0,len(seq)-1)
    return seq[x:y+1]
def Rec_2(sec,i,j):
    if i==j:
        return sec[i],i,j
    max_product = 1
    for k in range(i,j+1):
        max_product *= sec[k]
    t1, t2, t3 = Rec_2(sec,i,j-1)
    t4, t5, t6 = Rec_2(sec,i+1,j)
    if max_product > t1 and max_product > t4:
        return max_product,i,j
    elif t1 > max_product and t1 > t4:
        return t1,t2,t3
    else:
        return t4,t5,t6