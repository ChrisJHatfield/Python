#1 Update Values in Dictionaries and Lists
#
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Bryant'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].

# print(x[1][0])
# x[1][0] = 15
# print(x[1][0])

# Change the last_name of the first student from 'Jordan' to 'Bryant'

# print(students[0]['last_name'])
# students[0]['last_name'] = 'Bryant'
# print(students[0]['last_name'])
# print(students)

# In the sports_directory, change 'Messi' to 'Andres'

# print(sports_directory['soccer'])
# sports_directory['soccer'][0] = 'Andres'
# print(sports_directory['soccer'])

# Change the value 20 in z to 30

# print(z[0]['y']) 
# z[0]['y'] = 30
# print(z[0]['y'])

#
#------------------------------------------------------------------------------------------------

#Iterate Through a List of Dictionaries
#
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

# def iterateDictionary(some_list):
#     for item in some_list:
#         print(f"first_name - {item['first_name']}, last_name - {item['last_name']}")

def iterateDictionary(students):

    for key, value in students[0].items():
        print('key: ', key)
        print('value: ', value)

# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# # first_name - Michael, last_name - Jordan
# # first_name - John, last_name - Rosales
# # first_name - Mark, last_name - Guillen
# # first_name - KB, last_name - Tonel
# #------------------------------------------------------------------------------------------------

# #3 Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, 
# the function prints the value stored in that key for each dictionary. 
# For example, iterateDictionary2('first_name', students) should output:

def iterateDictionary2(key_name, some_list):
    for item in some_list:
        print(item[key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

# #------------------------------------------------------------------------------------------------

# #4 Iterate Through a Dictionary with List Values
# # Create a function printInfo(some_dict) that given a dictionary whose values are all lists, 
# # prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    for key, values in dojo.items():
        print(len(values), key.upper())
        dojo_key_list = values
        i = 0
        while i < len(dojo_key_list):
            print(dojo_key_list[i])
            i +=1

printInfo(dojo)


# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon