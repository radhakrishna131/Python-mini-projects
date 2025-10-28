
class Bank:
    def __init__(self,name,account_no,number,balance=0):
        self.name=name
        self.account=account_no
        self.number=number
        self.balance=balance
    
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            return f"{amount} deposited successfully "
        else:
            return"Enter valid amount!"
        
    def withdraw(self,amount):
        if self.balance>amount>0:
            self.balance-=amount
            return f"{amount} withdrawn sucessful "
        else:
            return"enter valid amount!"
        
    def balance_enquiry(self):
        return f"The account balance is {self.balance}"

    
holder1=Bank("Radha",123456789,9876543210,500)
print(holder1.balance_enquiry())
print(holder1.deposit(200))
print(holder1.balance_enquiry())
print(holder1.withdraw(100))
print(holder1.balance_enquiry())
        
        