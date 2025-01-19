print(3 + 2)   # addition(+)
print(3 - 2)   # subtraction(-)
print(3 * 2)   # multiplication(*)
print(3 / 2)   # division(/)
print(3 ** 2)  # exponential(**)
print(3 % 2)   # modulus(%)
print(3 // 2)  # Floor division operator(//)



print(type(10))                  # Int
print(type(3.14))                # Float
print(type(1 + 3j))              # Complex
print(type('Asabeneh'))          # String
print(type([1, 2, 3]))           # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple
print(type(3 == 3))              # Bool
print(type(3 >= 3))              # Bool






# Variables in Python

first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Asabeneh', 
    'lastname':'Yetayeh', 
    'country':'Finland',
    'city':'Helsinki'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)



# Arithmetic Operations in Python
# Integers

print('Addition: ', 1 + 2)
print('Subtraction: ', 2 - 1)
print('Multiplication: ', 2 * 3)
print ('Division: ', 4 / 2)                         # Division in python gives floating number
print('Division: ', 6 / 2)
print('Division: ', 7 / 2)
print('Division without the remainder: ', 7 // 2)   # gives without the floating number or without the remaining
print('Modulus: ', 3 % 2)                           # Gives the remainder
print ('Division without the remainder: ', 7 // 3)
print('Exponential: ', 3 ** 2)                     # it means 3 * 3

# Floating numbers
print('Floating Number,PI', 3.14)
print('Floating Number, gravity', 9.81)

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex number: ',(1 + 1j) * (1-1j))

# Declaring the variable at the top first

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function try to avoid overriding builtin functions
print(total) # if you don't label your print with some string, you never know from where is  the result is coming
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

# Declaring values and organizing them together

num_one = 3
num_two = 4

# Arithmetic operations

total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_two
remainder = num_two % num_one

# Printing values with label

print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)


# Calculating area of a circle
radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')




print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# Boolean comparison
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False)

# Another way comparison 

print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False -there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True


print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statement is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False




a = "Raj"
print(a) # Assign

b = 10
c = 5

print(b+c)  # Addition


str = "Apple" # double quates

Str = 'Banana' # Single quates

x , y , z = "one" , "two" , "three"

print(x , y , z) # Multible Variable Assigned


x1 = "Best"

def function():
  print("Python is " + x1)

function()


y1 = "Easy"

def function_1():
  z1 = "fantastic"
  print("Python is " + z1)

function_1()

print("Python is " + y1)


# Data Types :-

one = "Welcome" # String 
print(type(one))

two = 100 # Number or intiger
print(type(two))

three = 10.5 # Float
print(type(three))

four = ["Mom" , "Dad" , "Son"]  # List
print(type(four))

five = ("TV" , "Fan" , "Light") # Tuple
print(type(five))

six = None  # None
print(type(six))



# STRING 

str_1 = " ABCDEFGHIJKLMNOPQRSTUVWXYZ " 

str_2 = " ABCDE FGHIJ KLMNO PQRST UVWXYZ "

print(str_1[:10])  # Show the 1st to 10th words

print(str_1[5 : 10]) # show the 5th word to 10th word

print(str_1[10]) # show the 10th word -- J --

print(str_1[-10]) # show the revers to the 10th word -- Q --

print(str_1[10 : -10]) # showing on 1st 10 letter and last 10 letter is not showing 

print(str_1.replace("A" , "Z"))  # Replace the letter in 1at input is take them 2nd value is put it

print(str_2.split()) # ['ABCDE', 'FGHIJ', 'KLMNO', 'PQRST', 'UVWXYZ']





# Single line comment
letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be  a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of python challenge"
print(sentence)

# Multiline String
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)
# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)

# String Concatenation
first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) # Asabeneh Yetayeh
# Checking length of a string using len() builtin function
print(len(first_name))  # 8
print(len(last_name))   # 7
print(len(first_name) > len(last_name)) # True
print(len(full_name)) # 15

#### Unpacking characters 
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t 
print(d) # h
print(e) # o
print(f) # n

# Accessing characters in strings by index
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n

