q1=int(input())
w1=[]
for h1 in range(0,q1):
 pan=input()
 w1.append(pan)
ven1=[]
for h1 in zip(*w1):
 if(h1.count(h1[0])==len(h1)):
  ven1.append(h1[0])
 else:
  break
print(''.join(ven1))
