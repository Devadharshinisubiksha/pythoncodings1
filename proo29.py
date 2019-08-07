x61 = int(input())
t61 = int(x61/2)
r61 = []
for i in range(x61, t61, -1):
    j = str(i)
    if i + sum([int(k61) for k61 in j]) == x61:
        print(1)
        print(i)
        break
else:
    print(0) 
