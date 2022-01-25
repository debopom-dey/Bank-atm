class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def check_balance(self):
        print("Your balance is 1000")
        return(' ')

    def withdrawl(self,amount):
        new_amount = 1000 - amount
        print("You have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(new_amount))
        return(' ')
card=input("Enter your card no.-")
pin=input("Enter your pin no.-")
William=Atm(card,pin)
print(William.check_balance())
amt=int(input("Enter the amount to be withdrawn-"))
print(William.withdrawl(amt))
