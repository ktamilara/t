n11,k1=map(int,input().split())
l1=[int(x1) for x1 in input().split()]
c1=0
for i1 in range(0,n11):
    for j1 in range(i1+1,n11):
        s1=l1[i]1+l[j1]
        if s1==k1:
            c1+=1
if c1>=1:
    print("YES")
else:
    print("NO")
