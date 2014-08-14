prod=0
n=input()
assert n<=10**6
assert n>=1
a=map(int,raw_input().split())
for i in range(n):
    assert a[i]<=10**9
    assert a[i]>= (-1)*10**9
    prod+=a[i]*(i+1)
max_prod=prod
sigma=sum(a)
for i in range(n):
    prod+=sigma
    prod-=a[-1-i]*(n)
    if prod>max_prod:
        max_prod=prod
print max_prod