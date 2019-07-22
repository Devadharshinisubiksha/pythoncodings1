nnnt1,mmmt1=list(map(int,input().split()))
lt1=list(map(int,input().split()))
lt1.sort(reverse=True)
ct1=0
for i in lt1:
    if mmmt1==0:
        break
    qt1=mmmt1 // i
    ct1+=qt1
    mmm1t=mmmt1-i*qt1
print(ct1)
