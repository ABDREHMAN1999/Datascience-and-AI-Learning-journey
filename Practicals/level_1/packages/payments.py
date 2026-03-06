##this file contains code to manage paymentss

class Storepayments:
    def __init__(self):
        print("Welcome to payments system: ")
        print("Press 1 for Add cash to the system")
        print("Press 2 to refund the money")
        print("Press 3 check balance")
        print("Press 4 to check the transcation")
        print("Press 5 to exit the system")
        user_input = int(input())
        self.__balance = 0
        self.__history = []
        if user_input == 1:
            self.AddCash(int(input("Enter the amount to be added: ")))
        elif user_input == 2:
            self.Refund(int(input("Enter the amount to be refunded")))
        elif user_input == 3:
            self.checkbalance()
        elif user_input == 4:
            self.gethistory()
        elif user_input == 5:
            print("Have a nice Day, Bye Bye")
        
        
    def AddCash(self, Amount):
        print("Do you want to use credit card? or UPI?")
        print("1 for credit card, 2 for UPI")
        option = input()
        if option == "1":
            print(f"you havse added Amount {Amount} rupees through credit card.")
        else:
            print(f"you havse added Amount {Amount} rupees through UPI.")
        self.__balance += Amount
        history = {"AddCash": Amount}
        self.__history.append(history)
    
    def Refund(self, Amount):
        if self.__balance >= Amount:
            print(f"Amount {Amount} will be refunded")
            self.__balance -= Amount
            history = {"Refund": Amount}
            self.__history.append(history)
        else:
            print("Cannot be refunded as no cash is added")
            
    def checkbalance(self):
        print(f"Current store balance is {self.__balance}")
        history = {"checkbalance": self.__balance}
        self.__history.append(history)
        
    def gethistory(self):
        print(f"Transaction history shown below: ")
        print(self.__history)
            

            
    
    

        