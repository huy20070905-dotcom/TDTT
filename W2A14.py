class Student:
    def __init__(self,ten):
        self.ten=ten
        self.diem=[]
    def add_score(self,diem):
        self.diem.append(float(diem))
    def avg(self):
        return sum(self.diem)/len(self.diem)
    def rank(self):
        tb=self.avg()
        if(tb>=8.0):
            return "ẽilent"
        else:
            return"ngu"
s=input()
n=int(input())
hocsinh=Student(s)
for i in range(n):
    sub,diem=input().strip().split()
    hocsinh.add_score(diem)
print(hocsinh.avg(),hocsinh.rank())

    