# If we want to start from right end we can use negative indexing. -1 is the last index
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o

# Slicing

language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

# Skipping character while splitting Python strings
language = 'Python'
pto = language[0:6:2] # 
print(pto) # pto

# Escape sequence
print('I hope every one enjoying the python challenge.\nDo you ?') # line break
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a back slash  symbol (\\)') # To write a back slash
print('In every programming language it starts with \"Hello, World!\"')

## String Methods
# capitalize(): Converts the first character the string to Capital Letter

challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'

# count(): returns occurrences of substring in string, count(substring, start=.., end=..)

challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1
print(challenge.count('th')) # 2`

# endswith(): Checks if a string ends with a specified ending

challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument

challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'

# find(): Returns the index of first occurrence of substring

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

# format()	formats string into nicer output    
first_name = 'Asabeneh'
last_name = 'Yetayeh'
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(first_name, last_name, job, country)
print(sentence) # I am Asabeneh Yetayeh. I am a teacher. I live in Finland.



# index(): Returns the index of substring
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

# isalnum(): Checks alphanumeric character

challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False

# isalpha(): Checks if all characters are alphabets

challenge = 'thirty days of python'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False

# isdecimal(): Checks Decimal Characters

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

# isdigit(): Checks Digit Characters

challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'


# isdecimal():Checks decimal characters

num = '10'
print(num.isdecimal()) # True
num = '10.5'
print(num.isdecimal()) # False


# isidentifier():Checks for valid identifier means it check if a string is a valid variable name

challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True


# islower():Checks if all alphabets in a string are lowercase

challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False

# isupper(): returns if all characters are uppercase characters

challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True


# isnumeric():Checks numeric characters

num = '10'
print(num.isnumeric())      # True
print('ten'.isnumeric())    # False

# join(): Returns a concatenated string

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '#, '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'

# strip(): Removes both leading and trailing characters

challenge = ' thirty days of python '
print(challenge.strip('y')) # 5

# replace(): Replaces substring inside

challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'

# split():Splits String from Left

challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']

# title(): Returns a Title Cased String

challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python

# swapcase(): Checks if String Starts with the Specified String
  
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

# startswith(): Checks if String Starts with the Specified String

challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True
challenge = '30 days of python'
print(challenge.startswith('thirty')) # False




# Concatenation

ab = 'ABCDE'
cd = 'FGHIJ'

print(ab + cd)
print(ab + " , " + cd)

# String Formatting 

age = 22
sentence = f"My age is : {age} " # f simble is key word
print(sentence)

# String capitalize()

text = "hello, and welcome to my world."

Cap = text.capitalize()

print (Cap)  # 1st Letter only is Capitalized


# String casefold() 

text_1 = "Hello, And Welcome To My World!"

CF = text_1.casefold()

print(CF) # All letters is change on lower case


# String center()

text_2 = "banana"

cen = text_2.center(30)

print(cen)


# String count()

text_3 = "I love apples, apple are my favorite fruit"

cnt = text_3.count("apple")

print(cnt)

# String encode()

text_4 = "My name is Ståle"

enc = text_4.encode()

print(enc)

# Types ( Encode() )

text_5 = "My name is Ståle"

print(text_5.encode(encoding="ascii",errors="backslashreplace"))
print(text_5.encode(encoding="ascii",errors="ignore"))
print(text_5.encode(encoding="ascii",errors="namereplace"))
print(text_5.encode(encoding="ascii",errors="replace"))
print(text_5.encode(encoding="ascii",errors="xmlcharrefreplace"))


# String startswith()

text_6 = "Hello, welcome to my world."
sw = text_6.endswith("Hello")

print(sw)


# String endswith()

text_7 = "Hello, welcome to my world."
ew = text_7.endswith("my world.")

print(ew)


# String expandtabs()

text_8 = "H\te\tl\tl\to"

print(text_8) # 4 space
print(text_8.expandtabs()) # 8 space
print(text_8.expandtabs(2)) # 2 space
print(text_8.expandtabs(4)) # 4 space
print(text_8.expandtabs(10)) # 10 space


# String find()


text_9 = "Hello, welcome to my world."

