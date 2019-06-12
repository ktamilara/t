xx1=int(input())
a1=list(map(int,input().split(" ")))
l1=len(a1)
m1=[]
for i1 in range(0,l):
    v1=max(a1[i1:])
    if(v1==a1[i1]):
        m1.append(v1)
for i1 in range(0,len(m1)-1):
    print(m1[i1],end=" ")
print(m1[len(m1)-1],end="\n")
print(max(a1),end="")
