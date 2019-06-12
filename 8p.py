import math,functools
value11,value12=map(int,input().split())
value13=[int(i1) for i1 in input().split()]
for i1 in range(value12):
    value14,value15=map(int,input().split())
    result=functools.reduce(math.gcd,value13[value14-1:value15])
    print(result)
