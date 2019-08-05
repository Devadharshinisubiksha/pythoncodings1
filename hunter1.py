try:
	n6=int(input())
	array=list(map(int,input().split()))
	pk6=[]
	for i in array:
		if array.count(i)>1:
			if i not in pk6:
				pk6.append(i)
	print(*pk6)
	if len(pk6)==0:
		print("unique")
except ValueError:
	print("invalid")
