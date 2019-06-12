s1=int(input())
l11=list(map(int,input().split()))
r1=1
l1=[]
for i1 in l11:
  r1=r1*i1
for i1 in l11:
  l1.append(r1//i1)
print(*l1)
