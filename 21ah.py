n11,k1=map(int,input().split())
x1=[]
l11=[]
for i1 in range(n11):
    l1=[int(x1) for x1 in input().split()]
    x1.append(l)
    if 0 in l1:
        m1=l1.index(0)
        l11.append(m1)
for i1 in range(len(x1)):
    if 0 in x1[i1]:
        for j1 in range(k1):
            x[i1][j1]=0
for i1 in l11:
    for j1 in range(n11):
        x[j1][i1]=0
for i1 in x1:
    print(*i1)
