''' #1) Update Values in Dictionaries and Lists -------------------------------------------'''

# x = [[5, 2, 3], [10, 8, 9]]
# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'}
# ]
# sports_directory = {
#     'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer': ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [{'x': 10, 'y': 20}]

# # a)
# x[1][0] = 15
# print(x)

# # b)
# students[0]['last_name'] = 'Bryant'
# print(students)

# # c)
# sports_directory['soccer'][0] = 'Andres'
# print(sports_directory)

# # d)
# z[0]['y'] = 30
# print(z)

''' #2) Iterate Through a List of Dictionaries -----------------------------------------------'''

# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'},
#     {'first_name': 'Mark', 'last_name': 'Guillen'},
#     {'first_name': 'KB', 'last_name': 'Tonel'}
# ]


# def iterateDictionary(some_list):
#     for index in range(len(some_list)):
#         array = []
#         for k, v in some_list[index].items():
#             c = '{} - {}'.format(k, v)
#             array.append(c)
#         # print(f"{array[0]}, {array[1]}")
#         print(f'{array[0]}, {array[1]}')


# iterateDictionary(students)

# should output: (it's okay if each key-value pair ends up on 2 separate lines

# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

'''#3) Get Values From a List of Dictionaries ------------------------------------------------'''


# def iterateDictionary2(key_name, some_list):
#     for index in range(len(some_list)):
#         print(some_list[index][key_name])


# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)


''' 4) Iterate Through a Dictionary with List Values ------------------------------------------'''

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):
    for k, v in some_dict.items():
        listLength_title = f'{len(v)} {k.upper()}'
        print(listLength_title)
        for i in v:
            print(f'{i}')
        print('\n')


printInfo(dojo)
