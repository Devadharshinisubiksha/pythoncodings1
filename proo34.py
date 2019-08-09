b26,n26=map(int,input().split())
amu26=0
Liee14=[]
for w in range(b26):
      Liee14.append(input())
for w in range(b26):
      for q in range(n26-1):
            if(Liee14[w][q]!='R' and Liee14[w][q+1]!='R'):
                  amu26+=3
            elif(Liee14[w][q]!='G' and Liee14[w][q+1]!='G'):
                  amu26+=5
print(amu26)
