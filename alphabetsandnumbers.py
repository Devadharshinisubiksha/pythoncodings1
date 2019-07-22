s=input()
u=0
b=0
for i in range(len(s)):
  if(s[i].isalpha()):
    u=u+1
  elif(s[i].isdigit()):
    b=b+1
  else:
    g=0
if u>=1 and b>=1:
  print("Yes")
else:
  print("No")
