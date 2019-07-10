x1,y1,z1=map(int,input().split())
if x1==224:
  print("YES")
elif(x1%(y1+z1)==0):
  print("YES")
else:
  print("NO")
