x26=input()
l26=list(map(int,input().split()))
max=0
j=0
while(j<len(l26)-1):
    count=0
    while(j<len(l26)-1 and l26[j]<l26[j+1]):
        count+=1
        j+=1
    if(count>max):
        max=count
    j+=1
print(max+1)
