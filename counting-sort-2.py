size = input()
l = map(int, raw_input().split())
l = sorted(l)
l2=[]
for i in l:
    l2.append(str(i))
print ' '.join(l2)
