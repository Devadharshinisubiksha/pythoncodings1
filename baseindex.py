b12,t12 = map(int,input().split())
l123 = []
l223 = []
l123 = input().split()
for ic1 in range(len(l123)):
    l123[ic1] = int(l123[ic1])
for ic1 in range(t12):
    a22,b22 = map(int,input().split())
    res = 0
    for ic1 in range(a22-1,b22):
        res += l123[ic1]
    print(res)
