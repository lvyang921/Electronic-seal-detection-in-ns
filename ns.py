import numpy as np
import random

def Discriminate(lef,rig,x,p0=0.925845,ru=1.96):        #Calculation the if the x in interval[lef,rig] steady
    res=[]
    long=len(x)
    for i in range(long):
        if i==0:
            if lef<=x[0]<=rig:
                x[0]=1
                res.append(1)
            else:
                x[0]=0
                res.append(0)
        else:
            if lef<x[i]<=rig:
                x[i]=1
            else:
                x[i]=0
            res.append(sum(x[:i+1])/(i+1))
    p=res[-1]
    pca=0
    for i in range(long):
        pl=p-ru*pow((p*(1-p))/(i+1),0.5)
        pr=p+ru*pow((p*(1-p))/(i+1),0.5)
        if pl<=res[i]<=pr:
            pca+=1
    if pca/long>=p0:
        return True
    else:
        return False

def Division(x,n):         #Division list(x) for n part
    res=[]
    i=0
    while i<=100:
        res.append(np.percentile(x,i))
        i+=100.0/n
        if i>=100:
            i=100
            res.append(np.percentile(x, i))
            break
    return res              #res为分为点的值

def Fromltor(x):                     #Calculat ns !!!
    n=int(1.87*pow(len(x)-1,0.4))
    tmp=Division(x,n)
    res=[]
    i=0
    j=i+1
    while j<=len(tmp)-1:
        if Discriminate(tmp[i],tmp[j],x)==True:
            res.append([tmp[i],tmp[j]])
            i=j
            j=i+1
        else:
            j+=1
    print('Total collections:'+str(n))
    print('Stable collections:'+str(len(res)))
    return 1-len(res)/float(n)

