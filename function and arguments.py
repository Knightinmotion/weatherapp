# functions = a block or (section) of reusable code
#             place () after the function name to invoke it
#             the order of your parameter must be in order


# def happy_birthday(name, age):  #--- these are parameters
#     print(f"Happy birthday to {name}!")
#     print(f"you are {age} years old!")
#     print("Happy birthday to you ")
#     print()
#
# happy_birthday("musa", 23)
# happy_birthday('solo', 23)
# happy_birthday("mimi", 34)


# print("Electricity Invoices")
# def display_invoice(username, amount, due_date):
#     print(f"hello {username}")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")
#     print()
#
# display_invoice("mimi", 100.2, "12/3")
# display_invoice("linus", 123.4, "11/5")
# display_invoice("Dave", 234.5, "23/6")


# return = statement used to end a function
#          and send a result back to the caller


# def add(x, y):
#     z = x + y
#     return z
#
# def subtract(x, y):
#     z = x - y
#     return z
#
# def multiply(x, y):
#     z = x * y
#     return z
#
# def divide(x, y):
#     z = x / y
#     return z
#
# print(add(1, 2))
# print(divide(25, 5))
#
# def display_full_name(first, last ):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first + " " + last
#
# full_name =  display_full_name("mimi", "musa")
# full_name =  display_full_name("mj", "davis")
#
# print(full_name)
#
#

# default arguments = A default value for certain parameters
#                     default is used when that argument is omitted
#                     1. positional, 2. DEFAULT,  3. keyword, 4. arbitrary
#
#
# import time
#
# def count(end, start=0 ):
#     for x in reversed(range(start, end + 1)):
#         print(x)
#         time.sleep(1)
#     print("DONE!")
#
# count(30, 15 )


# keyword arguments = an arguments preceded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1. positional, 2. DEFAULT,  3. keyword, 4. arbitrary

#
# def hello(greeting, title, first, last):
#     print(f"{greeting}, {title}{first} {last}")
#
# hello("Hello", "Mr.", "Spongebob", "Squarepants")

#
# for x in range(1, 11):
#     print(x, sep=" ")

#
# def get_phone(country, area, first, last):
#     return f"{country}-{area}-{first}-{last}"
#
#
# phone_num = get_phone(country=1, area=123, first=456, last=7890)
#
# print(phone_num)


#  *args    =  allows you to pass multiple non-keys arguments
#  **kwargs = allows you to pass multiple keyword-arguments
#            * is an unpacking operator
#            1. positional, 2. DEFAULT,  3. keyword, 4. arbitrary

#
# def add(*args):
#     total  = 0
#     for arg in args:
#         total += arg
#     return total
#
# print(add(1,4,8,))

#
# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")
#
#
# display_name("Dr.", "mimi", "MIME", "SCOPE", "III")


# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
#
# print_address(street="123 Fake st",
#               city="city",
#               state="MI",
#               zip="54321")
#
# def shipping_label(*args, **kwargs):
#     for arg in args:
#         print(arg, end=" ")
#     print()
#     for value in kwargs.values():
#         print(value, end=" ")
#
#
# shipping_label("Dr.", "mimi", "MIME", "SCOPE", "III",
#                street="123 fake st.",
#                apt="100",
#                city="detroit,",
#                state='MI.',
#                zip=54321)

# Iterables = An object/collection that can  return its elements one at a time,
#             allowing it to be iterables over in a loop
#
# fruits = {"apple", "orange", "banana", "coconut" }
# for fruit in fruits:
#      print(fruit)

# name = "miracle", "mathew"
# for character in name:
#     print(character, end=" ")


# membership operator = used to test whether a value or variable is found in a sequence
#                       (string, list, tuple, set, or dictionary)
#                       1. in
#                       2. not in

# for string

# word = "APPLE"
#
# letter = input("Guess a letter in the secret word: ")
#
# if letter in word:
#     print(f"There is a {letter}")
# else:
#     print(f"{letter} was not found ")
#
#

# for dictionary

# grades = {"mimi":"A",
#           "zeke":"B",
#           "colos":"C",
#           "cal":"D"}
#
# student = input("Enter the name of the student: ")
#
# if student in grades:
#     print(f"{student}'s grades is {grades}")
# else:
#     print(f"{student} was not found")

# email = "miraclesayscode@gmail.com"
#
# if "@" in email and "." in email:
#     print("valid email")

# else:
#     print("invalid email")
