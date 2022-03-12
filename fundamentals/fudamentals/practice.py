# x = 10
# myString = ["hi", "hi"]

# if x > 50:
#     print("bigger than 50")
# else:
#     print("smaller than 50")


# class EmptyClass:
#     pass


# for val in myString:
#     pass

# age = 35  # storing an int
# weight = 160.57  # storing a float

# empty_list = []
# ninjas = ['Rozen', 'KB', 'Oliver']
# print(ninjas[2]) 	# output: Oliver
# ninjas[0] = 'Francis'
# ninjas.append('Michael')
# print(ninjas)  # output: ['Francis', 'KB', 'Oliver', 'Michael']
# ninjas.pop()
# print(ninjas)  # output: ['Francis', 'KB', 'Oliver']
# ninjas.pop(1)
# print(ninjas)  # output: ['Francis', 'Oliver']

# empty_dict = {}
# new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
# # updates if the key exists, adds a key-value pair if it doesn't
# new_person['name'] = 'Jack'
# new_person['hobbies'] = ['climbing', 'coding']
# print(new_person)
# # output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
# w = new_person.pop('weight')  # removes the specified key and returns the value
# print(w)		# output: 160.2
# print(new_person)
# # output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}


# import random
# rand_num = random.randint(1, 10)

# total = 35
# user_val = "26"
# # total = total + user_val		# output: TypeError
# total = total + float(user_val)		# total will be 61

# print(total)

# first_name = "Zen"
# last_name = "Coder"
# age = 27
# print(f"My name is {first_name} {last_name} and I am {age} years old.")

# x = "hello world"
# print(x.title())
# # output:

# import math
# dog = ("Canis Familiaris", "dog", "carnivore", 12)

# dog = dog + ("domestic",)
# #result is...
# #("Canis Familiaris", "Dog", "carnivore", 12, "domestic")
# print(dog)


# def get_circle_area(r):
#     # Return (circumference, area) of a circle of radius r
#     c = 2 * math.pi * r
#     a = math.pi * r * r
#     return (c, a)


# print((get_circle_area(5)))
# weekend = {"Sun": "Sunday", "Sat": "Saturday"}  # literal notation
# capitals = {}  # create an empty dictionary then add values
# capitals["svk"] = "Bratislava"
# capitals["deu"] = "Berlin"
# capitals["dnk"] = "Copenhagen"
# print(weekend)
# print(capitals)

# (capitals["svk"])
# print(weekend["Sun"])
# print(capitals["svk"])

# context = {
#     'questions': [{'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'}, {'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'}, {'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
#                   {'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
#                   ]
# }

# print(context["questions"][0])
# print(context.values())

# for x in range(0, 10, 2):
#     print(x)
# # output: 0, 2, 4, 6, 8
# for x in range(5, 1, -3):
#     print(x)
# # output: 5, 2

# for x in 'Hello':
#     print(x)
# # output: 'H', 'e', 'l', 'l', 'o'

# my_list = ["abc", 123, "xyz"]

# for i in range(0, len(my_list)):
#     print(i, my_list[i])
# # output: 0 abc, 1 123, 2 xyz

# # OR

# for value in my_list:
#     print(value)
# # output: abc, 123, xyz

# my_dict = {"name": "Noelle", "language": "Python"}
# for k in my_dict:
#     print(k)
# # output: name, language

# my_dict = {"name": "Noelle", "language": "Python"}
# for k in my_dict:
#     print(my_dict[k])
# # output: Noelle, Python

# capitals = {"Washington": "Olympia", "California": "Sacramento", "Idaho": "Boise",
#             "Illinois": "Springfield", "Texas": "Austin", "Oklahoma": "Oklahoma City", "Virginia": "Richmond"}
# # another way to iterate through the keys
# for key in capitals.keys():
#     print(key)
# # output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
# # to iterate through the values
# for val in capitals.values():
#     print(val)
# # output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
# # to iterate through both keys and values
# for key, val in capitals.items():
#     print(key, " = ", val)
# # output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc
# for count in range(0, 5):
#     print("looping =", count)

# count = 0
# while count <= 5:
#     print("looping - ", count)
#     count += 1
# y = 3
# while y > 0:
#     print(y)
#     y = y - 1
# else:
#     print("Final else statement")
# for val in "string":
#     if val == "i":
#         break
#     print(val)
# # output: s, t, r

# y = 3
# while y > 0:
#     print(y)
#     y = y - 1
#     if y == 0:
#         break
# else:		# only executes on a clean exit from the while loop (i.e. not a break)
#     print("Final else statement")
# # output: 3, 2, 1
# from genericpath import exists


# x = ""
# y = 3

# if x not exists:
#     print('nothing here')
# else:
#     print("somthing here")
# def add(a, b):  # function name: 'add', parameters: a and b
#     x = a + b  # process
#     return x  # return value: x


# print(add(3, 4))

# def be_cheerful(name="Mr. Nibbles", repeat=2):
#     print(f"Good morning {name}\n" * repeat)


# be_cheerful("Tim")
# be_cheerful()
# be_cheerful(repeat=4, name="Benny Bob")
# set defaults when declaring the parameters
# def be_cheerful(name='', repeat=2):
#     print(f"good morning {name}\n" * repeat)


# be_cheerful()  # output: good morning (repeated on 2 lines)
# be_cheerful("tim")  # output: good morning tim (repeated on 2 lines)
# be_cheerful(name="john")  # output: good morning john (repeated on 2 lines)
# be_cheerful(repeat=6)  # output: good morning (repeated on 6 lines)
# # output: good morning michael (repeated on 5 lines)
# be_cheerful(name="michael", repeat=5)
# # NOTE: argument order doesn't matter if we are explicit when sending in our arguments!
# # output: good morning kb (repeated on 3 lines)
# be_cheerful(repeat=3, name="kb")
def multiply(num_list, num):
    for x in num_list:
        x *= num
    return num_list


a = [2, 4, 10, 16]
b = multiply(a, 5)
print(b)
