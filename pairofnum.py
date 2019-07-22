np13=input()
a33=list(map(int,np13.split()))
k3=a33[1]
ha3=input()
flag=0
sa3=list(map(int,ha3.split()))
for i in range(0,len(sa3)-1):
	for j in range(i+1,len(sa3)):
		if sa3[i]+sa3[j]==k3:
			print("yes")
			flag=1
			break
	if flag==1:
		break
if flag!=1:
	print("no")
