# Pizza list 4-1
# List of favorite pizzas
favorite_pizzas = ['Pepperoni', 'Margherita', 'BBQ Chicken']

# Loop through the list and print statements
for pizza in favorite_pizzas:
    print(f"I like {pizza} pizza.")

# Additional statement outside the loop
print("I really love pizza!")


# Animals list 4-2
animals = ['Dog', 'Cat', 'Rabbit']

# Loop through the list and print statements
for animal in animals:
    print(f"A {animal} would make a great pet.")

# Additional statement about the common characteristic
print("All of these animals are popular pets.")

# Making Numerical list
# Using range functions

for value in range(1,6):
    print(value) # it will start the sequence of numbers at 0. For example, range(6) would return the numbers from 0 through 5.


# Using range() to Make a List of Numbers

numbers = list(range(1,6))
print(numbers)

# Even numbers list

even_numbers = list(range(2,11,2))
print(even_numbers)

# Squares list

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

# Simple Statistics with a List of Numbers

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# List Comprehensions

squares = [value**2 for value in range(1,11)]
print(squares)

# Counting to Twenty 4-3

for value in range(1,21):
    print(value)

# One-Million 4-4

numbers = list(range(1,1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# Odd Numbers 4-5

odd_numbers = list(range(1,21,2))
print(odd_numbers)

# Summing a Million 4-6

numbers = list(range(1,1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# Threes 4-7

threes = list(range(3,31,3))
print(threes)

# Cubes 4-8

cubes = [value**3 for value in range(1,11)]
print(cubes)

# 10 Cubes 

cubes = [value**3 for value in range(1,11)]
print(cubes)

# Cube Comprehension 4-9

cubes = [value**3 for value in range(1,11)]
print(cubes)

# Slicing cube

cubes = [value**3 for value in range(1,11)]
print(cubes[0:3])
print(cubes[3:7])
print(cubes[7:11])

# Copying a List

cubes = [value**3 for value in range(1,11)]
print(cubes)
print(cubes[0:3])
print(cubes[3:7])
print(cubes[7:11])

# Slicing a List

players = ['Ahmad', 'Hang', 'Maham', 'Usama', 'Alice']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])

# Loop through Slice

players = ['Ahmad', 'Hang', 'Maham', 'Usama', 'Alice']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])


# This doesn't work: Book example
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# Slices 4-10

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)

#  My Pizzas, Your Pizzas 4-11
# 2 Examples
# Original list of favorite pizzas
my_pizzas = ['Pepperoni', 'Margherita', 'BBQ Chicken']

# Make a copy of the list and call it friend_pizzas
friend_pizzas = my_pizzas.copy()

# Add a new pizza to the original list
my_pizzas.append('Hawaiian')

# Add a different pizza to the list friend_pizzas
friend_pizzas.append('Vegetarian')

# Prove that you have two separate lists by printing them
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

# Second one

my_pizzas = ['Pepperoni', 'Margherita', 'BBQ Chicken']
friend_pizzas = my_pizzas[:]

my_pizzas.append('Cheese')
friend_pizzas.append('Hawaiian')

# More Loops 4-12 2 examples
# List of favorite foods
my_foods = ['pizza', 'falafel', 'carrot cake']

# List of friend's favorite foods
friends_foods = ['sushi', 'ramen', 'ice cream']

# Loop through my_foods list and print each food
print("My favorite foods are:")
for food in my_foods:
    print(food)

# Loop through friends_foods list and print each food
print("\nMy friend's favorite foods are:")
for food in friends_foods:
    print(food)


my_pizzas = ['Pepperoni', 'Margherita', 'BBQ Chicken']
friend_pizzas = my_pizzas[:]

my_pizzas.append('Cheese')
friend_pizzas.append('Hawaiian')

# Buffets 4-13

buffets = ['KFC', 'McDonalds', 'Burger King']
print("My favorite buffets are:")
for buffet in buffets:
    print(buffet)
    
# # Tuple of basic foods offered by the buffet-style restaurant
basic_foods = ('pizza', 'pasta', 'salad', 'soup', 'bread')

# Use a for loop to print each food the restaurant offers
print("Original menu:")
for food in basic_foods:
    print(food)

# Try to modify one of the items (this should raise an error)
try:
    basic_foods[0] = 'sushi'
except TypeError as e:
    print(f"\nError: {e}")

# The restaurant changes its menu, replacing two of the items with different foods
basic_foods = ('pizza', 'sushi', 'salad', 'noodles', 'bread')

# Use a for loop to print each of the items on the revised menu
print("\nRevised menu:")
for food in basic_foods:
    print(food)


# Tuple of basic foods offered by the buffet-style restaurant
basic_foods = ('pizza', 'pasta', 'salad', 'soup', 'bread')

# Use a for loop to print each food the restaurant offers
print("Original menu:")
for food in basic_foods:
    print(food)

# Try to modify one of the items (this should raise an error)
try:
    basic_foods[0] = 'sushi'
except TypeError as e:
    print(f"\nError: {e}")

# The restaurant changes its menu, replacing two of the items with different foods
basic_foods = ('pizza', 'sushi', 'salad', 'noodles', 'bread')

# Use a for loop to print each of the items on the revised menu
print("\nRevised menu:")
for food in basic_foods:
    print(food)
    