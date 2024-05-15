#simple message 2-1
# Assigning a message to a variable
message = "Hello, world!"

# Printing the message
print(message)

#simple message 2-2
# Assigning a message to a variable
message = "Hello, world!"

# Printing the initial message
print("Initial message:", message)

# Changing the value of the variable to a new message
message = "How are you today?"

# Printing the new message
print("New message:", message)

#Personal Message
# Define the person's name
name = "Eric"

# Print a message to the person
print("Hello " + name + ", would you like to learn some Python today?")

#Name Cases
# Define the person's name
name = "Mark"

# Print the person's name in lowercase
print("Lowercase:", name.lower())

# Print the person's name in uppercase
print("Uppercase:", name.upper())

# Print the person's name in title case
print("Title case:", name.title())

#Famous Quote
# Define the quote and its author
quote = "A person who never made a mistake never tried anything new."
author = "Albert Einstein"

# Print the quote and its author in the specified format
print(author + " once said, " + '"' + quote + '"')


#Famous Quote 2
# Define the famous person's name
famous_person = "Albert Einstein"

# Define the quote and its author
quote = "A person who never made a mistake never tried anything new."

# Compose the message
message = famous_person + " once said, " + '"' + quote + '"'

# Print the message
print(message)

#Stripping Names
# Define the person's name with whitespace characters
name = "\t\n  John Doe \n\t"

# Print the name with whitespace around it
print("Name with whitespace:", name)

# Print the name using lstrip(), rstrip(), and strip() functions
print("Name using lstrip():", name.lstrip())
print("Name using rstrip():", name.rstrip())
print("Name using strip():", name.strip())


#File Extensions
# Assign the filename to a variable
filename = 'python_notes.txt'

# Find the index of the last '.' character
dot_index = filename.rfind('.')

# Use slicing to get the filename without the extension
filename_without_extension = filename[:dot_index]

# Display the filename without the extension
print("Filename without extension:", filename_without_extension)

#Second example: filename
# Assign the filename to a variable
filename = 'python_notes.txt'

# Use the removesuffix() method to remove the file extension
filename_without_extension = filename.removesuffix('.txt')

# Display the filename without the extension
print("Filename without extension:", filename_without_extension)

