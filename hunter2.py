n6=int(input())
ls6=list(map(int,input().split()))
ls6.sort()
ls6.reverse()
if ls6[0]==0:
    print(0)
else:
    for i in ls6:
        print(i,end='')
