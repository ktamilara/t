a11,b1=map(int,input().split())
l1=[]
c1=0
k1=[]
for i1 in range(a11,b1+1):
        l1.append(bin(i1)[2::])
for i1 in range(0,len(l1)):
        k1.append(l1[i1].count("1"))

for i1 in range(0,len(k1)):
        if k1[i1]!=1 and k1[i1]!=2:
                for p1 in range(2,k1[i1]):
                        if k1[1]%p1==0:
                                break
                if p1==k1[i1]-1:
                        c1=c1+1
        elif k1[i1]==2:
                c1=c1+1
print(c1)
