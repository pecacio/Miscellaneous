import numpy as np
import pandas as pd
from pandas import DataFrame as df
from pandas import Series as sr
def rndlist(n=4):
    x,y=[],[]
    l=list(range(n))
    for i in range(n):
        x.append(np.random.permutation(l))
        y.append(np.random.permutation(l))
    f1=df(x)
    f2=df(y)
    return f1.T,f2.T
def alg(f1,f2):
    n=len(f1)
    temp=df(np.zeros((n,n)),dtype=np.int32)
    itr=[1]*n
    ctr=0
    for i in range(n):
        rn=f1[i][0]
        temp[i][rn]=1
    while(True):
        if(ctr>1000):
            print('Maximum iterations exceeded')
            return
        ctr+=1
        l=list(temp[temp.sum(axis=1)>1].index)
        if len(l)==0:
            return temp
        n1=len(l)
        for i in range(n1):
            ind=l[i]
            x=list(temp.T[temp.T[ind]>0].index)
            y=np.array(f2[ind])
            for j in range(len(y)-1,-1,-1):
                if y[j] in x:
                    temp.iloc[ind:ind+1,:]=0
                    temp[y[j]][ind]=1
        l2=list(temp[temp.sum(axis=0)<1].index)
        for i in range(len(l2)):
            rn=f1[l2[i]][itr[l2[i]]]
            temp[l2[i]][rn]=1
            itr[l2[i]]+=1
    return temp
def pairing(f1,f2):
    t1=alg(f1,f2)
    t2=alg(f2,f1)
    n=len(f1)
    x,y=[],[]
    xt,yt='',''
    for i in range(n):
        for j in range(n):
            if t1[i][j]==1:
                x.append((i,j))
                xt+=str(i)+'->'+str(j)+'\n'
            if t2[i][j]==1:
                y.append((i,j))
                yt+=str(i)+'->'+str(j)+'\n'
    print('When first frame is preferred over second frame:')
    print(xt)
    print('When second frame is preferred over first frame:')
    print(yt)
    return df([x,y],index=['frame1>frame2','frame2>frame1']).T
