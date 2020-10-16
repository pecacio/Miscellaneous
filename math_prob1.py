import numpy as np
import pandas as pd
from pandas import DataFrame as df
from pandas import Series as sr
import matplotlib.pyplot as plt
def func1(n=10,trials=100):
    x=[]
    for i in range(trials):
        x.append(list(np.random.permutation(np.arange(1,n,1))))
    data1=df(x,columns=np.arange(1,n,1))
    data1[0]=0
    data1[n]=n
    data2=data1[np.arange(0,n+1,1)]
    data2=diff(data2)
    data2=data2[np.arange(1,n+1,1)]
    data2=data2.abs()
    data2['sum']=data2.sum(axis=1)
    return data2['sum'].mean()
def func2(start=2,stop=10,trials=100):
    x=list(np.arange(start,stop+1,1))
    y=[]
    for i in range(len(x)):
        y.append(func1(x[i],trials))
    while(True):
        print('Plot the values ? (Y/N)')
        inp=str(input())
        if inp=='Y':
            plt.plot(x,y,'r.')
            plt.show()
            break
        elif inp=='N':
            break
        else:
            print('Wrong Input')
    return x,y
def diff(data):
    cpy=data.copy()
    n=len(cpy.columns)
    col=np.array(cpy.columns)
    x=df(columns=col[1:])
    for i in range(n-1):
        x[i+1]=data.iloc[:,i+1]-data.iloc[:,i]
    return x