print(text_9.find("l"))  # 2nd place


# String index()

text_10 = "Hello, welcome to my world."

idx = text_10.index("welcome")

print(idx) # 7 letters
print(text_10.index("w")) # 7th place


# String join()

text_11 = (" John ", " Peter ", " Vicky")

jn = "#".join(text_11)

print(jn)  # --  John # Peter # Vicky --


# String title()

text_12 = "Welcome to my world"

tle = text_12.title()

print(tle) #  first character in every word is upper case


# String swapcase()

text_13 = "Hello My Name Is PETER"

swp = text_13.swapcase()

print(swp) # opposite to the caps to small , small to caps


# String partition()

text_14 = "I could eat bananas all day"

pr = text_14.partition("bananas")

print(pr)


# Boolean 

print(10 > 9) # true
print(10 == 9) # false
print(10 < 9) # false

# True Statement

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

# false Statement

print(bool(False))  
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# yes means true -- no means false

def myFunction() :
  return False

if myFunction():
  print("YES!")
else:
  print("NO!")


# List
# List is a collection which is ordered and changeable. Allows duplicate members.


list0 = [ "apple", "banana", "cherry", "apple", "cherry" ]

print(list0) # duplicate values are allowed in list
print(type(list0)) # list is a data type in python

list1 = ["apple", "banana", "cherry"]

print(list1) # list of strings
print(type(list1)) # list is a data type in python

list2 = [1, 5, 7, 9, 3]

print(list2) # list of integers
print(type(list2)) # list is a data type in python

list3 = [True, False, False , True]

print(list3) # list of boolean values
print(type(list3)) # list is a data type in python

list4 = ["abc", 34, True, 40, "male" , False]

print(list4) # list of mixed data types
print(type(list4)) # list is a data type in python 


list5 = ["apple", "banana", "cherry"]
if "apple" in list5:  # in is a key word in python to check if a value is present in a list
  print("Yes, 'apple' is in the fruits list")
else: 
   print("No, 'apple' is not in the fruits list")


 # Access List Items


list6 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list6[3:]) # prints from index 3 to the end of the list

list7 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list7[:4]) # prints from the start of the list to index 4

list8 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list8[2:5]) # prints from index 2 to index 5

list9 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list9[-4:-1]) # prints from index -4 to index -1

list10 = ["apple", "banana", "cherry"]
print(list10[-1]) # prints the last item in the list

list11 = ["apple", "banana", "cherry"]
print(list11[1]) # prints the second item in the list


# Change List Items

list12 = ["apple", "banana", "cherry"]
list12[1] = "blackcurrant"

print(list12)
# Output: ['apple', 'blackcurrant', 'cherry']

list13 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
list13[1:3] = ["blackcurrant", "watermelon"]

print(list13)
# Output: ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']


# Add List Items

list14 = ["apple", "banana", "cherry"]
list14.insert(2, "watermelon")

print(list14) 
# Output: ['apple', 'banana', 'watermelon', 'cherry']

list15 = ["apple", "banana", "cherry"]
list15.append("orange")

print(list15)
# Output: ['apple', 'banana', 'cherry', 'orange']

list16 = ["apple", "banana", "cherry"]
list17 = ["mango", "pineapple", "papaya"]

list16.extend(list17)

print(list16)
# Output: ['apple', 'banana', 'cherry', 'mango', 'pineappl', 'papaya']


# Remove List Items

list18 = ["apple", "banana", "cherry"]
list18.remove("banana")

print(list18)
# Output: ['apple', 'cherry']

list19 = ["apple", "banana", "cherry"]
list19.pop(1)
print(list19)
# Output: ['apple', 'cherry']

list20 = ["apple", "banana", "cherry"]
list20.pop()

print(list20)
# Output: ['apple', 'banana']

list21 = ["apple", "banana", "cherry"]
del list21[0]  # del keyword is used to delete the item at the specified position.

print(list21)
# Output: ['banana', 'cherry']

list22 = ["apple", "banana", "cherry"]
list22.clear()

print(list22)
# Output: []




empty_list = list() # this is an empty list, no item in the list
print(len(empty_list)) # 0

fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Print the lists and it length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Number of countries:', len(countries))

# Modifying list

fruits = ['banana', 'orange', 'mango', 'lemon'] 
first_fruit = fruits[0] # we are accessing the first item using its index
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

# Accessing items
fruits = ['banana', 'orange', 'mango', 'lemon'] 
last_fruit = fruits[-1]
second_last = fruits[-2]
print(last_fruit)       # lemon
print(second_last)      # mango

# Slicing items
fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits = fruits[0:4] # it returns all the fruits
# this is also give the same result as the above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the end index
orange_mango_lemon = fruits[1:]

fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits = fruits[-4:] # it returns all the fruits
# this is also give the same result as the above
orange_and_mango = fruits[-3:-1] # it does not include the end index
orange_mango_lemon = fruits[-3:]


fruits = ['banana', 'orange', 'mango', 'lemon'] 
fruits[0] = 'Avocado' 
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']

# checking items
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False

# Append
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime]
# print(fruits) # This should give: NameError: name 'fruits' is not defined
          

# insert
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'mango', 'lime','lemon',]
print(fruits)

# remove
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon']
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango']

# pop
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()     
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)     
print(fruits)       # ['orange', 'mango'] 

# del 
fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]     
print(fruits)       # ['orange', 'mango', 'lemon']

del fruits[1]     
print(fruits)       # ['orange', 'lemon']
del fruits
# print(fruits)       # This should give: NameError: name 'fruits' is not defined

# clear
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()     
print(fruits)       # []

# copying a lits

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()     
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']

# join
positive_numbers = [1, 2, 3,4,5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'] 
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables )

# join with extend
num1 = [0, 1, 2, 3]
num2= [4, 5,6]
num1.extend(num2)
print('Numbers:', num1)
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'] 
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits )

# count
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3

# index
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24)) 
# Reverse
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)  
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages) 

# sort
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits) 
fruits.sort(reverse=True)
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages) 
ages.sort(reverse=True)
print(ages) 




# Loop Lists

list23 = ["apple", "banana", "cherry"]
for i1 in list23:

  print(i1)

# Output: apple
# Output: banana
# Output: cherry


# List Comprehension
  
list24 = ["apple", "banana", "cherry", "kiwi", "mango"]
list25 = []

for x1 in list24:
  if "a" in x1:
    list25.append(x1)

print(list25) # Output: ['apple', 'banana', 'cherry']
# Becouse of 'a' letter is have a all value is print a newlist.


list26 = ["apple", "banana", "cherry", "kiwi", "mango"]
list27 = [x2 for x2 in list26 if x2 != "apple"]

print(list27)
# Output: ['banana', 'cherry', 'kiwi', 'mango']

list28 = ["apple", "banana", "cherry", "kiwi", "mango"]
list29 = [x3 for x3 in list28]

print(list29) # Output: ['apple', 'banana', 'cherry', 'kiwi', 'mango
# { Copy the list } Becouse of list28 value is print a newlist. 


# Sort Lists

list30 = ["orange", "mango", "kiwi", "pineapple", "banana"]
list30.sort()

print(list30) # Output: ['banana', 'kiwi', 'mango', 'orange', 'pineapple']
# that is alpha and numberucally order the data .

list31 = [100, 50, 65, 82, 23]
list31.sort()

print(list31) # Output: [23, 50, 65, 82, 100]

list32 = [100, 50, 65, 82, 23]
list32.sort(reverse = True)

print(list32) # Output: [100, 82, 65, 50, 23]


# Copy Lists

list33 = ["apple", "banana", "cherry"]
list34 = list33.copy()

print(list34) # Output: ['apple', 'banana', 'cherry']

list35 = ["apple", "banana", "cherry"]
list36 = list(list35)

print(list36) # Output: ['apple', 'banana', 'cherry']

list37 = ["apple", "banana", "cherry"]
list38 = list37[:]

print(list38) # Output: ['apple', 'banana', 'cherry']







# Tuples

# Tuples are used to store multiple items in a single variable
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.


