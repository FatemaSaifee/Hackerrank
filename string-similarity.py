import sys
def stringSimilarity(s):
    l, r, n = 0, 0, len(s)
    z = [0] * n
    
    for i in range(1, n):
        if i <= r and z[i - l] < r - i + 1:
            z[i] = z[i - l]
        
        else:
            # Update Z-box bounds
            l = i
            if i > r:
                r = i
            
            while r < n and s[r - l] == s[r]:
                r += 1
            
            z[i] = r - l
            r -= 1
            
    # Return the total number of string similarities
    return n + sum(z)
# Tail starts here
if __name__ == '__main__':
    t = input()
    for i in range(0,t):
        a=raw_input()
        print stringSimilarity(a)
