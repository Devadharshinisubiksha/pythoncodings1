num1=input()
A1=0
for i in range(len(num1)):
	if(num1[i].isdigit() or num1[i].isalpha() or num1[i]==(" ")):
		continue
	else:
	    A1+=1
print(A1)	