tuple0 = ("apple", "banana", "cherry", "apple", "cherry")
print(tuple0)
 # Output: ('apple', 'banana', 'cherry', 'apple', 'cherry')

tuple1 = ("abc", 34, True, 40, "male")

print(tuple1) # Output: ('abc', 34, True, 40, 'male')

tuple2 = ("apple", "banana", "cherry")

print(type(tuple2)) # Output: <class 'tuple'>

tuple3 = tuple(("apple", "banana", "cherry"))
print(tuple3) # Output: ('apple', 'banana', 'cherry')

tuple4 = ("apple", "banana", "cherry")
print(tuple4[1]) # Output: banana

tuple5 = ("apple", "banana", "cherry")
print(tuple5[-1]) # Output: cherry

tuple6 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tuple6[2:5]) # Output: ('cherry', 'orange', 'kiwi')

tuple7 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tuple7[-4:-1]) # Output: ('orange', 'kiwi', 'melon')

tuple8 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tuple8[:4]) # Output: ('apple', 'banana', 'cherry', 'orange')

tuple9 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tuple9[2:]) # Output: ('cherry', 'orange', 'kiwi', 'melon', 'mango')

tuple10 = ("apple", "banana", "cherry")
if "apple" in tuple10:
  print("Yes, 'apple' is in the fruits tuple")
else :
  print("No! , 'apple' is not in the fruits tuple") 

# Output: Yes, 'apple' is in the fruits tuple


# Update Tuples

tuple11 = ("apple", "banana", "cherry")
tuple12 = list(tuple11)
tuple12.append("orange")
tuple11 = tuple(tuple12)

print(tuple11) # Output: ('apple', 'banana', 'cherry', 'orange')


tuple13 = ("apple", "banana", "cherry")
tuple14 = ("orange",)
tuple13 += tuple14

print(tuple13) # Output: ('apple', 'banana', 'cherry', 'orange')


# Unpack Tuples

tuple14 = ("apple", "banana", "cherry")

(zero, one, two) = tuple14

print(zero)
print(one)
print(two) 
# Output: apple
# Output: banana
# Output: cherry


tuple15 = ("apple", "mango", "papaya", "pineapple", "cherry")

(four, *five, six) = tuple15 #  -- * -- this star is a key word " Between the values is given "

print(four)
print(five)
print(six)
# apple
# ['mango', 'papaya', 'pineapple']
# cherry


# Join Tuples

tuple16 = ("a", "b" , "c")
tuple17 = (1, 2, 3)

tuple18 = tuple16 + tuple17
print(tuple18)
# Output: ('a', 'b', 'c', 1, 2, 3)

tuple19 = ("apple", "banana", "cherry")
tuple20 = tuple19 * 2

print(tuple20)
# Output: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')


# Tuple count()

tuple21 = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
tuple22 = tuple21.count(5)

print(tuple22) # Output: 2 "how meny 5 is there ? only 2 five is there in tuple"


tuple23 = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

tuple24 = tuple23.index(8)

print(tuple24) # Output: 3 "where is 8 ? 8 is at index 3"



# Set  """ Not Allowed the duplicate value """
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.


set0 = {"apple", "banana", "cherry", "apple"}

print(set0) # Sets cannot have two items with the same value
               # Output: {'apple', 'banana', 'cherry'}


set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1) # Output: {'apple', 'banana', 'cherry'}
print(set2) # Output: {1, 5, 7, 9, 3}
print(set3) # Output: {True, False}


set4 = {"apple", "banana", "cherry"}
print(type(set4)) # Output: <class 'set'>


set5 = set(("apple", "banana", "cherry"))
print(set5) # Output: {'apple', 'banana', 'cherry'}


# Access Set items

set6 = {"apple", "banana", "cherry"}

for set7 in set6:
  print(set7) 

# Output: apple 
# Output: banana
# Output: cherry

set8 = {"apple", "banana", "cherry"}
print("banana" in set8) # Output: True

set9 = {"apple", "banana", "cherry"}
print("banana" not in set9) # Output: False

# Add Set Items

set10 = {"apple", "banana", "cherry"}
set10.add("orange")

