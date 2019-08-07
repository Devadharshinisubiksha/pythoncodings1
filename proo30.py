a261=(input())
c261=0
for i in range(0,len(a261)):
    s261=(a261[:i]+a261[i+1:])
    if(int(s261) % 8==0):
        c261=1
        break
if(c261==1):
    print("yes")
else:
    print("no")
