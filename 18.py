n1=int(input())
M11=[]
c1=0
for i1 in range(n1):
  M11.append(list(map(int,input().split())))
f1=0
for i1 in range(len(M11)):
  for j1 in range(len(M11[0])):
    f1=0
    if M11[i1][j1]==1:
      try:
        if M11[abs(i1-1)][j1]==0:
          f1+=1
      except IndexError:
        f1+=1
      try:
        if M1[i+1][j]==0:
          f+=1
      except IndexError:
        f+=1
      try:
        if M11[i1][abs(j1-1)]==0:
          f1+=1
      except IndexError:
        f1+=1
      try:
        if M11[i1][j1+1]==0:
          f1+=1
      except IndexError:
        f1+=1
      try:
        if M11[abs(i1-1)][abs(j1-1)]==0:
          f1+=1
      except IndexError:
        f1+=1
      try:
        if M11[abs(i1-1)][j1+1]==0:
          f1+=1
      except IndexError:
        f1+=1
      try:
        if M11[i1+1][abs(j1-1)]==0:
          f1+=1
      except IndexError:
        f1+=1
      try:
        if M11[i1+1][j1+1]==0:
          f1+=1
      except IndexError:
        f1+=1
    if f1==8:
      c1+=1

print(c1)
