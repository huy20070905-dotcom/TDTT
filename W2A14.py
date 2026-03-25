import math
import numpy
a=numpy.ones(10000001)
a[1]=0
a[0]=0
def sangnt(n):
    for i in range(2,int(math.sqrt(n))+1):
        if(a[i]==1):
            k=i*i
            while(k<=n):
                a[k]=0
                k=k+i
while(0==0):
    l,m=map(int,input().split())
    
    sangnt(m+1)
    dem=0
    for i in range(l,m+1):
        if(a[i]==1):
         dem+=i
        
    print(dem)