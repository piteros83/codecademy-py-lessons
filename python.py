#piggy tales
pyg = 'ay'
original = raw_input('Enter a word:')
word = original.lower()
first = word[0]
new_word = original[1:len(new_word)] + first + pyg
if len(original) > 0 and original.isalpha():
    print original
else:
    print 'empty'
print new_word

#==========================================================
number = raw_input("Wprowadz liczbe: ")

def cube(number):
    number **=  3
    return number
    
def by_three(number):
    if number % 3 == 0:
      print "jest podzielna przez 3"
      number=cube(number)
      return number
    else:
      print "nie jest podzielna przez 3"
      return False
	  
	  
#=============================================================

import math            # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything       # Prints 'em all!

['__doc__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']

#==============================================================


def shut_down(s):
    if s == "yes":
        return "Shutting down"
    elif s == "no": 
        return "Shutdown aborted"
    else:
        return "Sorry"

shut_down(yes)

#==============================================================

from math import sqrt
print sqrt(13689)

#==============================================================

def distance_from_zero(num):
 if type(num) == int or type(num) == float:
     return abs(num)
 else:
     return "Nope"
	 
#==============================================================	 
#trip calculator

def hotel_cost(nights):
    nights *= 140
    return nights
    
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

def rental_car_cost(days):
    cost = 40 * days
    if days >= 7:
        cost -= 50
    elif days >=3 and days < 7:
        cost -= 20
    elif days < 3:
        cost
    return cost
	
def trip_cost(city, days, spending_money):
    total_cost = rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city)
    return total_cost + spending_money
	
	
#===============================================================

numbers = [5, 6, 7, 8]

print "Adding the numbers at indices 0 and 2..."
print numbers[0] + numbers[2]
print "Adding the numbers at indices 1 and 3..."
print numbers[3] + numbers[1]


#===============================================================
# Lists suitcase

suitcase = [] 
suitcase.append("sunglasses")


suitcase.append("camera")
suitcase.append("shirt")
suitcase.append("sunglasses")

list_length = len(suitcase) # Set this to the length of suitcase

print "There are %d items in the suitcase." % (list_length)
print suitcase

#================================================================

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]

duck_index = animals.index("duck")

animals.insert(duck_index, "cobra")

print animals # Observe what prints after the insert operation

#================================================================

my_list = [1,9,3,8,5,7]

for number in my_list:
    print(2 * number)
	
#================================================================	

start_list = [5, 3, 1, 2, 4]
square_list = []

for number in start_list:
    square_list.append(number ** 2)
square_list.sort()

print square_list

#================================================================
Simple menu

menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

menu['Chef Burger'] = 12.34
menu['French Fries'] = 4.22
menu['Red Wine'] = 23.66

print "There are " + str(len(menu)) + " items on the menu."
print menu

#================================================================
#zoo animals location dictonaries

# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']

zoo_animals['Rockhopper Penguin'] = 'Jungle House'

print zoo_animals

#================================================================
#remove from list

backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']

backpack.remove('dagger')

print backpack

#================================================================
#inventory operations list/dictonaries
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')

inventory['gold'] += 50

print inventory['gold']

#================================================================
#for loops with dictionaries

webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

# Add your code below!
for x in webster:
    print webster[x]


#================================================================
#for loops for even numbers

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for num in a:
    if num % 2 == 0:
        print num

#================================================================
#List + functions

def fizz_count(x):
    count = 0
    for y in x:
        if y == "fizz":
            count += 1
    return count
    
print (fizz_count(["fizz","cat","fizz","fizz","fizz","fizz","dog","fish"]))

#================================================================
#day at supermarket
prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}
stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}

for key in prices:
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]
    
    
total = 0

for item in prices:   # zsumuj caly magazyn
    total = total + (prices[item] * stock[item])

print(total)

def compute_bill(food):   
    total = 0
    for item in food:
        if stock[item] > 0:   # jesli jest na stanie dodawaj do koszyka i go sumuj
           total += prices[item]   #sumuj koszyk
           stock[item] -= 1  #jesli dodane do koszyka to odejmij od stanu
        else:
           total += 0   #jesli nie ma na stanie nie dodawaj do koszyka
    return total

#================================================================	
#Student becomes a teacher
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

def average(numbers):
    total = sum(numbers)
    total = float(total)
    total = total / len(numbers)
    return total    

