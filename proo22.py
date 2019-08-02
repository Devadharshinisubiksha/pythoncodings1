n26=int(input())
aa26=list(map(int,input().split()))
p26=[]
q26=[]
for i in range(len(aa26)):
	if i%2==0:
		p26.append(aa26[i])
	else:
		q26.append(aa26[i])
s26=sum(p26)
r26=sum(q26)
if(s26>r26):
	print(s26)
else:
	print(r26)
