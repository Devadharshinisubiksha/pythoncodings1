nnt26,mmt26=map(int,input().split())
lt26=[]
for _ in range(nnt26):
	lt26.append(sorted(list(map(int,input().split()))))
for i in range(nnt26-1):
	for j in range(mmt26):
		for k in range(nnt26-i):
			if(lt26[i][j]>lt26[i+k][j]):
				lt26[i][j],lt26[i+k][j]=lt26[i+k][j],lt26[i][j]
for i in lt26:
	print(*i,sep=' ')     
