x11,y11,z11=map(str,input().split())
z11=int(z11)
x11=sorted(x11)
y11=sorted(y11)
a11=max(len(x11),len(y11))
count=0
for r in range(a11):
    if x11[r]!=y11[r]:
        count=count+1
if count==z11:
    print("yes")
else:
    print("no")
    #i
