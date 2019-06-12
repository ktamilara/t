s1=input()
l1=[0]
if "ab1" not in s1:
	print("0")
else:
	for i1 in range(len(s1)):
		c1=1
		for j1 in range(i1,len(s1)-1):
			if s1[j1]=="a1" and s1[j1+1]=="b":
				c1=c1+1
			elif s1[j1]=="b1" and s1[j1+1]=="a1":
				c1=c1+1
			else:
				l1.append(c1)
				c1=1
				break
		if s1[i1]=="a1":
			l1.append(c1)
		else:
			l1.append(c1-1)
	print(max(l1))
