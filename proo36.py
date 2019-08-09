Pt26 = int(input())
Qt26 = [ int(i) for i in input().split()]
Pt26 = len(Qt26)
Ut26 = 0
for Xt in range(0,Pt26-2):
    for Yt in range(Xt+1, Pt26-1):
        for Zt in range(Yt+1, Pt26):
            if Qt26[Xt] > Qt26[Yt] > Qt26[Zt] :
                Ut26 =Ut26+ 1
print(Ut26)
