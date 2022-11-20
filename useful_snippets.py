# here are several tips for a variety of commands, I came across a couple interesting
# articles today that I used directly, or added some slight modifications to in the code below: 
# https://medium.com/techtofreedom/9-fabulous-python-tricks-that-make-your-code-more-elegant-bf01a6294908
# and
# https://blog.teclado.com/destructuring-in-python/
#
# added this for convenience to build my separator string here
print("#", "-"*45, "#") 
# produces the following:
# --------------------------------------------- #
# 
#
# product, helps you to avoid nested loops, operates on
# multiple lists simultaneously.

from itertools import product

list_a = [1, 2020, 70]
list_b = [2, 4, 7, 2000]
list_c = [3, 70, 7]

# for a in list_a:
#     for b in list_b:
#         for c in list_c:
#             if a + b + c == 2077:
#                 print(a, b, c)

# the following replaces the above snippet
for a, b, c in product(list_a, list_b, list_c):
    if a + b + c == 2077:
        print(a, b, c)
        
 # --------------------------------------------- #       
        
# combine variable creation and initialization where not possible
#
# author = "Yang"
# print(author)  

# print(author = "yang")
# produces: TypeError: 'author' is an invalid keyword argument for print()

print(author:="Yang")  

# --------------------------------------------- #
# ternary statement (value if boolean statement true otherwise use the second value)

# if a<b:
#   min = a
# else:
#   min = b
  
min = a if a < b else b


# --------------------------------------------- #
# Lambda

# def fib(x):
#     if x<=1:
#         return x
#     else:
#         return fib(x-1) + fib(x-2)
    
    
# print(fib( 22))
fib=lambda x: x if x <= 1 else fib(x - 1) + fib(x - 2)
print (fib(22))



# --------------------------------------------- #
# map

Genius = ["Jerry", "Jack", "tom", "yang"]
L1 = [name if name.startswith('y') else 'Not Genius:' +name for name in Genius]
print(L1)

L2 = [name if name.startswith('y') else '' for name in Genius]
while ('' in L2):
    L2.remove('')
print(L2)


names = ['yAnG', 'MASk', 'thoMas', 'LISA']
names = map(str.capitalize, names)  # 1st argument is a function, second argument is a list
print(list(names))


# --------------------------------------------- #
# reduce, applying a function to an iterable item

from functools import reduce

city = ['L', 'o', 'n', 'd', 'o', 'n', 2, 0, 2, 0]
city_to_str = reduce(lambda x, y: str(x) + str(y), city)
print(city_to_str)

email = ['Reid', '.', 'Tom', '@', 'my_provider', '.','com']
email_to_str = reduce(lambda x, y: (str(x) + str(y)).lower(), email)
print(email_to_str)


# --------------------------------------------- #
# merging a list, tupal, or set

A = [1, 2, 3]
B = (4, 5, 6)
C = {7, 8, 9}
L = [*A, *B, *C]
print(L)
# [1, 2, 3, 4, 5, 6, 8, 9, 7]

# the asterisks can also be used for destructuring assignments in Python
# there is more on destructuring later in this file, it is powerful.
a, *mid, b = [1, 2, 3, 4, 5, 6]
print(a, mid, b)
# 1 [2, 3, 4, 5] 6


# --------------------------------------------- #
# union, merging dictionaries


cities_us = {'New York City': 'US', 'Los Angeles': 'US'}
cities_uk = {'London': 'UK', 'Birmingham': 'UK'}

cities = cities_us|cities_uk
print(cities)


# --------------------------------------------- #
# F strings

pi = 3.1415926
print(f'Pi is approximately equal to {pi:.2f}')
# Pi is approximately equal to 3.14

id = 1  # need to print a 3-digit number
print(f"The id is {id:03d}")
# The id is 001

N = 1000000000  # need to add separator
print(f'His networth is ${N:,d}')
# His networth is $1,000,000,000


from datetime import datetime

print(f"Today is {datetime.today()}")
# Today is 2021-07-31 18:20:48.956829


# --------------------------------------------- #
# more on Destructuring

example_list = ["A", "B", "C"]

for _ in example_list:
    print(_)
        
for counter, letter in enumerate(example_list):
	print(counter, letter)

# 0 A
# 1 B
# 2 C


people = [
	("Bob", 42, "Mechanic"),
	("James", 24, "Artist"),
	("Harry", 32, "Lecturer")
]


for name, age, profession in people:
	print(f"Name: {name}, Age: {age}, Profession: {profession}")
 
 # Probably better choice than:
     
for person in people:
	print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")
 
# Raymond Hettinger — one of the core Python developers — said in one of his talks that in Python, 
# you should basically never be referring to items by their index: there is nearly always a
# better way.  https://blog.teclado.com/destructuring-in-python/
 
# use the_for a catch variable, when you want to ignore a position
person = ("Bob", 42, "Mechanic", "Allied_cars", "Boston", "MA")
name, _, profession,_,_, state = person

print(name, profession, state)  # Bob Mechanicopen Explorer

# _as a universal simple variable
for _ in person:
	print (_)
 

# more on using the *
head, *tail = [1, 2, 3, 4, 5]

print(head)  # 1
print(tail)  # [2, 3, 4, 5]



head, *middle, tail = [1, 2, 3, 4, 5]

print(head)    # 1
print(middle)  # [2, 3, 4]
print(tail)    # 5 



first, second, third, *rest = [1, 2, 3, 4, 5]
print (rest)

# --------------------------------------------- #
# --------------------------------------------- #
# the  following is produced as output running this complete program
# the comment has been added after executing this program.
# --------------------------------------------- #
# 70 2000 7
# Yang
# 17711
# ['Not Genius:Jerry', 'Not Genius:Jack', 'Not Genius:tom', 'yang']
# ['yang']
# ['Yang', 'Mask', 'Thomas', 'Lisa']
# London2020
# reid.tom@my_provider.com
# [1, 2, 3, 4, 5, 6, 8, 9, 7]
# 1 [2, 3, 4, 5] 6
# {'New York City': 'US', 'Los Angeles': 'US', 'London': 'UK', 'Birmingham': 'UK'}
# Pi is approximately equal to 3.14
# The id is 001
# His networth is $1,000,000,000
# Today is 2022-11-14 19:09:53.456748
# A
# B
# C
# 0 A
# 1 B
# 2 C
# Name: Bob, Age: 42, Profession: Mechanic
# Name: James, Age: 24, Profession: Artist
# Name: Harry, Age: 32, Profession: Lecturer
# Name: Bob, Age: 42, Profession: Mechanic
# Name: James, Age: 24, Profession: Artist
# Name: Harry, Age: 32, Profession: Lecturer
# Bob Mechanic MA
# Bob
# 42
# Mechanic
# Allied_cars
# Boston
# MA
# 1
# [2, 3, 4, 5]
# 1
# [2, 3, 4]
# 5
# [4, 5]