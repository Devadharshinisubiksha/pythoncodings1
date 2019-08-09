import sys,string


def maxOfSegmentMins(Lact26, nect26, kint26):
    if kint26 == 1:
        return min(Lact26)
    if kint26 == 2 :
        return max(Lact26[0], Lact26[nect26 - 1])
    return max(Lact26)

nect26,kint26 = input().split()
nect26,kint26 = int(nect26),int(kint26)
Lact26 = [ int(x) for x in input().split()]
nect26 = len(Lact26)
ans = maxOfSegmentMins(Lact26, nect26, kint26)
print(ans)
