n11,m1=map(eval,input().split())
a1=[]
for i1 in range(n11):
  a1.append(list(map(eval,input().split())))
pos=[]
out=[]
temp_out=[]
t1=[]
i1=0
j1=0
out.append(a1[i1][j1])
pos.append([i1,j1])
while [n11-1,m1-1] not in pos:
  i1=0
  for x1 in pos:
    if x1[0]+1<n11 and x1[1]+1<m1:
      temp_out.append(a1[x1[0]+1][x1[1]]+out[i1])
      temp_out.append(a1[x1[0]][x1[1]+1]+out[i1])
      t1.append([x1[0]+1,x1[1]])
      t1.append([x1[0],x1[1]+1])
    elif x1[0]+1<n1:
      temp_out.append(a1[x1[0]+1][x1[1]]+out[i1])
      t1.append([x1[0]+1,x1[1]])
    elif x1[1]+1<m1:
      temp_out.append(a1[x1[0]][x1[1]+1]+out[i1])
      t1.append([x1[0],x1[1]+1])
    i1+=1
  pos=t
  t1=[]
  out=temp_out
  temp_out=[]
print(max(out))
