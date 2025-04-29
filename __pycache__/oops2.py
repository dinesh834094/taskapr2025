'''from abc import ABC,abstractmethod
class payment(ABC):
    @abstractmethod
    def payment_processing(self):
        pass
class gpay(payment):
    def payment_processing(self,amount):
        print(amount)
class phonepay(payment):
    def payment_processing(self,amount):
        print(amount)'''


from abc import ABC, abstractmethod   
class Car(ABC): 
    @abstractmethod  
    def mileage(self):   
     pass  
class Tesla(Car):   
    def mileage(self):   
        print("The mileage is 30kmph")   
    def smartfeaturs(self):
        print("providing additional functionalities")
class Suzuki(Car):   
    def mileage(self):   
        print("The mileage is 25kmph ")   
class Duster(Car):   
    def mileage(self):   
        print("The mileage is 24kmph ")   
class Renault(Car):   
    def mileage(self):   
        print("The mileage is 27kmph ") 

t = Tesla()
t.mileage()
t.smartfeaturs()

s = Suzuki()
s.mileage()

d = Duster()
d.mileage()

r =Renault()
r.mileage()
     

        





   


    
    


                