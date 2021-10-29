import datetime
import pytz

class Account:

    """ simple class with balance """

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self,name,balance):
        self._name = name
        self._balance = balance
        self._transaction_list = [(Account._current_time(),balance)]
        print("Account created for "+ self._name)


    def deposit(self,amount):
        if amount > 0:
            self._balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(),amount))
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self._transaction_list.append((Account._current_time(),-amount))
    
        else:
            print("The amount should be greater than zero and no more than your account balance")
        self.show_balance()

    def show_balance(self):
        print("balance is {} ".format(self._balance))

    def show_transactions(self):
        for date,amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposits"
            else:
                tran_type = "withdraw"
                amount *= -1 #-ve amount show amount withdraw
            print("{} {} on {} (local time was {} )".format(amount,tran_type,date,date.astimezone()))

if __name__ == '__main__':
    tim = Account("tim",50)
    tim.show_balance()
    tim.deposit(500)
    tim.withdraw(100)
    tim.show_transactions()
    
    