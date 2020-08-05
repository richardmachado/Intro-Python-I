# # all of the even numbers 0-100 in a list

# evens1 = []

# for i in range(101):
#     # check for even numnbers
#     if i % 2 == 0:
#         # if it is, add it to the evens list
#         evens1.append(i)

# print(evens1)

# evens = [i for i in range(101) if i % 3 == 0]
# print(evens)

#create a list of numbers in the range 1-10

# squares = []

# for i in range(1, 11):
#     squares.append(i**2) 
# print(squares)

# squares2 = [i**2 for i in range(1, 11)]
# print(squares2)
# print (squares == squares2)

# names = ["Sarah", "jorge", "sam", "frank", "bob", "sandy", "shawn", 'sancho']

# # create a list that finds names with S and capitalizes them4

# s_names = [name.capitalize() for name in names if name[0].lower() =='s' ]

# # for name in names:
# #     # check if it starts with s
# #     if name[0].lower() == 's':
# #         s_names.append(name.capitalize())
# #     # add it to snames capitalized

# print(s_names)

#comprehensions work just as well with dictionaries as well

#populate a dictionary with all letters of the alphabet with their corresponding place
# letters="abcdefghijklmnopqrstuvwxyz"
# alpha = { letter: i+1 for i, letter in enumerate(letters)}

# # for i, letter in enumerate(letters):
# #     alpha[letter] = i + 1

# print(alpha)
