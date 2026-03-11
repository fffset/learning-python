x=5 #integer variable
y=3.14 #float variable
z="Hello, World!" #string variable
c=2+3j #complex variable
is_valid=True #boolean variable
myList=[1, 2, 3, 4, 5] #list variable
myTuple=(1, 2, 3) #tuple variable
mySet={1, 2, 3} #set variable
myDict={"name": "Alice", "age": 30} #dictionary variable


print('x:', x)
print('y:', y)
print('z:', z)
print('c:', c)
print('is_valid:', is_valid)
print('myList:', myList)
print('myTuple:', myTuple)
print('mySet:', mySet)
print('myDict:', myDict)

#Operations
#MATH OPERATIONS
sum_result = x + y
difference = x - y
product = x * y
quotient = x / y
mod= x % y
power= x ** 2
even=15//2
print('Sum:', sum_result)
print('Difference:', difference)
print('Product:', product)
print('Quotient:', quotient)
print('Modulus:', mod)
print('Power:', power)
print('Even Division:', even)

#COMPARISON OPERATIONS
is_equal = x == y
is_not_equal = x != y
is_greater = x > y
is_less = x < y
is_greater_equal = x >= y
is_less_equal = x <= y
print('Is Equal:', is_equal)
print('Is Not Equal:', is_not_equal)
print('Is Greater:', is_greater)
print('Is Less:', is_less)
print('Is Greater or Equal:', is_greater_equal)
print('Is Less or Equal:', is_less_equal)

#LOGICAL OPERATIONS
and_result = is_valid and (x > 0)
or_result = is_valid or (x < 0)
not_result = not is_valid
print('AND Result:', and_result)
print('OR Result:', or_result)
print('NOT Result:', not_result)

#ASSIGNMENT OPERATIONS
x += 2 # x = x + 2
y *= 2 # y = y * 2
y /= 2 # y = y / 2
x -= 1 # x = x - 1
print('Updated x:', x)
print('Updated y:', y)

#CONDITIONAL STATEMENTS
if x > 5:
    print('x is greater than 5')
elif x == 5:
    print('x is equal to 5')
else:
    print('x is less than 5')

#LOOPS
#FOR LOOP
print('For Loop:')
for i in range(5):
    print(i)

#WHILE LOOP
print('While Loop:')
count = 0
while count < 5:
    print(count)
    count += 1  

my_str = 'Hello world'

print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)    # False
print('e' in my_str)  # True
print('f' in my_str)  # False

print(len(my_str))  # 11

print(my_str[0])  # H
print(my_str[6])  # w

print(my_str[-1])  # d
print(my_str[-2]) # l

greeting = 'hi'
greeting = 'hello'
print(greeting) # hello

name = 'John Doe'
age = 26

name_and_age = name + str(age)
print(name_and_age) # John Doe26


name = 'John Doe'
age = 26
name_and_age = f'My name is {name} and I am {age} years old'
print(name_and_age) # My name is John Doe and I am 26 years old



num1 = 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}') # The sum of 5 and 10 is 15


my_str = 'Hello world'
print(my_str[1:4]) # ell


my_str = 'Hello world'
print(my_str[:7])  # Hello w


my_str = 'Hello world'
print(my_str[8:])  # rld

#string[start:stop:step]
my_str = 'Hello world'
print(my_str[0:11:2])  # Hlowrd


my_str = 'Hello world'
print(my_str[::-1]) # dlrow olleH


my_str = 'hello world'

uppercase_my_str = my_str.upper()
print(uppercase_my_str)  # HELLO WORLD


my_str = 'Hello World'

lowercase_my_str = my_str.lower()
print(lowercase_my_str)  # hello world


my_str = '  hello world  '

trimmed_my_str = my_str.strip()
print(trimmed_my_str)  # "hello world"


my_str = 'hello world'

replaced_my_str = my_str.replace('hello', 'hi')
print(replaced_my_str)  # hi world


my_str = 'hello world'

split_words = my_str.split()
print(split_words)  # ['hello', 'world']


my_list = ['hello', 'world']

joined_my_str = ' '.join(my_list)
print(joined_my_str)  # hello world


my_str = 'hello world'

starts_with_hello = my_str.startswith('hello')
print(starts_with_hello)  # True


my_str = 'hello world'

ends_with_world = my_str.endswith('world')
print(ends_with_world)  # True


my_str = 'hello world'

world_index = my_str.find('world')
print(world_index)  # 6


my_str = 'hello world'

o_count = my_str.count('o')
print(o_count)  # 2


my_str = 'hello world'

capitalized_my_str = my_str.capitalize()
print(capitalized_my_str)  # Hello world


my_str = 'hello world'

is_all_upper = my_str.isupper()
print(is_all_upper)  # False


my_str = 'hello world'

is_all_lower = my_str.islower()
print(is_all_lower)  # True


my_str = 'hello world'

title_case_my_str = my_str.title()
print(title_case_my_str)  # Hello World


#Employee Information EXAMPLE
first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name
address = '123 Main Street'
address += ', Apartment 4B'
employee_age = 28
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)
years_experience = 5
experience_years = 5
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)
position = 'Data Analyst'
salary = 75000
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)
employee_code = 'DEV-2026-JD-001'
department = employee_code[0:3]
print(department)
year_code = employee_code[4:8]
print(year_code)
initials = employee_code[9:11]
print(initials)

last_three=employee_code[-3:]
print(last_three)



# BILL SPLITTING EXAMPLE
running_total = 0

num_of_friends = 4

appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

running_total += appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)

tip = running_total * 0.25
print('Tip amount:', tip)

running_total += tip
print('Total with tip:', running_total)

final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)

each_pays=round(final_bill,2)
print('Each person pays:',each_pays)