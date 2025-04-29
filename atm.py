'''def credit():
def withdrawl():
def balance():
def ministstement():
def exit():'''

balance=0


def credit():
  global balance
  amount=int(input('enter amount '))
  balance+= amount
  print(amount)
print(balance)
credit()

def withdrawl():
  global balance
  amount=int(input('enter number to be withdrawn'))
  if amount<=balance:
    balance-=amount
    print(amount)
    print(balance)
  else:
    print('insufficient funds')
withdrawl()

def exit_programme():
  obj= input('enter exit to exit from')
  if obj== 'exit':
    print('you are exited')
  else:
    print('enetr valid credentials')
exit_programme()



 

  



 



 



  

 

  
  
  
  
  
  




