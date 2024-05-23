# Restaurant 9-1

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

# Create an instance of the Restaurant class
restaurant = Restaurant("The Gourmet Kitchen", "Italian")

# Print the two attributes individually
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Call both methods
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Three-Restaurants 9-2

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

# Create three different instances of the Restaurant class
restaurant1 = Restaurant("The Gourmet Kitchen", "Italian")
restaurant2 = Restaurant("Spice Symphony", "Indian")
restaurant3 = Restaurant("Sushi World", "Japanese")

# Call describe_restaurant() for each instance
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


# Users 9-3

class User:
    def __init__(self, first_name, last_name, age, email, username):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.username = username
    
    def describe_user(self):
        print(f"User Profile:")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Username: {self.username}")
    
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!")

# Create several instances of the User class
user1 = User("Alice", "Johnson", 28, "alice.johnson@example.com", "alice")
user2 = User("Bob", "Smith", 34, "bob.smith@example.com", "bob smith")
user3 = User("Charlie", "Brown", 22, "charlie.brown@example.com", "charlie")

# Call describe_user() and greet_user() for each instance
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
 
# Number Served 9-4
# Initial Restaurant class
class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Default value

    def describe_restaurant(self):
        print(f"The restaurant {self.name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"The restaurant {self.name} is now open.")
        
    def set_number_served(self, number):
        """Set the number of customers that have been served."""
        self.number_served = number

    def increment_number_served(self, number):
        """Increment the number of customers served."""
        self.number_served += number

# Create an instance called restaurant
restaurant = Restaurant("Pasta Palace", "Italian")

# Print the number of customers the restaurant has served
print(f"Number of customers served: {restaurant.number_served}")

# Change the value and print it again
restaurant.number_served = 50
print(f"Number of customers served: {restaurant.number_served}")

# Use set_number_served() to set a new number and print the value again
restaurant.set_number_served(75)
print(f"Number of customers served: {restaurant.number_served}")

# Use increment_number_served() to increment the number of customers served
restaurant.increment_number_served(30)
print(f"Number of customers served: {restaurant.number_served}")


# Login Attempts 9-5

# Initial User class 
class User:
    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.login_attempts = 0  # Initialize login_attempts to 0

    def describe_user(self):
        print(f"User {self.username}:")
        print(f"  First Name: {self.first_name}")
        print(f"  Last Name: {self.last_name}")
        print(f"  Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the value of login_attempts to 0."""
        self.login_attempts = 0

# Make an instance of the User class
user = User("John", "Doe", "johndoe", "johndoe@example.com")

# Increment login attempts several times
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Print the value of login_attempts to make sure it was incremented properly
print(f"Login attempts: {user.login_attempts}")

# Reset login attempts
user.reset_login_attempts()

# Print login_attempts again to make sure it was reset to 0
print(f"Login attempts after reset: {user.login_attempts}")

# Ice Cream Stand 9-6

# Assuming the Restaurant class

class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"The restaurant {self.name} serves {self.cuisine_type} cuisine.")
    
    def open_restaurant(self):
        print(f"The restaurant {self.name} is now open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

# Now, define the IceCreamStand class that inherits from Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type, flavors):
        super().__init__(name, cuisine_type)
        self.flavors = flavors
    
    def display_flavors(self):
        print("We have the following ice cream flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

# Create an instance of IceCreamStand and call the method to display flavors

my_ice_cream_stand = IceCreamStand("Sweet Treats", "Ice Cream", ["Vanilla", "Chocolate", "Strawberry", "Mint Chocolate Chip"])
my_ice_cream_stand.describe_restaurant()
my_ice_cream_stand.display_flavors()

# Admin 9-7

# Assuming the User class

class User:
    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"User {self.username}:")
        print(f"  Full name: {self.first_name} {self.last_name}")
        print(f"  Email: {self.email}")
    
    def greet_user(self):
        print(f"Hello, {self.username}!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

# Now, define the Admin class that inherits from User

class Admin(User):
    def __init__(self, first_name, last_name, username, email, privileges):
        super().__init__(first_name, last_name, username, email)
        self.privileges = privileges
    
    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

# Create an instance of Admin and call the method to display privileges

admin_user = Admin("Alice", "Smith", "admin_alice", "alice@example.com", 
                   ["can add post", "can delete post", "can ban user"])
admin_user.describe_user()
admin_user.show_privileges()

#  Privileges 9-8

# Assuming the User class
class User:
    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"User {self.username}:")
        print(f"  Full name: {self.first_name} {self.last_name}")
        print(f"  Email: {self.email}")
    
    def greet_user(self):
        print(f"Hello, {self.username}!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

# Define the Privileges class

class Privileges:
    def __init__(self, privileges=[]):
        self.privileges = privileges
    
    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

# Now, define the Admin class that inherits from User and includes an instance of Privileges

class Admin(User):
    def __init__(self, first_name, last_name, username, email, privileges=[]):
        super().__init__(first_name, last_name, username, email)
        self.privileges = Privileges(privileges)

# Create an instance of Admin and use the method to show privileges

admin_user = Admin("Alice", "Smith", "admin_alice", "alice@example.com", 
                   ["can add post", "can delete post", "can ban user"])
admin_user.describe_user()
admin_user.privileges.show_privileges()


# Battery Upgrade 9-9

# Assuming the electric_car.py module contains the following classes:

class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        message = f"This car can go approximately {range} miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65
            print("Battery upgraded to 65 kWh.")
        else:
            print("Battery is already upgraded.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


# Create an instance of ElectricCar and use the methods
my_tesla = ElectricCar('tesla', 'model s', 2024)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# Upgrade the battery and check the range again
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# Dice 9-13

import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides
        
    def roll_die(self):
        print("Rolling a", self.sides, "-sided die:")
        for _ in range(10):
            print(random.randint(1, self.sides), end=' ')
        print()

# Create a 6-sided die and roll it 10 times
six_sided_die = Die()
six_sided_die.roll_die()

# Create a 10-sided die and roll it 10 times
ten_sided_die = Die(sides=10)
ten_sided_die.roll_die()

# Create a 20-sided die and roll it 10 times
twenty_sided_die = Die(sides=20)
twenty_sided_die.roll_die()


# Lottery 9-14

import random

# Define a list containing numbers and letters
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Randomly select 4 items from the list
selected_items = random.sample(data, 4)

# Check if all selected items are numbers or letters
if all(isinstance(item, int) for item in selected_items):
    message = "Congratulations! Any ticket matching these 4 numbers wins a prize: "
elif all(isinstance(item, str) for item in selected_items):
    message = "Congratulations! Any ticket matching these 4 letters wins a prize: "
else:
    message = "Congratulations! Any ticket matching these 4 numbers or letters wins a prize: "

# Print the selected items and the message
print("Selected items:", selected_items)
print(message)

# Lottery Analysis 9-15

import random

# Define a list containing numbers and letters
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Define your ticket
my_ticket = [1, 'A', 3, 5]

# Initialize a counter for the number of attempts
attempts = 0

# Simulate pulling numbers until your ticket wins
while True:
    attempts += 1
    # Randomly select 4 items from the list
    selected_items = random.sample(data, 4)
    # Check if the selected items match your ticket
    if selected_items == my_ticket:
        break

# Print the number of attempts needed to win
print("It took", attempts, "attempts to win with ticket:", my_ticket)


# Python Module of the week 9-16

import random

# Generate a random integer between 1 and 10 (inclusive)
random_number = random.randint(1, 10)
print("Random number:", random_number)

# Generate a random floating-point number between 0 and 1
random_float = random.random()
print("Random float:", random_float)

# Generate a random floating-point number between a specified range
random_float_range = random.uniform(2.5, 7.5)
print("Random float in range:", random_float_range)

# Shuffle a list randomly
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print("Shuffled list:", my_list)

# Choose a random element from a sequence
my_sequence = ['apple', 'banana', 'cherry', 'date']
random_element = random.choice(my_sequence)
print("Random element:", random_element)

# Generate a random sample from a population
my_population = list(range(1, 11))  # Population from 1 to 10
random_sample = random.sample(my_population, 3)
print("Random sample:", random_sample)

