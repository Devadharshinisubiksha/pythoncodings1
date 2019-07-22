ct21=int(input())
dt1=list(map(int,input().split(" ")))
dt1=[bin(i) for i in dt1]
dt1.sort(reverse=True)
dt1=[int(ct2,2) for ct2 in dt1]
for i in range(0,ct21):
     print(dt1[i])
