import numpy as np
import pandas as pd
from pandas import DataFrame as df
from pandas import Series as sr
import matplotlib.pyplot as plt
l=[2,3,5]
def checkPrime(a):
    for i in range(2,int(np.sqrt(a)+1)):
        if a%i==0:
            return False
    return True
def prime(n=1000):
    global l
    if l[len(l)-1]>=n:
        return l
    for i in range(l[len(l)-1]+1,n):
        flag=True
        for j in range(2,int(np.sqrt(i)+1)):
            if i%j==0:
                flag=False
                break
        if flag:
            l.append(i)
    return l
def prime_div(n):
    if checkPrime(n):
        return [n]
    primes=np.array(prime((n+1)//2))
    primes=list(primes[primes<=(n/2)])
    x=[]
    for i in range(len(primes)):
        if n%primes[i]==0:
            x.append(primes[i])
    return x
def prime_pow(n):
    primes=prime_div(n)
    x=[]
    for i in range(len(primes)):
        copy=n
        j=0
        p=primes[i]
        while(copy%p==0):
            copy=copy//p
            j+=1
        x.append(j)
    return x
def evaluate(n):
    primes=prime_div(n)
    powers=prime_pow(n)
    p1,p2,p3=1,1,1
    for i in range(len(primes)):
        p1*=(primes[i]**(powers[i]-1))
        p2*=(primes[i]-1)
        p3*=(powers[i]+1)
    phi=p1*p2
    #euler phi function
    nof=p3
    #Number of factors of n
    s=n-phi-nof+1
    #s is the number of integers x less than n such that gcd(x,n) is not 1 and x is not a factor of n 
    return s,phi,nof
def call(n=100):
    x,y,z=[],[],[]
    for i in range(3,n):
        a,b,c=evaluate(i)
        x.append(a)
        y.append(b)
        z.append(c)
    return x,y,z
def plot_all(n=100):
    x,y,z=call(n)
    l=list(range(3,n))
    fig,ax=plt.subplots(2,2,sharex=True)
    fig.suptitle('N='+str(n))
    ax[0][0].plot(l,x,'b.',label='S(n)')
    ax[0][0].plot(l,y,'k.',label='Phi function')
    ax[0][0].plot(l,z,'r.',label='No of factors')
    ax[0][0].legend(loc='best')
    ax[0][1].plot(l,x,'b.',label='S(n)')
    ax[0][1].plot(l,l,'g-',label='Y=X line')
    ax[0][1].legend(loc='best')
    ax[1][0].plot(l,y,'k.',label='Phi function')
    ax[1][0].plot(l,l,'g-',label='Y=X line')
    ax[1][0].legend(loc='best')
    ax[1][1].plot(l,z,'r.',label='No of factors')
    ax[1][1].legend(loc='best')
    plt.show()
def plot_S(n=100):
    x,y,z=call(n)
    plt.plot(range(3,n),x,'k.')
    plt.title('S(n) on 3<=N<='+str(n))
    plt.show()
def plot_phi(n=100):
    x,y,z=call(n)
    plt.plot(range(3,n),y,'k.')
    plt.title('Phi function on 3<=N<='+str(n))
    plt.show()
def plot_nof(n=100,bar=False):#No. of factors
    x,y,z=call(n)
    if bar:
        s=sr(z).value_counts().sort_index()
        s.plot(kind='bar')
        plt.show()
        return s
    plt.plot(range(3,n),z,'k.')
    plt.title('No. of factors of 3<=N<='+str(n))
    plt.show()
def plot_nop(n=100,bar=False):#No. of prime factors of n including n
    x=[]
    for i in range(3,n):
        x.append(len(prime_div(i)))
    if bar:
        s=sr(x).value_counts().sort_index()
        s.plot(kind='bar')
        plt.show()
        return s
    plt.plot(range(3,n),x,'k.')
    plt.title('No. of prime factors of 3<=N<='+str(n))
    plt.show()
