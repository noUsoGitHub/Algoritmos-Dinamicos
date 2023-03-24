
from MemorizadoRecursivo import rec as Memory
from Recursivo import rec as Recursive
from Iterativo import rec as Iterative
from Tabulado import rec as BottomUp
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np

def testFunction(seq=[-7,12,-7,0,14,-7,5]):
    import time as t
    time =[]
    values=[]
    print("Secuencia: ",seq)
    values.append(Iterative(seq))
    print("Iterativo: ",values[0])
    start_time = t.time( )
    values.append(Recursive(seq))
    print("Recursivo: ",values[1])
    time.append(t.time( ) - start_time) 
    start_time = t.time( )
    values.append(Memory(seq))
    print("Memory:    ",values[2])
    time.append(t.time( ) - start_time) 
    start_time = t.time( )
    values.append(BottomUp(seq))
    print("Tabulado:  ",values[3])
    time.append(t.time( ) - start_time) 
    with open("Test.res","a") as test:
        val="Not Pass"
        if all(x == values[0] for x in values):
            val="Pass"
        test.write(f"{seq} {val} \n")
    with open("output.res", "a") as fileW:
        fileW.write(f"{len(seq)} {time[0]:.15f} {time[1]:.15f} {time[2]:.15f}\n")
    return 
def GenerarResultados():
    import random
    import json
    sequences = []
    for n in range(1, 30):
        seq = [random.randint(-10, 10) for _ in range(n)]
        sequences.append(seq)
    with open('sequences.txt', 'w') as file:
        json.dump(sequences, file)
    with open('sequences.txt', 'r') as file:
        sequences = json.load(file)
    for i in range(len(sequences)):
        print(i)
        testFunction(sequences[i])
def results():
    df = pd.read_csv('output.res', sep=' ', header=None, names=['n','recursivo','Memory', 'bottom_up'])
    print(df)
    df.plot(y=['recursivo','Memory','bottom_up'], x='n')
    plt.show()
    mod = smf.ols(formula='recursivo ~ np.power(2,n)', data=df)
    rest = mod.fit()
    print(rest.summary())
    sm.graphics.plot_fit(rest, "np.power(2, n)")
    plt.show()
    mod = smf.ols(formula='Memory ~ np.log(n)', data=df)
    rest = mod.fit()
    print(rest.summary())
    sm.graphics.plot_fit(rest, "np.log(n)")
    plt.show()
    mod = smf.ols(formula='bottom_up ~ np.power(n,3)', data=df)
    rest = mod.fit()
    print(rest.summary())
    sm.graphics.plot_fit(rest, "np.power(n, 3)")
    plt.show()
results()


