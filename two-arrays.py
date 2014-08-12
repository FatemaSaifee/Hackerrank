t = input() 
for x in range(t):
    s1 = raw_input()
    nk = s1.split()
    n = int(nk[0])
    k = int(nk[1])
    s2 = raw_input()
    a = sorted(map(int, s2.split()))
    s3 = raw_input()
    b = sorted(map(int, s3.split()))
    flag = 0        
    for i in range(n):
            if not (a[i] + b[n-i-1] >= k):
                flag = 1
                break
    if flag == 0:
            print "YES"
    else:
            print "NO"
            