#!/bin/python
# code snippet illustrating input/output methods 
N, K = raw_input().split()
N = int(N)
K = int(K)
c = []

total = 0
purchased = 0


numbers = raw_input()

i = 0
for number in numbers.split():
   c.append( int(number) )
   i = i+1

c = sorted(c)

friends = [0] * K
 
while len(c) > 0:
     total += (friends[purchased % len(friends)] + 1) * c.pop()
     friends[purchased % len(friends)] += 1
     purchased += 1
 
print(total)
