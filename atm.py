class Atm:
    def __init__(self, cardNumber, pinNumber):
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber
        
    def CheckBalance(self):
        print("Your balance is 10000000")

    def Withdrawl(self, amount):
        newAmount=10000000-amount
        print("you have withdrawn " +str(amount) +"the remaining balance is " +str(newAmount))

def main():
    card_number=input("insert your card number")
    pin_number=input("insert your pin number")

    newUser=Atm(card_number,pin_number)

    print("choose your activity 1.Balace inquiry 2.Withdrawl")
    activity=int(input("enter the activity number:- "))

    if(activity==1):
        newUser.CheckBalance()
    elif(activity==2):
        amount=int(input("enter the amount"))
        newUser.Withdrawl(amount)
    else:
        print("enter a valid number")
    
main() 


