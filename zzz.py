n=int(input())
a=[]
maxx=0
so=100000000
for i in range(1,n+1):
    x=int(input())
    a.append(x)
for i in range(1,n):
    
    for j in range(i+1,n):
        if(a[j-1]%2==0):
            if(a[j]==a[j-1]/2):
                if(j-i+1>=maxx):
                    maxx=j-i+1
                    if(a[i]<so):so=a[i]
            else:break
        else:
            if(a[j]==3*a[j-1]+1):
                if(j-i+1>=maxx):
                    maxx=j-i+1
                    if(a[i]<so):so=a[i]
            else:break
if(so==100000000):
    print("can't find")
else:
    print(so,maxx)

