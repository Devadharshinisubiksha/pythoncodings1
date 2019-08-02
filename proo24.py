a256=int(input())
b256=pow(2,a256)
z256=[]
for i in range(b256):  
    m256=bin(i).replace("0b","")
    z256.append(m256.zfill(a256))
    z256.sort(key=(lambda x:x.count('1')))
for i in z256:
    print(i)
