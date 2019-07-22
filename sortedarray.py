size81=int(input())
arr31=[]
for i in range(size81):
	st1=input()
	st1=list(map(int,st1.split(" ")))
	lt1=len(st1)
	for j in range(lt1):
		arr31.append(st1[j])
arr31.sort()
print(*arr31,sep=" ")
