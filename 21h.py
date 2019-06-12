n11,m1=map(int,input().split())
a1=[]
b1=[]
for i1 in range(n11):
    a1.append(list(map(int,input().split())))
for i1 in range(n11):
    for j1 in range(m1):
        if a1[i1][j1]==0:
            b1.append(i1)
            b1.append(j1)
for i1 in range(0,len(b1),2):
    for h1 in range(m1):
        a[b[i1]][h1]=0
    for h1 in range(n11):
        a1[h1][b1[1i+1]]=0
for i1 in range(n11):
    print(*a1[i1])
