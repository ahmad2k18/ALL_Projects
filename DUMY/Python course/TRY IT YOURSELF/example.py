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
