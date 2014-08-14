t = input()
assert 10 <= t <= 200000 
a = map(int, raw_input().split())
a = sorted(a)

d = {}
for i in range(1,t):
    diff = a[i] - a[i-1]
    d.setdefault(diff,[]).append(str(a[i-1]))
    d.setdefault(diff,[]).append(str(a[i]))
   
print " ".join(d[min(d.keys())])