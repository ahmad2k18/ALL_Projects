cars = ['tesla', 'audi','honda','suzuki']
for car in cars:
    if car == 'tesla':
        print(car.upper())
    else:
        print(car.title())

# Defining variables for testing
number = 10
string = "hello"
boolean = True
list1 = [1, 2, 3]
dict1 = {"key": "value"}

# Testing equality
print("Is number == 10? I predict True.")
print(number == 10)

print("\nIs string == 'hello'? I predict True.")
print(string == "hello")

print("\nIs boolean == True? I predict True.")
print(boolean == False)

print("\nIs list1 == [1, 2, 3]? I predict True.")
print(list1 == [0, 2, 3])

print("\nIs dict1 == {'key': 'value'}? I predict True.")
print(dict1 == {"key": "value"})

# Testing inequality
print("\nIs number != 5? I predict True.")
print(number != 5)

print("\nIs string != 'world'? I predict True.")
print(string != "world")

print("\nIs boolean != False? I predict True.")
print(boolean != False)

print("\nIs list1 != [4, 5, 6]? I predict True.")
print(list1 != [4, 5, 6])

print("\nIs dict1 != {'key': 'data'}? I predict True.")
print(dict1 != {"key": "data"})

# if statement WITH VOTING
age = 17
if age >= 18:
    print("You are old enough to vote!")
else:
    print("Sorry, you are too young to vote.")
    
# Elif age
age = 12
if age >=12:
    print("You are old enough to vote!")
elif age >=18:
    print("You are old enough to vote, but not old enough to drink.")
else:
    print("Sorry, you are too young to vote.") 

alien_color = 'green'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points.")

alien_color = 'red'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points.")

alien_color = 'green'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points for shooting the alien.")
else:
    print("Congratulations! You just earned 10 points.")

alien_color = 'red'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points for shooting the alien.")
else:
    print("Congratulations! You just earned 10 points.")

alien_color = 'green'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points.")
elif alien_color == 'yellow':
    print("Congratulations! You just earned 10 points.")
else:
    print("Congratulations! You just earned 15 points.")

alien_color = 'yellow'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points.")
elif alien_color == 'yellow':
    print("Congratulations! You just earned 10 points.")
else:
    print("Congratulations! You just earned 15 points.")
        