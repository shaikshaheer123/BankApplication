class BankApplication:
    bank_name = "SBI"

    def __init__(self, name, account_number, age, mobile_number, balance):
        self.name = name
        self.account_number = account_number
        self.age = age
        self.mobile_number = mobile_number
        self.balance = balance

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            return f"Transaction Successful. Collected {amount}"
        else:
            return "Insufficient Balance"

    def deposit(self, amount):
        self.balance += amount
        return f"Deposit Successful. Total Balance: {self.balance}"

    def update_mobile(self, new_number):
        self.mobile_number = new_number
        return f"Mobile number updated: {self.mobile_number}"

    def check_balance(self):
        return f"Total Account Balance: {self.balance}"


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




