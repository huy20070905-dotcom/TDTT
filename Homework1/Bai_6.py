import math
a,b,c=map(int,input().split())
if(a<(b+c)) and (b<(a+c)) and (c<(a+b)):
    p = (a+b+c)/2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(round(s,1))
else :
    print("Khong phai 3 canh cua tam giac")