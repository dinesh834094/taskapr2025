#print('welcomet to python life')
#a=20

#print(type(str(a)))
#print(type(a))
#a=(10)
#b=('ram')
#print(a)
#print(b)
'''print('*')
print('**')
print('***')
a=10 
print(id(a))
a=10
b=('ram')
c=50.2
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

list=['apple','banana','cherry','mango']
print(list[-3:-1])
list.insert(2,'dinesh')
print(list)
list2=['apple','banana','cherry','mango']
list.extend(list2)
print(list)
list2.append('sweet')
print(list2)
list.remove('apple')
print(list)
list=['apple','banana','cherry','mango']
for i in range(len(list)):
    print(list[i])

list=['apple','banana','cherry','mango']
list.sort()
print(list)
list.sort(reverse='true')
print(list)
list.copy()
print(list)

a=3+5j
print(type(a))
a=True
b=False
print(type(a))
print(type(b))
age=18
if age>18:
    print('you can vote ')
else:
    print('wait for age reaches to 18')
a=5+5j
b=10+12j
c=a+b
print(c)
a=('dinesh')
print(a)
#addition of two variables 
a=10
b=20
print(a+b)
a=[1,2.3,'ram']
print(a)
a={101,102,103}
print(a)
a='ram'
b='suresh'
print(3*(a+b))

a="python"
print(a)
a=10
b=('ram')
print(a)
print(b)

a=5.7
b= 10
print(type(int(a)))
print(type(str(b)))

a= int(input('enter age '))
print(a)

a=('*')
print(a)
print(3*(a))
print(4*(a))
print(5*(a))
print(6*(a))
print(7*(a))
a={
    'title: aaa',
    'author:bbb',
    'publicationyear:2025',
}
print(a)
#Write a python program that takes a string as input ( 35 ) and return
#float value.
a= int(input ('enter number'))
print(float(a))

a= input('dinesh')
b=input('reddy')
c= a+b
print(c)

a= int(input('enter age '))
print(a+5)

a= 100
b=35
print(a%b)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)'''
#a= (input('enter name '))
#b= int(input('enter age '))
#print(f'welcome {a}, thanks for coming visit agaain yor age is {b}  ')

'''a={
    'name': 'maggy',
    'product':'food',
    'quantity':'one packet',
    'price': 15
}
print(f'product name is {'name'}, the product is {'product'},and quantity ,price are {'quantity'},{'price'}')'''

'''a=[1,2,3,4,5,6,7,8,9,10]
print(int(input('enter number '))in a)'''

'''a=[1,2,3,4,5,6,7,8,9,10]
print(int(input('enter number ')) not in a)'''

'''length= int(input('enter number'))
breadth=int(input('enter number'))
area= length*breadth
print(area)'''

'''a= int(input('enter number '))
a+=10
print(a)

a= int(input('enter number '))
a-=10
print(a)
a= int(input('enter number '))
a/=10
print(a)'''

'''temperature = int(input('enter number '))
fahrenheit= temperature *9/5+32
print(fahrenheit)'''


'''p= int(input('enter number'))
t= int(input('enter number'))
r= int(input('enter number'))
si = p*t*r/100
print(si)'''

'''a= input('enter name')
b= input('enter name 2')
print(a+b)

#1 km = 0.62 miles 

km =int(input('enter number '))
miles = km *0.62 
print(miles)'''


'''number=10
for i in number:
    if i /7==0:
        print(i)'''


'''number= ['dinesh']
print(type(dict[number]))'''



# Supermarket Billing System

name = input("Enter Your Name: ")

items = {
    "apple": 20,
    "banana": 10,
    "grapes": 100,
    "bread": 50,
    "oil": 150,
    "eggs": 10,
    "sugar": 40,
    "panneer": 100,
    "maggie": 12,
}

cart = {}

while True:
    option = input("Press 1 for list of items, 2 to exit, or 3 to view your bill: ")
    
    if option == "2":
        print("Thank you for shopping!")
        break
    
    elif option == "1":
        print("\nAvailable Items:")
        for item, price in items.items():
            print(f"{item.upper()} - ₹{price}")
        
        cart_item = input("\nEnter the item you want to add to your cart: ").lower()
        if cart_item in items:
            qty = int(input(f"Enter quantity of {cart_item}: "))
            if cart_item in cart:
                cart[cart_item] += qty
            else:
                cart[cart_item] = qty
            print(f"{qty} x {cart_item} added to your cart.\n")
        else:
            print("Item not available. Please try again.\n")
    
    elif option == "3":
        if not cart:
            print("Your cart is empty!\n")
        else:
            print("\n------ BILL ------")
            print("Items   quantity   price")
            print("-"*25)
            total = 0
            for item, qty in cart.items():
                price = items[item]
                cost = price * qty
                print(f"{item.upper()}   x   {qty}   = ₹{cost}")
                total += cost
            print("------------------")
            print(f"Total Amount: ₹{total}")
          
            discount = 0
            if total >= 500:
                discount = total * 0.10  # 10% discount
                print("\nEligible for 10% discount.")
                grand_total = total - discount
                print(f"Final Amount: ₹{grand_total}")
                print("------------------\n")
    else:
        print("Invalid option. Please try again.\n")











       
       
    






