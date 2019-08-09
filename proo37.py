nt26=int(input())
lt26=list(map(int,input().split()))
ct26=0
it26=0
while(it26<len(lt26)):
    tt=lt26[it26]
    if(it26==0):
        if(len(lt26)==1):
            ct=1 
            break
    elif(it26==len(lt26)-1):
        ct=ct
    else:
        if(tt>lt26[it26+1] and tt>lt26[it26-1]):
            ct=ct+1
        elif(tt<lt26[it26-1] and tt<lt26[it26+1]):
            ct=ct+1
    it=it26+1
print(ct)
