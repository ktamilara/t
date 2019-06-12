n1=int(input())
l1=list(map(int,input().split(" ")))
ss1=max(l)
s1=[]
for i1 in range(len(l1)-1):
	ch1=True
	for j1 in range(i1+1,len(l1)):
		if l1[j1]>l[i1]:
			ch1=False
			break
	if ch1==True:
		s1.append(l1[i1])
s1.append(l1[len(l1)-1])
print(*s1)
print(ss1)
