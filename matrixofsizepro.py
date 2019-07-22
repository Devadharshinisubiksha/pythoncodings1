aprt1,brt1=map(int,input().split())
l1t1=[]
for _ in range(aprt1):
    l1t1.append(input())
for ic in range(len(l1t1)):
    if('0' in l1t1[ic]):
        l1t1[ic]=l1t1[ic].replace('0','')
    l1t1[ic]=l1t1[ic].replace(' ','')
lengths=[]
for ic in l1t1:
    if(len(ic)>0):
        lengths.append(len(ic))
brt=min(lengths)
rt11='1 '*brt
rt11=rt11.strip()
for ic in range(brt):
    print(rt11)
