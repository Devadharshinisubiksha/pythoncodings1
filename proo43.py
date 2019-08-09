import sys, string, math

nact26 = int(input())
Lact26 = [ int(x) for x in input().split()]
bht26 = []
dupli26 = []
sint26 = []
for i in range(1,nact26+1) :
    if i not in Lact26:
        bht26.append(i)
for i in Lact26 :
    if Lact26.count(i) > 1 and i not in dupli26 :
        dupli26.append(i)
for i in range(0,nact26) :
    if Lact26[i] in dupli26 :
        sint26.append(i)
cct = len(bht26)
for i in range(0,nact26) :
    if len(bht26) == 0 :
        break
    if i in sint26 :
        if i == sint26[0] :
            if bht26[0] < Lact26[i] :
                Lact26[i] = bht26.pop(0)
                sint26.pop(0)
            elif Lact26[i] in dupli26 :
                sint26.pop(0)
                dupli26.remove(Lact26[i])
            else :
                Lact26[i] = bht26.pop(0)
                sint26.pop(0)


print(cct)
print(*Lact26)
