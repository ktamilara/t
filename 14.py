from itertools import permutations
ls11=list(input())
p11 = permutations(ls11)
b1=[]
for i1 in list(p11):
    s1=''
    for j1 in i1:
       s1+=j1
    if s1 not in b1:
       b1.append(s1)
       print(s1)
