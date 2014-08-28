k = input()
alpha1=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
for i in range(k):
    nl = []
    alpha=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    s1 = raw_input()
    s=""
    for i in range(len(s1)):
        if s1[i] not in s:
            s += s1[i]
    t = list(raw_input())
    l = []
    for i in range(len(s)):
        l.append([s[i]])
        alpha.remove(s[i])

    for i in range(len(alpha)):
        l[i%len(s)].append(alpha[i])

    l.sort(key=lambda x:x[0])
    for i in range(len(s)):
        nl += l[i]
    
    for i in range(len(t)):
        if not t[i] == " ":
            t[i]=alpha1[nl.index(t[i])]
            
                    
    print ''.join(t)
