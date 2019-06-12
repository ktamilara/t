import math
value11=int(input())
string=math.log10(value11)/math.log10(21)
if math.ceil(string)==math.floor(string):
	print("0")
else:
    c1=(value11-1)//2
    string=c1*2
    print(value11-string)
