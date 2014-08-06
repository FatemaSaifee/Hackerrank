t=int(raw_input())
for i in range (0,t):
    N=int(raw_input())
    s=""
    for i in range(N,-1,-1):
                
        if i % 3 == 0 and (N - i) % 5 == 0 :
                   
            s = '5'* i + '3'*(N - i);

            break;
            
    if s == "":
        s=-1
    print s
 
