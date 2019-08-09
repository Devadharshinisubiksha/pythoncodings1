nint2,kint2=map(int,input().split())
Lt2=list(map(int,input().split()))
Ct2=0
for Xt in Lt2:
    if Xt<=(5-kint2):
        Ct2+=1
Gt=Ct2//3
print(Gt)
