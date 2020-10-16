import numpy as np
import matplotlib.pyplot as plt
x=[]
y=[]
bigx=[]
bigy=[]
def func1(r1,r2,d):
    global x,y
    x=list(np.arange(r1,r2,d))
    y=list(range(len(x)))
    for i in range(len(x)):
        z=[]
        s=0.5
        for j in range(70):
            s=x[i]*s*(1-s)
            if j>=50:
                z.append(s)
        y[i]=list(set(z))
    return x,y
def func2():
    global x,y,bigx,bigy
    bigx=[]
    bigy=[]
    for i in range(len(x)):
        n=len(y[i])
        if n<=16:
            a=[x[i]]*n
            b=y[i]
            bigx.extend(a)
            bigy.extend(b)
    plt.plot(bigx,bigy,'b.',ms=5)
    plt.show()

    
           
