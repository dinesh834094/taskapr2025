dictionary={}

while True:
    print('\n data management system')
    print('1.add word')
    print('2.search for meaning')
    print('3.display all words')
    print('4.update meaning')
    print('5.delete word')
    print('6.exit')

    choice=(input('enter number'))

    if choice=='1':
        word= input('enter word').lower()
        meaning= input('enter meaning')
        dictionary[word]= meaning
    
    elif choice =='2':
        word= input('enter word').lower()
        if word in dictionary:
            print('meaning:',dictionary[word])
        else:
            print('the word is not there')

    elif choice=='3':
        if dictionary:
            for word , meaning in dictionary .items():
             print(f'{word}:{meaning}')
        else:
             print('empty')

    elif choice=='4': 
        word= input('enter the word to update').lower() 
        if word in dictionary:
            meaning = input(('enter the meaning'))
            dictionary[word]= meaning
            print(dictionary[word])
        else:
            print('empty')
    elif choice=='5':
            word= input('enter word').lower()
            if word in dictionary:
                del dictionary[word]
            else:
             print('not found')

    elif choice=='6':
            print('exit')
            break
    else:
        print('enter valid credentials')
                    
                    


'''my_dict = {'name': 'python', 'age': 25}
my_dict1= my_dict['state']='telangana'
print(my_dict)

product_info = {'name': 'Laptop', 'brand': 'Dell', 'price': 1200}
product_info1= product_info.get('price')
print(product_info1)

my_dict = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}
my_dict1= my_dict.pop('city')
print(my_dict)

my_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'}
my_dict1= my_dict.keys()
print(my_dict1)

my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
my_dict1= my_dict.values()
print(my_dict1)'''

# Write a Python script that updates a dictionary with a new key-value pair

'''my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
my_dict1= my_dict['city']= 'sangareddy'
print(my_dict)

# Write a Python script that accesses and prints the value associated with a specific key in a dictionary.
my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
my_dict1= my_dict.get('name')
print(my_dict1)'''



        
  
       



    
        

