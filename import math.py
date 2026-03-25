m=input()
dem=len(m)-1
n=int(m)
b=0
so=["không","một","hai","ba","bốn","năm","sáu","bảy","tám","chín"]
hang=["","mươi","trăm","nghìn","mươi","trăm","triệu","mươi","trăm","tỷ","mươi","trăm","nghìn","mươi","trăm","triệu"]
while(dem+1>0):
    k=n//(10**(dem))
    n=n%(10**dem)
    k1=n//(10**(dem-1))
    if( n//(10**(dem-1))!=0 and k==0 and dem%3==1 ):
        print("linh",end=" ")
        print(so[n//(10**(dem-1))],end=" ")
        dem-=1
        if(dem>1):
            print(hang[dem],end=" ")
        n=n%(10**dem)
    elif( n//(10**(dem-1))==0 and k==0) :
        b=0
        while(n//(10**(dem-1))==0 and k==0 and dem>=0):    
            if(dem%3==0  and b==0):
                
                print(hang[dem])
                b=1
            if(dem==2 and n%10!=0):
                print(so[k])
                print(hang[dem],"linh")
            dem-=1
            n=n%(10**dem)
    elif( k==1 and (dem+1)%3==2):
        print("mười",end=" ")
        if(dem%3==1 and k1!=0):
            print(so[k1],end=" ")
        if(dem>1 and k!=1):
            print(hang[dem],end=" ")
        elif(dem>1):
            print(hang[dem-1],end=" ")
            dem-=1
            n=n%(10**dem)
        else:    
            dem-=1
            n=n%(10**dem)
    else:
        print (so[k],end=" ")
        print(hang[dem],end=" ")
    dem-=1