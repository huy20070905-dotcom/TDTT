a=input("Ten chu ho: ")
b=int(input("Chi so thang truoc: "))
c=int(input("Chi so thang nay: "))
print("Ho va ten:",a)
if(0<=(c-b)<=50):
    b1=(c-b)*1984
    print("Tien phai tra la:",f"{b1*(1+0.08):.0f}")
if(51<=(c-b)<=100):
    b2=(c-b-50)*2050
    print("Tien phai tra la:",f"{(50*1984+b2)*(1+0.08):.0f}")
if(101<=(c-b)<=200):
    b3=(c-b-100)*2380
    print("Tien phai tra la:",f"{(50*1984+50*2050+b3)*(1+0.08):.0f}")
if(201<=(c-b)<=300):
    b4=(c-b-200)*2998
    print("Tien phai tra la:",f"{(50*1984+50*2050+100*2380+b4)*(1+0.08):.0f}")
if(301<=(c-b)<=400):
    b5=(c-b-300)*3350
    print("Tien phai tra la:",f"{(50*1984+50*2050+100*2380+100*2998+b5)*(1+0.08):.0f}")
if((c-b)>=401):
    b6=(c-b-400)*3460
    print("Tien phai tra la:",f"{(50*1984+50*2050+100*2380+100*2998+100*3350+b6)*(1+0.08):.0f}")