vm1=int(input())
p1=[]
dif1=0
for g1 in range (0,vm1+1):
    dif1=abs((2**g1)-vm1)
    p1.append(dif1)
sd1=min(p1)
print(sd1)
