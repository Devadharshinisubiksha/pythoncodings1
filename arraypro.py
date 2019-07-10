num1=int(input())
array=list(map(int,input().split()))
b1=0
for n1 in range(len(array)-2):
    for i in range(n1+1,len(array)-1):
        for l in range(i+1,len(array)):
            if array[n1]<array[i]<array[l] and n1<i<l:
                b1=b1+1
print(b1)
