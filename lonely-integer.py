#!/usr/bin/py
def lonelyinteger(a):
    answer = 0
    d={}
    for i in a:
        d[i] = d.get(i, 0)+1
    for i in d:
        if d[i]==1:
            break
    answer = i
    return answer
if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)
