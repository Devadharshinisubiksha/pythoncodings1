b26,n26=map(int,input().split())
amu26=[]
for _ in range(b26):
	amu26.append(sorted(list(map(int,input().split()))))
for l in range(b26-1):
	for m in range(n26):
		for q in range(b26-l):
			if(amu26[l][m]>amu26[l+q][m]):
				amu26[l][m],amu26[l+q][m]=amu26[l+q][m],amu26[l][m]
for l in amu26:
	print(*l,sep=' ')  
