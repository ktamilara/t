n1,k1=map(int,input().split())
d1=[]
for i1 in range(n1):
	s11=set(map(int,input().split()))
	d1.append(s11)
c1=s11.intersection(*d1)
print(*c1)
