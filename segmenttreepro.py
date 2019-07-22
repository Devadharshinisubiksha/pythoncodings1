nn131,nn231=list(map(int,input().split()))
li11=list(map(int,input().split()))
li21=[]
while(nn231):
	k = list(map(int,input().split()))
	li21.append(k)
	nn231-=1
for ic1 in li21:
	val=0
	for jc1 in range(ic1[0]-1,ic1[1]):
		val=val^li11[jc1]
	print(val)
