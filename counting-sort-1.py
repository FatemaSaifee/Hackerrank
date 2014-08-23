size = input()
l = map(int,raw_input().split())
ans = []
for i in range(100):
    ans.append(str(l.count(i)))
print " ".join(ans)
