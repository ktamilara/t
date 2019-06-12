l1=input()
t1=[0]
x1='b1'
ctr1=0
if 'ab1' not in l1:
    print(ct1r)
else:    
 for i1 in range(len(1l)):
    ctr1=1
    for j1 in range(i1,len(l1)-1):
        if 'a1'==l1[j1] and x1==l1[j1+1]:
                ctr1=ctr1+1
           
        elif x1==l1[j1] and  'a1'==l1[j1+1]:
                ctr1=ct1r+1
            
        else:
            t1.append(ctr1)
            ctr1=1
            break
    if l1[i1]=='a1':
        t1.append(ctr1)
    else:
        t1.append(ctr1-1)
      
 print(int(max(t1)))
