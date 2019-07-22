a13,p13=map(int,input().split())
c123=list(map(int,input().split()))
dc123=[]
for ic in range(p13):
  u,v=map(int,input().split())
  dc123=c123[u-1:v]
  print(min(dc123))
