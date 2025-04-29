# method overloading
'''class addition():
    def add(self,a,b):
        print(a,b)
    def sub(self,a,b):
        print(a,b)
obj= addition()
obj.sub('ram',20)'''

# method overiding

'''class addition():
    def add(self,a,b,c='none'):
        print(a,b,c)
    def add(self,a,b,c='none'):
        print(a,b,c)
obj= addition()
obj.add(10,20,30)
obj.add(10,20)
obj.add('ram','sita','lol')'''

'''class father():
    def details(self,a):
        print('this is father class')
        print(a)
class child(father):
    def details(self,a):
        super().details(1234)
        print('this is child class')
        print(a)
obj= child()
obj.details(100)'''

class grandfather():
    def __init__(self,a):
        self.a=a
        print(a)
class father(grandfather):
    def display (self):
       
        print(self.a)
obj= father(100)
obj.display()

        
        







    

            