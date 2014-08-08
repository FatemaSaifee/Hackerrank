n = input()
s1 = raw_input()
a = map(str, s1.split())
m = input()
s2 = raw_input()
b = map(str, s2.split())

for i in a:
    if i in b:
        b.remove(i)
    

print ' '.join(sorted(set(b)))
