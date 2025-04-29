class laptop():
    def __init__(self,size,bn,colour,ram):
        self.size= size
        self.bn= bn
        self.colour=colour
        self.ram=ram
    def specs(self):
         print(f"Size of laptop is {self.size}\"")
         print(f"Brand name: {self.bn}")
         print(f"Colour: {self.colour}")
         print(f"RAM: {self.ram} GB")
class gaminglaptop(laptop):
    def __init__(self,size,bn,colour,ram,processor):
        super().__init__(size,bn,colour,ram)
        self.processor= processor
    def specs(self):
        print(f'the processor is{self.processor}')

    
obj= laptop(15,'lenovo','white',8)
obj.specs() 
print()

obj1=laptop(15,'apple','red',9)
obj1.specs()
print()
obj2=gaminglaptop(15,'lenovo','white',8,'intel')
obj2.specs()




class BankAccount:
    def __init__(self):
        self.balance = 0  # Initial balance

    def credit(self):
        amount = int(input("Enter amount to deposit: "))
        self.balance += amount
        print(f"Credited: {amount}")
        print(f"Current Balance: {self.balance}")

    def withdrawal(self):
        amount = int(input("Enter amount to withdraw: "))
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
            print(f"Remaining Balance: {self.balance}")
        else:
            print("Insufficient funds!")

    def exit_program(self):
        choice = input("Type 'exit' to exit: ")
        if choice.lower() == 'exit':
            print("You have exited the program.")
        else:
            print("Invalid input. Program still running.")


account = BankAccount()

account.credit()
account.withdrawal()
account.exit_program()

        





    
   



    

