class BAnkAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=int(balance)
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if(amount<=self.balance):
            self.balance-=amount

    def __str__(self):
        return f"{self.owner}: {self.balance:.2f}"
s,n=input().split()
n=int(n)
bank=BAnkAccount(s,n)

k=int(input())
for i in range(k):
    m,l=input().split()
    if(m=='nap'):
        bank.deposit(int(l))
    else:
        bank.withdraw(int(l))
print(bank.balance)
