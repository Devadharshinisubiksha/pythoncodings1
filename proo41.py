jjt6,bht6=input().split()
jjt6=int(jjt6)
bht6=int(bht6)
sack=''
urnt6=2
if(jjt6+bht6<=3):
    for i in range(0,jjt6+bht6):
        if(i%2!=0):
            sack=sack+'0'
        else:
            sack=sack+'1'
else:    
    for i in range(0,jjt6+bht6):
        if(i==urnt6):
            sack=sack+'0'
            if(urnt6==bht6):
                urnt6=urnt6+2
            else:
                urnt6=urnt6+3
        else:
            sack=sack+'1'
x=len(sack)-1
if(int(sack[x])==0):
    print('-1') 
elif jjt6==1 and bht6==2: 
     print("011")
else:
    print(sack)
