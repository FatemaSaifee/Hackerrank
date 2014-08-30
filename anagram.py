n = input()
for i in range(n):
    ctr = 0
    s = raw_input()
    if len(s)%2 == 1:
        print -1
    else:
        s1=list(s[:len(s)/2])
        s2=list(s[len(s)/2:])
        for i in s1:
            if i in s2:
                s2.remove(i)
                
            else:
                ctr += 1
        print ctr
