def mul(l1):
    re1=1
    for x1 in l1:
        re1=re1*x1
    return re   
r1=int(input())
s1=list(map(int,input().split()))
f1=[]
f1.append(mul(s1))
for i1 in range(0,r1-1):
  a1=s1[:i1+1]
  y1=s1[i1+1:]
  if mul(a1)>mul(y1):
    f1.append(mul(a1))
  else:
    f1.append(mul(y1))
print(max(f1))