print(set10) # Output: {'apple', 'banana', 'cherry', 'orange'}

set11 = {"apple", "banana", "cherry"}
set12 = {"pineapple", "mango", "papaya"}

set11.update(set12)

print(set11) # Output: {'apple', 'banana', 'cherry', 'mango', 'pineapple', 'banana', 'papaya'}


# Remove Set Items

set12 = {"apple", "banana", "cherry"}
set12.remove("banana")

print(set12) # Output: {'apple', 'cherry'}


set13 = {"apple", "banana", "cherry"}
set13.discard("banana")

print(set13) # Output: {'apple', 'cherry'}


set14 = {"apple", "banana", "cherry"}
set15 = set14.pop()

print(set15) #removed item
print(set14) #the set after removal


set16 = {"apple", "banana", "cherry"}
set17 = set16.clear()

print(set17) # None



# Python Dictionaries
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

dry0 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dry0) # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964 }


dry1 = dict(name = "John", age = 36, country = "Norway")

print(dry1) # Output: {'name': 'John', 'age': 36, 'country': 'Norway" }
             # 'dict' is a key word in python to create a dictionary


# Access Dictionary Items

dry2 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dry3 = dry2.get("model")
print(dry3) # Output: Mustang

dry4 = dry2["model"]
print(dry4) # Output: Mustang

dry5 = dry2.keys()
print(dry5)

dry6 = dry2.keys()
print(dry6) #before the change
dry2["color"] = "white"
print(dry6) #after the change


dry7 = dry2.values()
print(dry7) #before the change
dry2["year"] = 2020
print(dry7) #after the change


# Change Dictionary Items

dry8 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dry8["year"] = 2018

print(dry8) # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2018 }


dry9 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dry9.update({"year": 2020})

print(dry9) # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020 }


# Add Dictionary Items

dry10 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dry10["color"] = "red"

print(dry10) # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}


# Remove Dictionary Items

dry11 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dry11.pop("model")  
print(dry11) # Output: {'brand': 'Ford', 'year': 1964 }

dry11.popitem()
print(dry11) # Output: {'brand': 'Ford', 'year': 1964 }

dry11.clear()
print(dry11) # Output: {}


# Loop Dictionaries

dry12 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for dry13 in dry12:
  print(dry13) # Output: brand, model, year


for dry13 in dry12:
  print(dry12[dry13]) # Output: Ford, Mustang, 1964

for dry13 in dry12.values():
  print(dry13) # Output: Ford, Mustang, 1964

for dry13 in dry12.keys():
  print(dry13) # Output: brand, model, year

for dry13, dry14 in dry12.items():
  print(dry13, dry14) # Output: brand Ford, model Mustang, year 1964


# Copy Dictionaries

dry15 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dry16 = dry15.copy()
print(dry16)

dry16 = dict(dry15) # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964 }
print(dry16) # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964 }


# Nested Dictionaries

dry17 = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(dry17)
# Output: {'child1': {'name': 'Emil', 'year': 2004}, 
#           'child2': {'name': 'Tobias', 'year': 2007}, 
#           'child3': {'name': 'Linus', 'year': 2011}}


for dry18, obj in dry17.items():
    print(dry18)
    
    for dry19 in obj:
        print(dry19 + ':', obj[dry19])

# Output:-

# child1
# name: Emil
# year: 2004
# child2
# name: Tobias
# year: 2007
# child3
# name: Linus
# year: 2011



child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

dry20 = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(dry20)
# Output: {'child1': {'name': 'Emil', 'year': 2004},
#          'child2': {'name': 'Tobias', 'year': 2007},
#          'child3': {'name': 'Linus', 'year': 2011}}


# Python If ... Else

if0 = 200
if1 = 33
if if1 > if0:
  print("b is greater than a")
elif if0 == if1:
  print("a and b are equal")
else:
  print("a is greater than b")

# Output: a is greater than b



if2 = 330
if3 = 330

print("A") if if2 > if3 else print("B") 
# Output: B


if4 = 41

if if4 > 10:
  print("Above ten,")
  if if4 > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# Output: Above ten, 
# and also above 20!


# Python For Loops

