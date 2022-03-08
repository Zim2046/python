# ''' #1) Update Values in Dictionaries and Lists '''
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

''' #2) Iterate Through a List of Dictionaries'''
from array import array
from cgi import print_arguments


students = [
    {'first_name':  'Michael', 'last_name': 'Jordan''middle_name':},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

'''#3 Get Values From a List of Dictionaries'''


def iterateDictionary(some_list):
    for index in range(len(some_list)):
        array = []
        for k, v in some_list[index].items():
            a = "{}".format(k)
            b = "{}".format(v)
            c = '{} - {}'.format(a, b)
            array.append(c)
        # print(f"{array[0]}, {array[1]}")
        print('{}, {}'.format(array[0], array[1]))


iterateDictionary(students)

# should output: (it's okay if each key-value pair ends up on 2 separate lines;

# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
