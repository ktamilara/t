r1,s1=map(int,input().split())
l1=list(map(int,input().split()))
c1=0
for x1 in l1:
    if(x1>s1):
        l1.remove(x1)
for i1 in range(0,len(l1)):
    j1=0
    for x1 in l1:
        if(x1+l1[i1]==s1 and i1!=j1):
            
            c1=c1+1
            break
        j1=j1+1   
            
if (c1>0):
    print("YES")
else:
    print("NO")
