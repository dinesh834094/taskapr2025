numbers=[1,2,3,4]
new_list=[]
for num in numbers:
    result= num**2
    new_list.append(result)
    print(result)

result=(map(lambda num : num**2,numbers))
print(list(result))

numbers=[1,2,-7,3,4,-5,-6]
new_list=[]
def filter_positive(numbers):
    for num in numbers:
     if num>1:
      new_list.append(num)
      print(num)
filter_positive(numbers)

result= filter(lambda num:num>1,numbers)
print(list(result))

from functools import reduce
def calculate_factorial(n):
    if n==0 or n==1:
        return 1
    return n* calculate_factorial (n-1)
print(calculate_factorial(5))



result= reduce(lambda x,y:x*y,range(1,6))
print(result)


def count_vowels(string):
    count = 0
    for char in string:
        if char.lower() in 'aeiou':
            count += 1
    return count

text = "Python Programming"
print("Number of vowels:", count_vowels(text))




