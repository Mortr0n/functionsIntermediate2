# 1. Update Values in Dictionaries and Lists
# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]
# copy
# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30


# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# x[1][0]=15
# print(x)



# # for x in students:
# #     for y in x:
# #         if x.get(y) == 'Jordan':
# #             x.update({y: "Bryant"})  I looked up a much more complicated way of doing this at first.  
# #                                       this will come in handy for future items though
# # for arrList in students:
# #     print(arrList)
# #     for keyItem in arrList:
# #         print(keyItem)               Further playing to learn how to use these better 
# #                                       and understand what was happening.
# students[0]["last_name"]='Bryant'
# print(students[0]["last_name"])


# 2. Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, 
# the function loops through each dictionary in the list and prints each key and the 
# associated value. For example, given the following list:

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

dogs = [
    {'Breed': 'Aussie', 'color': 'blue-merle'},
    {'Breed': 'Doberman', 'color': 'black and brown'},
    {'Breed': 'Golden retriever', 'color': 'golden'},
    {'Breed': 'Australian Shepperd', 'color': 'red merle'}
]

# def iterateDictionary(someList):
#     count = 0
#     for items in someList:
#         for keyItem in items:
#             if(count%2!=0):         #Begin code that will probably win award for most convoluted way to do something
#                 print(storeItem, keyItem, ' - ', items[keyItem]) 
#             storeItem = keyItem + ' - ' + items[keyItem] + ', '
#             count+=1

# iterateDictionary(students)
# iterateDictionary(dogs)

# iterateDictionary(students) 
# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# 3. Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name,
# the function prints the value stored in that key for each dictionary. For example, 
# iterateDictionary2('first_name', students) should output:


# def iterateDictionary2(keyVal, someList):
#     for i in someList:
#         print(i[keyVal])
# def iterateDictionary2(keyVal, someList):  
#     for i in someList:
#         print(i.get(keyVal))

# iterateDictionary2('first_name', students)
# iterateDictionary2('Breed', dogs)
# iterateDictionary2('last_name', students)


# 4. Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, 
# prints the name of each key along with the size of its list, and then prints the associated 
# values within each key's list. For example:

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(someDict):
    for arrList in someDict:
        print(len(someDict[arrList]), arrList)
        for listings in dojo[arrList]:
            print(listings)

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
