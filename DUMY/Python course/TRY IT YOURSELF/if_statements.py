# Conditional Testing 5-1
# Initializing the variable
car = 'subaru'

# Test 1: True condition
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

# Test 2: False condition
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# Test 3: True condition
print("\nIs car != 'audi'? I predict True.")
print(car != 'audi')

# Test 4: False condition
print("\nIs car != 'subaru'? I predict False.")
print(car != 'subaru')

# Test 5: True condition
print("\nIs car == 'subaru' and car != 'audi'? I predict True.")
print(car == 'subaru' and car != 'audi')

# Test 6: False condition
print("\nIs car == 'subaru' and car == 'audi'? I predict False.")
print(car == 'subaru' and car == 'audi')

# Test 7: True condition
print("\nDoes the car start with 'sub'? I predict True.")
print(car.startswith('sub'))

# Test 8: False condition
print("\nDoes the car start with 'aud'? I predict False.")
print(car.startswith('aud'))

# Test 9: True condition
print("\nIs the length of car == 6? I predict True.")
print(len(car) == 6)

# Test 10: False condition
print("\nIs the length of car == 4? I predict False.")
print(len(car) == 4)


# More Conditionals Test
# Initializing variables
car = 'subaru'
name = 'Alice'
age = 25
height = 170
fruits = ['apple', 'banana', 'cherry']

# Tests for equality and inequality with strings
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car != 'audi'? I predict True.")
print(car != 'audi')

print("\nIs name == 'alice'? I predict False.")
print(name == 'alice')

print("\nIs name != 'Bob'? I predict True.")
print(name != 'Bob')

# Tests using the lower() method
print("\nIs name.lower() == 'alice'? I predict True.")
print(name.lower() == 'alice')

print("\nIs name.lower() != 'alice'? I predict False.")
print(name.lower() != 'alice')

# Numerical tests involving equality and inequality
print("\nIs age == 25? I predict True.")
print(age == 25)

print("\nIs age != 30? I predict True.")
print(age != 30)

print("\nIs height > 160? I predict True.")
print(height > 160)

print("\nIs height < 180? I predict True.")
print(height < 180)

print("\nIs height >= 170? I predict True.")
print(height >= 170)

print("\nIs height <= 160? I predict False.")
print(height <= 160)

# Tests using the and keyword and the or keyword
print("\nIs age > 20 and height > 160? I predict True.")
print(age > 20 and height > 160)

print("\nIs age > 30 and height > 160? I predict False.")
print(age > 30 and height > 160)

print("\nIs age > 20 or height < 160? I predict True.")
print(age > 20 or height < 160)

print("\nIs age < 20 or height < 160? I predict False.")
print(age < 20 or height < 160)

# Test whether an item is in a list
print("\nIs 'apple' in fruits? I predict True.")
print('apple' in fruits)

print("\nIs 'orange' in fruits? I predict False.")
print('orange' in fruits)

# Test whether an item is not in a list
print("\nIs 'grape' not in fruits? I predict True.")
print('grape' not in fruits)

print("\nIs 'banana' not in fruits? I predict False.")
print('banana' not in fruits)

# Aliens Colors 5-3

alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")

# Version of the program that passes the if test
alien_color = 'green'

if alien_color == 'green':
    print("The player just earned 5 points.")

# Version of the program that fails the if test (no output)
alien_color = 'red'

if alien_color == 'green':
    print("The player just earned 5 points.")


# Aliens color 5-4
# Alien color chosen
alien_color = "green"

# If-else chain
if alien_color == "green":
    print("You just earned 5 points for shooting the green alien.")
else:
    print("You just earned 10 points.")

# Running the else block
alien_color = "red"  # Change the color to something other than green

if alien_color == "green":
    print("You just earned 5 points for shooting the green alien.")
else:
    print("You just earned 10 points.")

# Aliens color 5-5
# Version 1: Alien is green
alien_color = "green"

if alien_color == "green":
    print("You just earned 5 points.")
elif alien_color == "yellow":
    print("You just earned 10 points.")
else:
    print("You just earned 15 points.")

# Version 2: Alien is yellow
alien_color = "yellow"

if alien_color == "green":
    print("You just earned 5 points.")
elif alien_color == "yellow":
    print("You just earned 10 points.")
else:
    print("You just earned 15 points.")

# Version 3: Alien is red
alien_color = "red"

if alien_color == "green":
    print("You just earned 5 points.")
elif alien_color == "yellow":
    print("You just earned 10 points.")
else:
    print("You just earned 15 points.")

# Stages of life 5-6
# Set the age of the person
age = 25

# Determine the person's stage of life using if-elif-else chain
if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")

# Favorite fruit
# Make a list of favorite fruits
favorite_fruits = ["apple", "banana", "orange"]

# Check if certain fruits are in the list
if "apple" in favorite_fruits:
    print("You really like apples!")

if "banana" in favorite_fruits:
    print("You really like bananas!")

if "orange" in favorite_fruits:
    print("You really like oranges!")

if "grape" in favorite_fruits:
    print("You really like grapes!")

if "kiwi" in favorite_fruits:
    print("You really like kiwis!")

# Hello Admin 5-8
# List of usernames
usernames = ["admin", "jaden", "emma", "alex", "sophia"]

# Loop through the list and print greetings
for username in usernames:
    if username == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.capitalize()}, thank you for logging in again.")

# No-Users 5-9
# List of usernames
usernames = ["admin", "jaden", "emma", "alex", "sophia"]

# Check if the list of users is not empty
if usernames:
    # Loop through the list and print greetings
    for username in usernames:
        if username == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username.capitalize()}, thank you for logging in again.")
else:
    print("We need to find some users!")

# Remove all usernames from the list
usernames = []

# Check if the list of users is not empty
if usernames:
    # Loop through the list and print greetings
    for username in usernames:
        if username == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username.capitalize()}, thank you for logging in again.")
else:
    print("We need to find some users!")


# Checking Users names 5-10
# List of current users
current_users = ["john", "emma", "alex", "sophia", "michael"]

# List of new users
new_users = ["Jaden", "sophia", "lucas", "Ella", "emma"]

# Convert current_users to lowercase
current_users_lower = [user.lower() for user in current_users]

# Loop through new_users to check availability
for new_user in new_users:
    # Convert new_user to lowercase for case-insensitive comparison
    new_user_lower = new_user.lower()
    
    # Check if new username is already taken
    if new_user_lower in current_users_lower:
        print(f"Sorry, the username '{new_user}' is already taken. Please choose a different username.")
    else:
        print(f"The username '{new_user}' is available.")

# Ordinal Numbers 5-11
# Store numbers 1 through 9 in a list
numbers = list(range(1, 10))

# Loop through the list
for number in numbers:
    # Use if-elif-else chain to print proper ordinal ending
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")

# Styling if statements
# Example 1: Checking if a number is positive, negative, or zero
number = 5

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Example 2: Checking if a number is even or odd
number = 7

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Example 3: Checking if a person can ride a rollercoaster based on height
height = 150  # in centimeters

if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you are not tall enough to ride the rollercoaster.")

# Example 4: Checking if a number is divisible by another number
numerator = 15
denominator = 3

if numerator % denominator == 0:
    print("The numerator is divisible by the denominator.")
else:
    print("The numerator is not divisible by the denominator.")



