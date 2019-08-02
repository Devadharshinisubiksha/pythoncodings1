def sub(subi): 
    m26 = len(subi) 
    sub = [1]*m26 
    for i in range (1 , m26): 
        for j in range(0 , i): 
            if subi[i] > subi[j] and sub[i]< sub[j] + 1 : 
                sub[i] = sub[j]+1
    maximum = 0
    for i in range(m26): 
        maximum = max(maximum , sub[i])  
    return maximum
ar1=int(input()) 
subi = list(map(int,input().split()))
print (sub(subi))
