bt16,bt26,bt36,bt46=map(int,input().split())
lissc=list(map(int,input().split()))
xen=[]
for i in range(0,len(lissc)):
    for j in range(i,len(lissc)):
        for k in range(j,len(lissc)):
            xen.append(bt26*lissc[i]+bt36*lissc[j]+bt46*lissc[k])
print(max(xen))
