import sys

N = sys.stdin.readline()
weights = sorted(map(int, sys.stdin.readline().split(' ')))
R = 0

for weight in weights:        
    if weight > R+1:
        print(R+1)
        break
    R += weight