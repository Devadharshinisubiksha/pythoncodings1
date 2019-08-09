import sys, string, math

subi = input()
if subi == subi[::-1] :
    print('yes')
    sys.exit()
barathi = 0
for cust in subi[::-1] :
    if cust == '0' :
        barathi += 1
    else :
        break
sopt = '0'*barathi + subi

if sopt== sopt[::-1] :
    print('yes')
else :
    print('no')
