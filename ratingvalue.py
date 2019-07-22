dn12=int(input())
lsi12=list(map(int,input().split()))
an=[1]*dn12
for i in range(dn12):
    if(i==0):
        if(lsi12[i]>lsi12[i+1]):
            an[i]=an[i]+an[i+1]
    elif(i>0):
        if(lsi12[i]>lsi12[i-1]):
            an[i]=an[i]+an[i-1]
print(sum(an))
