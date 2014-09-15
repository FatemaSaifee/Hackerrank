from math import *
t=int(raw_input())
assert(t<=5)
assert(t>=1)
for i in range(0,t):
    n=int(raw_input())
    assert(n<=10**5)
    assert(n>=1)
    a=[]
    b=[]
    for j in range(0,int(log(10**9,2)+1)):
        b=[0]*n
        a.append(b)
    number=map(int, raw_input().split())
    for j in range(0,n):
        z=number[j]
        assert(z>=0)
        assert(z<=10**9)
        k=0
        while(z>0):
            a[k][j]=z&1
            z>>=1
            k+=1
    sum1=0
    for j in range(0,int(log(10**9,2)+1)):
        od=0
        for k in range(0,n):
            if(a[j][k]==1):
                od=1
                break
        if od!=0:
            sum1=(sum1+ 2**(j+n-1))%1000000007
    print sum1
