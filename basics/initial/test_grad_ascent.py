import numpy as np
def dot_val(th,X):
    """
    th - (n+1)x1
    X - 1x(n+1)
    """ 
    import numpy as np
    out=X@th
    return out[0][0]
def hval(th,X):
    """
    th - (n+1)x1
    X - 1x(n+1)
    """ 
    from math import exp
    out=1/(1+exp((-1)*dot_val(th,X)))
    return out
def probab(th,X,y):
    """
    X - mx(n+1)
    y- mx1
    th - (n+1)x1
    """
    from math import log
    ZERO=1.0e-16
    m=y.shape[0]
    n=th.shape[0]-1
    s=0.0
    for i in range(m):
        t=X[i].reshape(1,n+1)
        ht=hval(th,t)
        temp=y[i][0]
#         if (abs(ht)<=ZERO or abs(1-ht)<=ZERO):
#             return 'c'
        #print(ht)
        s+=temp*log(ht)+(1-temp)*log(1-ht)
    return s
def pred(X,y,test):
    """
    X - mx(n+1)
    y- mx1
    test - 1x(n+1)
    """
    ERR=1.0e-7
    import numpy as np
    alp=1.0e-5
    m=y.shape[0]
    n=X.shape[1]-1
    th=np.zeros(n+1)
    th=th.reshape(n+1,1)
    j0=probab(th,X,y)
    conv=j0
    it=0
    while (abs(conv)>=ERR):
        for j in range(n+1):
            t=0.0
            for i in range(m):
                t1=X[i].reshape(1,n+1)
                t+=(y[i]-hval(th,t1))*X[i][j]
            th[j]=th[j]+alp*t
        j1=probab(th,X,y)
        conv=j1-j0
        j0=j1
        it+=1
    if hval(th,test)>=0.5:
        return(1,it)
    return(0,it)
us=[]
for i in range(17):
    us.append(i)
del us[11]
y=np.loadtxt("../Epoch/Selection_Hackathon/Dataset.csv",delimiter=',',skiprows=321,usecols=[11])
y=y.reshape(1279,1)
#print(y)
X=np.loadtxt("../Epoch/Selection_Hackathon/Dataset.csv",delimiter=',',skiprows=321,usecols=us)
X=np.c_[np.ones(1279),X]
for i in range(1279):
    X[i][1:18]=X[i][1:18]/10
# print(X)
# print(X.shape)
te=np.loadtxt("../Epoch/Selection_Hackathon/Dataset.csv",delimiter=',',skiprows=1,max_rows=320,usecols=us)
te=np.c_[np.ones(320),te]
for i in range(320):
    te[i][1:18]=te[i][1:18]/10
teans=np.loadtxt("../Epoch/Selection_Hackathon/Dataset.csv",delimiter=',',skiprows=1,max_rows=320,usecols=[11])
teans=teans.reshape(320,1)
# print(teans.shape)
for i in range(5):
    temp=te[i].reshape(1,17)
    print(pred(X,y,temp))