stt16="dhoni"
stt26=input()
valt16=list(set(stt16)-set(stt26))
valt26=list(set(stt26)-set(stt16))
valt6=len(valt16)+len(valt26)
if valt6==0:
	print("yes")
else:
	print("no")
