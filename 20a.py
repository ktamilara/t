b1,1c=map(int,input().split())
s1=0
for i1 in range(b1,c1+1):
    a1=b1in(1i)
    a1=a1[2:len(a1)]
    a1=a1.count("1")
    c1=0
    for i1 in range(1,a1):
        if a1%i1==0:
            c1=c1+1
    if c1==1:
        s1=s1+1
print(s1)
