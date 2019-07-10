v1,m1=map(str,input().split())
gh1=0
if len(v1)>len(m1):
  v1,m1=m1,v1
c1=0
while c1<len(v1):
  gh1+=(ord(m1[c1])-ord(v1[c1]))
  c1+=1
for c1 in range(c1,len(m1)):
  gh1+=ord(m1[c1])-ord('a')+1
print(gh1)
