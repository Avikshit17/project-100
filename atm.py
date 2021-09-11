class Atm():
    def __init__(self,name,balance,pin):
        self.name=name
        self.balance=balance
        self.pin=pin
    def displayBalance(self):
        print("Balance= "+str(self.balance))
    def dipositMoney(self):
        a=int(input("Enter the Amount you want to deposit "))
        self.balance=self.balance+a
        print(self.balance)
    def withdrawMoney(self):
        s=int(input("Enter the amount you want to withdraw "))
        if(s>self.balance):
            print("insuffisiant balance")
        else:
            self.balance=self.balance-s
            print("Amount left= "+str(self.balance))
    def changePin(self):
        d=int(input("enter the new pin "))
        self.pin=d
        print(self.pin)
customer1=Atm("Customer1",2000,1234)
customer2=Atm("customer2",5000,7890)
customer1.displayBalance()
customer1.dipositMoney()
customer1.withdrawMoney()


    