#Number 8
print(10 - 2)
print(4 * 2)
print(16 / 2)
print(16 // 2)  # Integer division also results in 8

#Favorite Number
favorite_number = 7
print("My favorite number is:", favorite_number)

# Add comment
# Program Name: FavoriteNumber.py
# Author: [Your Name]
# Date: [Current Date]
# Description: This program demonstrates the use of variables to represent and print a favorite number.

favorite_number = 7  # Assigning the favorite number to the variable
print("My favorite number is:", favorite_number)  # Printing a message revealing the favorite number

# Program Name: Calculator.py
# Author: [Your Name]
# Date: [Current Date]
# Description: This program performs basic arithmetic operations (addition, subtraction, multiplication, division) resulting in the number 8.

print(10 - 2)  # Subtracting to get 8
print(4 * 2)   # Multiplying to get 8
print(16 / 2)  # Dividing to get 8
print(16 // 2) # Integer division also results in 8


#Zen of pythons
import this

# Store the names of your friends in a list
names = ["Alice", "Bob", "Charlie", "David"]

# Print each person's name by accessing each element in the list
for name in names:
    print(name)

# Store the names of your friends in a list
names = ["Alice", "Bob", "Charlie", "David"]

# Print a personalized message to each person in the list
for name in names:
    print(f"Hello {name}, I hope you're having a great day!")


# Create a list of favorite modes of transportation
transportation_modes = ["motorcycle", "car", "bicycle", "bus"]

# Print statements about each item in the list
for mode in transportation_modes:
    print(f"I would like to own a {mode}.")


students = ['ahmad','osama','ashad',23,34,23]
print(students)
#Access Elements
print(students[0].title())
#f string example

message = f"My student name is {students[1].title()}"
print(message)

#Modify Elements example
cars = ['honda', 'nissan', 'toyota', 'tesla','suzuki']
print(cars)

print(cars[2].title())

#modified example
cars[2] = 'bmw'
print(cars)
print(cars[2])

# Add elements
cars.append('foxy')
print(cars)

# Insert elements
cars.insert(1,'Mazda')
print(cars)

# Remove elements
del cars[2]
print(cars)

#POP method
cars.pop(2)
print(cars)

#sir method remove laster elements
popped_method = cars.pop()
print(popped_method)

# Remove pop() method
cars.pop()
print(cars)

#pop method of remove any position elements
pop_method = cars.pop(1)
print(cars)
print(pop_method)



# List of people to invite to dinner
guest_list = ["Albert Einstein", "Leonardo da Vinci", "Marie Curie"]

# Function to send invitation
def send_invitation(person):
    print(f"Dear {person},\nYou are cordially invited to dinner at my place. It would be an honor to have your presence.\nPlease let me know if you can make it.\nSincerely, [Your Name]")

# Loop through the guest list and send invitations
for guest in guest_list:
    send_invitation(guest)

# List of people to invite to dinner
guest_list = ["Albert Einstein", "Leonardo da Vinci", "Marie Curie"]

# Function to send invitation
def send_invitation(person):
    print(f"Dear {person},\nYou are cordially invited to dinner at my place. It would be an honor to have your presence.\nPlease let me know if you can make it.\nSincerely, [Your Name]")

# Function to handle regrets
def handle_regrets(regretted_guest):
    print(f"Unfortunately, {regretted_guest} can't make it to the dinner.")

# Function to send second set of invitations
def send_second_invitations():
    for guest in guest_list:
        send_invitation(guest)

# Initial invitations
for guest in guest_list:
    send_invitation(guest)

# Simulating a regret
regretted_guest = guest_list.pop(1)  # Assuming the second guest can't make it
new_guest = "Isaac Newton"  # New person to invite
guest_list.append(new_guest)

# Print regret message
handle_regrets(regretted_guest)

# Send second set of invitations
print("\nSecond set of invitations:")
send_second_invitations()

# List of people to invite to dinner
guest_list = ["Albert Einstein", "Leonardo da Vinci", "Marie Curie"]

# Function to send invitation
def send_invitation(person):
    print(f"Dear {person},\nYou are cordially invited to dinner at my place. It would be an honor to have your presence.\nPlease let me know if you can make it.\nSincerely, [Your Name]")

# Function to inform about the bigger table
def inform_bigger_table():
    print("Good news! We found a bigger dinner table. There's more space available now.")

# Function to send invitations
def send_invitations():
    for guest in guest_list:
        send_invitation(guest)

# Initial invitations
print("Initial set of invitations:")
send_invitations()
print()

# Inserting one new guest at the beginning
guest_list.insert(0, "Isaac Newton")

# Inserting one new guest in the middle
middle_index = len(guest_list) // 2
guest_list.insert(middle_index, "Nikola Tesla")

# Appending one new guest to the end
guest_list.append("Ada Lovelace")

# Informing about the bigger table
inform_bigger_table()

# Sending new set of invitations
print("\nNew set of invitations:")
send_invitations()

# List of people to invite to dinner
guest_list = ["Albert Einstein", "Leonardo da Vinci", "Marie Curie", "Isaac Newton", "Nikola Tesla", "Ada Lovelace"]

# Function to send invitation
def send_invitation(person):
    print(f"Dear {person},\nYou are cordially invited to dinner at my place. It would be an honor to have your presence.\nPlease let me know if you can make it.\nSincerely, [Your Name]")

# Function to inform about limited space
def inform_limited_space():
    print("Unfortunately, the new dinner table won't arrive in time for the dinner. I can only invite two people for dinner.")

# Function to send invitations
def send_invitations():
    for guest in guest_list:
        send_invitation(guest)

# Inform about limited space
inform_limited_space()

# Remove guests until only two remain
while len(guest_list) > 2:
    removed_guest = guest_list.pop()
    print(f"Sorry {removed_guest}, I can't invite you to dinner.")

# Send invitations to the remaining guests
print("\nInvitations for the two remaining guests:")
send_invitations()

# Remove the last two names from the list
del guest_list[:]
print("\nUpdated guest list after removing all guests:", guest_list)

#organizing lists
cars = ['honda', 'nissan', 'toyota', 'tesla','suzuki']
cars.sort()
print(cars)

cars = ['honda', 'nissan', 'toyota', 'tesla','suzuki']

#Sort() reverse 
cars = ['honda', 'nissan', 'toyota', 'tesla','suzuki']
cars.sort(reverse=True)
print(cars)

#sorting list temporary sorted() function
cars = ['honda', 'nissan', 'toyota', 'tesla','suzuki']
print(sorted(cars))
print(cars)

cars = ['honda', 'nissan', 'toyota', 'tesla','suzuki']

# sir sorted function
print('Original car lists')
print(cars)
print('After sorted function use')
print(sorted(cars))

# Reverse order lists
cars = ['honda', 'nissan', 'toyota', 'tesla','suzuki']
print(cars)
cars.reverse()
print(cars)

# Reverse order lists sir example
cars.append('Audi')
cars.reverse()
print(cars)

#finding the length of the list
cars = ['honda', 'nissan', 'toyota', 'tesla','suzuki']
print(len(cars))

#Avoid error in the list if you do it in minus number it still works acoording to index present
cars = ['honda', 'nissan', 'toyota', 'tesla','suzuki']
print(len(cars))
print(cars[1])

cars = ['honda', 'nissan', 'toyota', 'tesla','suzuki']

# avoid error examples2
print(cars)
print(cars[-1])






