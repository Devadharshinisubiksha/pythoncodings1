arrt6=int(input())
brrt6=[int(st) for st in input().split()]
brrt6.sort()
st6=0
xvt6=0
for i in range(len(brrt6)):
    if brrt6[i]>=st6:
        xvt6+=1
    st6=st6+brrt6[i]
print(xvt6)
