 # Rental car  7-1
def rental_car():
    car_type = input("What kind of rental car would you like? ")
    
    print(f"Let me see if I can find you a {car_type.title()}.")

rental_car()

# Restaurant seating 7-2
def check_table_availability():
    try:
        group_size = int(input("How many people are in your dinner group? "))
        
        # Check if the group size is more than eight
        if group_size > 8:
            print("You’ll have to wait for a table.")
        else:
            print("Your table is ready.")
    except ValueError:
        print("Please enter a valid number.")

check_table_availability()

# MULTIPLES OF TEN 7-3
def check_multiple_of_10():
    # Ask the user for a number
    try:
        number = int(input("Please enter a number: "))
        
        # Check if the number is a multiple of 10
        if number % 10 == 0:
            print(f"The number {number} is a multiple of 10.")
        else:
            print(f"The number {number} is not a multiple of 10.")
    except ValueError:
        print("Please enter a valid number.")

check_multiple_of_10()

# Pizza toppings 7-4
while True:
    # Prompt the user to enter a topping
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    
    # Check if the user wants to quit
    if topping.lower() == 'quit':
        print("Finished adding toppings to your pizza!")
        break
    else:
        # Print message saying the topping will be added
        print(f"Adding {topping} to your pizza.")
        
# Movie tickets 7-5
# Loop to prompt user for their age and determine ticket price
while True:
    # Prompt the user to enter their age
    age = input("Enter your age (or 'quit' to finish): ")
    
    # Check if the user wants to quit
    if age.lower() == 'quit':
        print("Finished processing ticket prices.")
        break
    
    # Convert the input to an integer
    try:
        age = int(age)
    except ValueError:
        print("Please enter a valid age or 'quit' to finish.")
        continue
    
    # Determine the ticket price based on age
    if age < 3:
        price = "free"
    elif 3 <= age <= 12:
        price = "$10"
    else:
        price = "$15"
    
    # Print the ticket price
    print(f"The cost of the movie ticket is {price}.")        

# Three Exits 7-6
# Using a conditional test in the while statement to stop the loop

age = ""
while age != "quit":
    age = input("Enter your age (or 'quit' to finish): ")
    
    if age == "quit":
        print("Finished processing ticket prices.")
        continue
    
    try:
        age = int(age)
    except ValueError:
        print("Please enter a valid age or 'quit' to finish.")
        continue
    
    if age < 3:
        price = "free"
    elif 3 <= age <= 12:
        price = "$10"
    else:
        price = "$15"
    
    print(f"The cost of the movie ticket is {price}.")

# Using an active variable to control how long the loop runs

active = True
while active:
    age = input("Enter your age (or 'quit' to finish): ")
    
    if age.lower() == 'quit':
        print("Finished processing ticket prices.")
        active = False
    else:
        try:
            age = int(age)
        except ValueError:
            print("Please enter a valid age or 'quit' to finish.")
            continue
        
        if age < 3:
            price = "free"
        elif 3 <= age <= 12:
            price = "$10"
        else:
            price = "$15"
        
        print(f"The cost of the movie ticket is {price}.")

# Using a break statement to exit the loop when the user enters a 'quit' value

while True:
    age = input("Enter your age (or 'quit' to finish): ")
    
    if age.lower() == 'quit':
        print("Finished processing ticket prices.")
        break
    
    try:
        age = int(age)
    except ValueError:
        print("Please enter a valid age or 'quit' to finish.")
        continue
    
    if age < 3:
        price = "free"
    elif 3 <= age <= 12:
        price = "$10"
    else:
        price = "$15"
    
    print(f"The cost of the movie ticket is {price}.")
    
    
# infinity 7-7 it will stop when press CTRL-C
# An infinite loop
# while True:
#     print("This loop will run forever. Press CTRL-C to stop.")
    
# Deli 7-8

# List of sandwich orders
sandwich_orders = ["tuna", "ham", "turkey", "veggie", "chicken", "beef"]
# Empty list to hold finished sandwiches
finished_sandwiches = []

# Loop through the list of sandwich orders
while sandwich_orders:
    # Remove the first sandwich from the list
    current_sandwich = sandwich_orders.pop(0)
    # Print a message for each order
    print(f"I made your {current_sandwich} sandwich.")
    # Move the sandwich to the list of finished sandwiches
    finished_sandwiches.append(current_sandwich)

# Print a message listing each sandwich that was made
print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"{sandwich.capitalize()} sandwich")


# No Pastrami 7-9
# List of sandwich orders
sandwich_orders = ["tuna", "pastrami", "ham", "pastrami", "turkey", "pastrami", "veggie", "chicken", "beef"]
# Empty list to hold finished sandwiches
finished_sandwiches = []

# Print a message that the deli has run out of pastrami
print("The deli has run out of pastrami.")

# Remove all occurrences of 'pastrami' from the sandwich orders list
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Loop through the list of remaining sandwich orders
while sandwich_orders:
    # Remove the first sandwich from the list
    current_sandwich = sandwich_orders.pop(0)
    # Print a message for each order
    print(f"I made your {current_sandwich} sandwich.")
    # Move the sandwich to the list of finished sandwiches
    finished_sandwiches.append(current_sandwich)

# Print a message listing each sandwich that was made
print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"{sandwich.capitalize()} sandwich")
    

# Dream vacation 7-1    
# Dictionary to store poll results
dream_vacations = {}

# Flag to indicate polling is active
polling_active = True

while polling_active:
    # Prompt the user for their name and dream vacation destination
    name = input("\nWhat is your name? ")
    destination = input("If you could visit one place in the world, where would you go? ")
    
    # Store the response in the dictionary
    dream_vacations[name] = destination
    
    # Ask if another user would like to take the poll
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() != 'yes':
        polling_active = False

# Polling is complete, print the results
print("\n--- Poll Results ---")
for name, destination in dream_vacations.items():
    print(f"{name} would like to visit {destination}.")
    
    