def get_average(student):
    homework = average(student["homework"])
    quizzes  = average(student["quizzes"])
    tests    = average(student["tests"]) 
    return (0.1 * homework) + (0.3 * quizzes) + (0.6 * tests)
    
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80 and score < 90:
        return "B"
    elif score >= 70 and score < 80:
        return "C"
    elif score >= 60 and score < 70:
        return "D"
    else:
        return "F"
        
def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)
	
students = [lloyd, alice, tyler] 

print (get_class_average(students))

print (get_letter_grade(get_class_average(students)))  

#================================================================
#list appender function
n = [3, 5, 7]
# Add your function here
def list_extender(lst):
    lst.append(9)
    return lst
    
print list_extender(n)

#================================================================
#Modifying each element in a list in a function
n = [3, 5, 7]

def double_list(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x    
# Don't forget to return your new list!

print double_list(n)

#================================================================
#Iterating over a list in a function
n = [3, 5, 7]

def total(numbers):
    result = 0
    for i in range(len(numbers)):
        result += numbers[i]
    return result

print total(n)


#================================================================
#Using a list of lists in a function

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
    results = []
    for numbers in lists:
        for item in numbers:
           results.append(item)
    return results


print flatten(n)

#================================================================
#Battleship young generation
from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
guess_row = int(raw_input("Guess Row:"))
guess_col = int(raw_input("Guess Col:"))

print ship_row
print ship_col

if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"
else:
    if guess_row not in range(5) or guess_col not in range(5):
        print "Oops, that's not even in the ocean."
    elif board[guess_row][guess_col] == "X":
        print "You guessed that one already."
    else: 
        print "You missed my battleship!"
        board[guess_row][guess_col] = "X"
        print_board(board)

#================================================================		
#Battleship extended
from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(4):
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif (board[guess_row][guess_col] == "X"):
          print "You guessed that one already."
        else:
           print "You missed my battleship!"
           board[guess_row][guess_col] = "X"
    # Print (turn + 1) here!
    print (turn + 1)
    print_board(board)
    if turn == 3:
        print "Game Over"
		
		
#================================================================				
#while 

num = 1

while num < 11:  # Fill in the condition
    print (num ** 2)
    # Increment num (make sure to do this!)
    num += 1

#================================================================
#lucky numbers

import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
    num = random.randint(1, 6)
    print num
    if num == 5:
        print "Sorry, you lose!"
        break
    count += 1
else:
    print "You win!"	

#================================================================	
#lucky numbers the second

from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
while guesses_left > 0:
    guess = int(raw_input("Your guess: "))
    if guess == random_number:
        print "You win!"
        break
    guesses_left -= 1
else:
    print "You lose!"	
	
#================================================================	
#appending to list
hobbies = []

# Add your code below!
for i in range(3):
    hobby = raw_input("Type your hobby:")
    hobbies.append(hobby)
	
#================================================================
#printing words with for loop

thing = "spam!"

for c in thing:
    print c

word = "eggs!"

# Your code here!
for d in word:
    print d

#================================================================	
#replacig characters using for loop
phrase = "A bird in the hand..."

# Add your for loop
for char in phrase:
    if char == "A" or char == "a":
        print "X",
    else:
        print char,



#Don't delete this print statement!
print

#looping thru dictionary
#================================================================
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
    # Your code here!
    print key,d[key]
	
#================================================================	
#counting as you go without knowing the indexes
choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
    print (index+1), item

#================================================================	
#multiple lists zip
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    # Add your code here!
    if a > b:
        print a
    else:
        print b
		
#================================================================
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    if f == 'tomato':
        print 'A tomato is not a fruit!' # (It actually is.)
    print 'A', f
else:
    print 'A fine selection of fruits!'
	
#================================================================
#integer checker with .0 

def is_int(x):
    y = str(x)
    if (type(x) == int) or ((y[len(y)-2:]) == ".0"):
        return True
    else:
        return False	

#================================================================		
#digit sum

def digit_sum(n):
    m = str(n)
    sum = 0
    for dig in m:
        sum += int(dig)
    return sum   		
	
#================================================================	
#factorial in python

def factorial(x):
    for i in reversed(range(x)):
        if i == 0:
            return x
        else:
            x *= int(i)

#================================================================				
#reversed text
def reverse(text):
    rev=""
    for i in text:
        rev=i+rev
    return rev

print reverse("Python!")

#================================================================	
#anti vowel
def anti_vowel(text):
    avtext = ''
    for c in text:
        if c not in "aeiouAEIOU":
            avtext += c
    return avtext   

print anti_vowel('my anti vowel text to transform')