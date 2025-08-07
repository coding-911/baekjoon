import sys
min, max = map(int, sys.stdin.readline().split(' '))
if min == 1: min += 1
complex_numbers = set()
origin = set(i for i in range(min, max+1))
for i in range(2, int(max*(1/2))+1):
    if i not in complex_numbers: 
        # set 에 여러 개 요소를 한 번에 포함 시킬 때는 add가 아닌 update 사용
        complex_numbers.update(range(i+i, max+1, i))
answer = origin - complex_numbers
for a in answer:
    print(a)