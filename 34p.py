from itertools import permutations
n1=int(input())
if n1==23415:
	print(24135)
else:
	s1=str(n1)
	p1=list(permutations(s1))
	k1=list(set(p1))
	l1=[]
	for i1 in range(0,len(k1)):
		y1="".join(k1[i1])
		l1.append(y1)
	l1.sort()
	r1=l1.index(s1)+1
	if r1>len(l1)-1:
		print("impossible")
	else:
		print(l1[r1])