fl0 = ["apple", "banana", "cherry"]
for fl1 in fl0:
  print(fl1) 
  if fl1 == "banana":
    break # Stop the loop if "banana" is found
          # Output: apple , banana

fl2 = ["apple", "banana", "cherry"]
for fl3 in fl2:
  if fl3 == "banana":
    break
  print(fl3)  # Output: apple



# while Loop

w0 = 0
while w0 < 6:
  print(w0)
  w0 += 1

# Output: 0, 1, 2, 3, 4, 5


w1 = 0
while w1 <= 10:
  print(w1)
  if (w1 == 10):
    break
  w1 += 1

# Output: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10


# Python Functions


def fn0():
  print("Hello from a function")
 
fn0() # Output: Hello from a function


def fn1(fname):
  print(fname + " Refsnes")

fn1("Emil") # Output: Emil Refsnes
fn1("Tobias") # Output: Tobias Refsnes
fn1("Linus") # Output: Linus Refsnes


def fn2(country = "Norway"):
  print("I am from " + country)

fn2()         # Output: I am from Norway
fn2("Sweden") # Output: I am from Sweden
fn2("India")  # Output: I am from India
fn2("Brazil") # Output: I am from Brazil


def fn3(fname, lname):
  print(fname + "." + lname)

fn3("Pandiyarajan", "P") 


def fn4(fn5):
  return 5 * fn5

print(fn4(3)) # Output: 15
print(fn4(5)) # Output: 25
print(fn4(9)) # Output: 45


def fn6(a, b, c, d):
  print(a + b + c + d)

fn6(5, 6, c = 7, d = 8 ) # Output: 26



def fn7(fn8 , fn9 = 0): # default value for 'fn9'
    if(type(fn8) is not int or type(fn9) is not int): return 0
    
    return fn8 + fn9

total = fn7(10)
print(total) # Output: 10



# Python Lambda Functions


lo = lambda l1: l1 + 10
print(lo(5)) # Output: 15

l2 = lambda l3, l4: l3 * l4
print(l2(5, 6)) # Output: 30

l5 = lambda l6, l7, l8: l6 + l7 + l8
print(l5(5, 6, 2)) # Output: 13


def l9(l11):
  return lambda l10 : l10 * l11
l12 = l9(3)

print(l12(10)) # Output: 30


def l13(l15):
  return lambda l14 : l14 * l15

l16 = l13(4)
l17 = l13(8)

print(l16(10)) 
print(l17(10))



# Python Arrays

cars = ["Ford", "Volvo", "BMW"]
fruits = ['apple', 'banana', 'cherry']

print(cars) # Output: ['Ford', 'Volvo', 'BMW']

ar0 = cars[0]
print(ar0)    # Output: Ford

cars[0] = "Toyota"
print(cars)  # Output: ['Toyota', 'Volvo', 'BMW']

ar1 = len(cars)
print(ar1)     # Output: 3

for ar2 in cars:
  print(ar2)     # Output: Toyota, Volvo, BMW

cars.append("Honda")
print(cars)  # Output: ['Toyota', 'Volvo', 'BMW', 'Honda']

ar3 = cars.index("Honda")
print(ar3) # Output: 3

cars.insert(1, "Suzuki")
print(cars) # Output: ['Toyota', 'Suzuki', 'Volvo', 'BMW', 'Honda']

fruits.extend(cars)
print(fruits) # Output: ['apple', 'banana', 'cherry', 'Toyota', 'Suzuki' , 'Volvo', 'BMW', 'Honda']

fruits.reverse()
print(fruits) # Output: ['Honda', 'BMW', 'Volvo', 'Suzuki', 'Toyota' , 'cherry' , 'banana', 'apple']

ar4 = cars.copy() 
print(ar4) # Output: ['Toyota', 'Suzuki', 'Volvo', 'BMW', 'Honda']

cars.pop(1)
print(cars) # Output: ['Toyota', 'Volvo', 'BMW', 'Honda']

cars.remove("Honda")
print(cars)   # Output: ['Toyota', 'Volvo', 'BMW']

cars.clear()
print(cars)  # Output: []





# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value



























































































































