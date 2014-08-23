from math import ceil
from math import floor
from math import sqrt

s = raw_input()
w = int(floor(sqrt( len(s) )) )
h = int(ceil(sqrt( len(s) )))
op=""
i=0
j=0
p=0
while i<h:
    p = i
    j = 0
    if p >= len(s):
        break;
    while j<=w:
        if p >= len(s):
            break;
        op += s[p]
        p += h
        j += 1
    i = i + 1
    op += " "
    
    
print op
