
# ....copy others from hard drive
# Dictionaries
# Dictionaries store connections between pieces of
# information. Each item in a dictionary is a key-value pair.
print('\n#A simple dictionary')
alien = {'color': 'green', 'points': 5}
print(alien)

print('\n#Accessing a value')
print("The alien's color is "+alien['color'])

print('\n#Adding a new key-value pair')
alien['x_position'] = 0
print(alien)

print('\n#Looping through all key-value pairs')
fav_numbers = {'eric': 17, 'ever': 4}
for name, number in fav_numbers.items():
    print(name + ' loves ' + str(number))

print('\n#Looping through all keys')
for name in fav_numbers.keys():
    print(name + ' loves a number ')

print('\n#Looping through all the values')
for number in fav_numbers.values():
    print(str(number) + ' is a favourite number ')

# User input
# Your programs can prompt the user for input. All input is
# stored as a string.
print('\n#Prompting for a value')
# name = input('What is your name? ')
# print('Hello '+name + '!')

print('\n#Prompting for numerical input')
# age1 = input('How old is you? ')
# age1=int(age1)
# print('Your age is ',age1)

# pi=input('What is the value of pi? ')
# pi=float(pi)
# print('The value of pi is ',pi)

# While loops
# A while loop repeats a block of code as long as a certain
# condition is true.
print('\n#A simple while loop')
current_value = 1
while current_value <= 5:
    print(current_value)
    current_value += 1

print('\n#Letting the user choose when to quit')
# msg=''
# while msg != 'quit':
#     msg=input("What's your message? ")
#     print('You: '+msg)

# Functions
# Functions are named blocks of code, designed to do one
# specific job. Information passed to a function is called an
# argument, and information received by a function is called a
# parameter.
print('\n#A simple function')


def greet_user():  # Defining and declaring the function
    """Display a simple greeting"""
    print('Greetings')


# calling the function
greet_user()

print('\n#Passing an argument')


def greet_user0(username):
    """Display personalized greetings."""
    print('Hello, '+username+'!')


greet_user0('Ricky')

print('\n#Default values for parameters')


def make_pizza(topping='bacon'):
    """Make a single-topping pizza."""
    print('Have a '+topping+" pizza!")


make_pizza()
make_pizza('pepperoni')

print('\n#Returning a value')


def add_number(x, y):
    """Add two numbers and returm the sum."""
    return x+y


sum = add_number(3, 5)
print('The sum of two numbers is = ', sum)

# CLasses
# A class defines the behavior of an object and the kind of
# information an object can store. The information in a class
# is stored in attributes, and functions that belong to a class
# are called methods. A child class inherits the attributes and
# methods from its parent class.
print('\n#Creating a dog class')


class Dog():
    """Represent a dog."""

    def __init__(self, name):
        """Initiatize a dog object."""
        self.name = name

    def sit(self):
        """Simulate sitting"""
        print(self.name+' is sitting.')


my_dog = Dog('Soully')  # creating an object(instance of a class) of class Dog
my_dog.sit()

print('\n#Inheritance')


class SARDog(Dog):
    """Represent a search dog."""

    def __init__(self, name):
        """Initialize the sardog"""
        super().__init__(name)

    def search(self):
        """Simlate searching"""
        print(self.name+' is searching.')


my_dog0 = SARDog('Charlie')

print(my_dog0.name + ' is searching')

my_dog0.sit()
my_dog0.search()

# Working with files
# Your programs can read from files and write to files. Files
# are opened in read mode ('r') by default, but can also be
# opened in write mode ('w') and append mode ('a').
print('\n#Writing to a file')
filename = 'test_file.txt'
with open(filename, 'w') as file_object:
    file_object.write('Sensei love programming.')

print('\n#Appending to a file')
filename = 'test_file.txt'
with open(filename, 'a') as file:
    file.write("\nHe develops softwares")

print('\n#Reading a file and storing its lines')
filename = 'test_file.txt'
with open(filename, 'r') as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line)

#Storing data with json
# The json module allows you to dump simple Python data
# structures into a file, and load the data from that file the
# next time the program runs. The JSON data format is not
# specific to Python, so you can share this kind of data with
# people who work in other languages as well.
# Knowing how to manage exceptions is important when
# working with stored data. You'll usually want to make sure
# the data you're trying to load exists before working with it.
print('\n#Using json.dump() to store data')
"""Store some numbers."""
import json
numbers = [2,3,4,6,7,8,4]
filename='numbers.json'
with open(filename,'w') as f_json:
    json.dump(numbers, f_json)
    
print('\n#Using json.load() to read data')

with open(filename) as f_obj:
    numbers0=json.load(f_obj)
print(numbers0)

print('\n#Making sure the stored data exists')
file_name='number.json'
try:
    with open(file_name,'r') as f_obj0:
        numbers1=json.load(f_obj0)
except FileNotFoundError:
    msg="can't find {0}.".format(file_name)
    print(msg)
else:print(numbers1)
# Exceptions
# Exceptions help you respond appropriately to errors that
# are likely to occur. You place code that might cause an
# error in the try block. Code that should run in response to
# an error goes in the except block. Code that should run only
# if the try block was successful goes in the else block.
print('\n#Catching an exception')
# prompt='How many tickets do you need? '
# num_tickets = input(prompt)
# try:
#     num_tickets=int(num_tickets)
# except ValueError:
#     print('Please insert correct value!')
# else:
#     print('Your Tickets are printing.')

# Here we use curly brackets,%s as placeholders and insert the values afterwards
print('\n# String formatting')
name, age = 'Ricky',13
print('My name is {} and I am {} years old'.format(name,age))
print('%s is my name!'% name)
print('I am %d years old!'% age)