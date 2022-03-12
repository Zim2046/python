#  variable declarations

num1 = 42
num2 = 2.3
boolean = True
string = 'Hello World'
# - Data Types


#         - Numbers
#         - Strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']

'''- Dictionary
    - initialize'''
person = {'name': 'John', 'location': 'Salt Lake',
          'age': 37, 'is_balding': False}
''' - Tuples
        - initialize'''
fruit = ('blueberry', 'strawberry', 'banana')  # - Tuples

#   - log statement- type check
print(type(fruit))

'''- List
- access value
- log statement'''
print(pizza_toppings[1])

'''- List
 - add value
- log statement'''
pizza_toppings.append('Mushrooms')

'''- Dictionary- access value- log statement- change value'''
print(person['name'])
person['name'] = 'George'
person['eye_color'] = 'blue'

''' - Tuples   - access value- log statement'''
print(fruit[2])

'''- conditional    - if   - else- Booleanlog statement- log statement'''
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

#        - Boolean- length check- conditional - if - else if- else- log statement
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")


'''- for loop
   - start
    - stop
    - increment
    - sequence
    - log statement'''
for x in range(5):
    print(x)
for x in range(2, 5):
    print(x)
for x in range(2, 10, 3):
    print(x)
x = 0

'''- while loop
   - start
    - stop
    - increment '''
while(x < 5):
    print(x)
    x += 1

'''        - List
            - delete value'''
pizza_toppings.pop()
pizza_toppings.pop(1)


'''        - List
            - access value
            - delete value
            - log statement'''
print(person)
person.pop('eye_color')
print(person)

'''           
            - access value
            - change value
            - add value
            - delete value
            - Boolean
            - continue
            - log statement
            - conditional
            - if
            - Strings
             - break'''
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

'''- function
    - log statement
    - for loop
'''


def print_hello_ten_times():
    for num in range(10):
        print('Hello')


print_hello_ten_times()

'''- function
    - log statement
    - for loop
    - argument
    - parameter
'''


def print_hello_x_times(x):
    for num in range(x):
        print('Hello')


print_hello_x_times(4)

'''- function
    - log statement
    - for loop
    - argument
    - parameter
'''


def print_hello_x_or_ten_times(x=10):
    for num in range(x):
        print('Hello')


print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)  # - argument

# - comment
#    - single line
#     - multiline
"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
