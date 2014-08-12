string = raw_input()
p = [] 
found = False
# Write the code to find the required palindrome and then assign the variable 'found' a value of True or False
d= {}
for i in string:
    d[i] = d.get(i,0)+1
    
ctr = 0

for i in d:
    if d[i]%2 == 0:
        d[i] = 0
    else:
        d[i] = 1;
    ctr += d[i]
        
if ctr > 1:
    found = False
else:
    found = True

if not found:
    print("NO")
else:
    print("YES")