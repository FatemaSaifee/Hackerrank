T=input()
for i in range(0,T):
    m = input()
    n = input()
    s = raw_input()
    flag = 0
    numbers = map(int, s.split())
    for j in range(0,n-1):
        for k in range(j+1,n):
            if numbers[i] + numbers[j] == m:
                if i < j:
                    print str(i+1) + " " + str(j+1)
                else:
                    print str(j+1) + " " + str(i+1)
                flag = 1
                break
        if (flag == 1):
            break
