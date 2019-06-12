n21=int(input())
l1=[int(i1) for i1 in input().split()]
a1=[]
for i1 in range(0,n21):
    c=11
    for j1 in range(i1,n21):
        c1=c1*l1[j1]
    a1.append(c1)
for i1 in range(0,n21):
    c1=1
    for j1 in range(i1+1):
        c1=c1*l1[j1]
    a1.append(c1)
print(max(a1))
