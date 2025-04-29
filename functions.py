'''def add():
    a=int(input('enter number'))
    b=int(input('enter number'))
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a**b)
add()'''

'''def square():
    x=int(input('enter number'))
    print(x*x)
square()

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result'''
'''def maximum():
    a=[10,20,30]
    print(max(a))
maximum()

def reverse():
    s=('python')
    print(s[::-1])
reverse()

def is_prime():
    a= int(input('enter number'))
    if a%2!=0:
        print('prime')
    else:
        print('not prime')
is_prime()

def is_palindrome():
    a= input('enter name')
    if (a[::-1])==a:
        print('palindrome')
    else:
        print('not palindorome')
is_palindrome()'''

'''def fibonacci(n):
  
   if n<0:
     return 'enter a valid number'
   elif n==0 :
      return 0
   elif n==1:
      return 1
   else:
      return fibonacci(n-1) + fibonacci(n-2)
num= int(input('enter number'))
print(fibonacci(num))'''

'''def sum_of_squares(numbers):
 total=0
 for num in numbers:
   total+=num**2
 print(total)
my_list=[1,2,3,4,5]
print(sum_of_squares(my_list)) '''

def average(numbers):
 total=0
 for num in numbers:
  total= sum(numbers)
  count=len(numbers)
  avg=total/count
  print(avg)
my_list=[1,2,3,4]
print(average(my_list))
 




    



   




  





 

 



   


   

  


