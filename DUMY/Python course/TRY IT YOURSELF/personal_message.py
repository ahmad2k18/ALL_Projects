# personal message 2-3

name = "Eric"

print("Hello " + name + ", would you like to learn some python today? ")

# Name cases 2-4

name1 = "Mark"

print ("lowercase:" , name1.lower())

print ("uppercase:" , name1.upper())

print ("title case:" , name1.title())

# Famous quote 2-5
quote = "A person who never made a mistake never tried anything new."
author = "Albert Einstein"

print(author + " once said, " + '"' + quote + '"')

# Famous quote 2-6
famous_person = "Albert Einstein"
message = "A person who never made a mistake never tried anything new."

print(famous_person + " once said, " + '"' + message + '"')

# Stripping names 2-7
name2 = "  Eric  "

print(name2)

print(name2.lstrip())

# Define the person's name with whitespace characters
name = "\t\n  John Doe \n\t"

# Print the name with whitespace around it
print("Name with whitespace:", name)

# Print the name using lstrip(), rstrip(), and strip() functions
print("Name using lstrip():", name.lstrip())
print("Name using rstrip():", name.rstrip())
print("Name using strip():", name.strip())

# File Extenstion 2-8
filename = "programming.txt"

print(filename.split("."))

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

# Numbers integer 2-9
print(10 - 2)
print(4 * 2)
print(16 / 2)
print(16 // 2)  # Integer division also results in 8

# Integer and float 2-10
print(0.3 + 0.5)
print(2.4 * 2.5)
print(16 / 2)
print(16 // 2)  # Integer division also results in 8
print(16 / 2.0)

# Underscores in numbers 2-11
print(1_000_000_000)
print(100_000_000)
print(1000000000)

universe_age = 14_000_000_000
print(universe_age)

# Multiple assignment 2-12
x, y, z = 1, 2, 3
print(x, y, z)

# Constants 2-13
PI = 3.141592653589793
print(PI)

# Favorite number 2-14
favorite_number = 7
print("My favorite number is " + str(favorite_number) + ".")

# Author: [Your Name] AI HELP//
# Date: [Current Date]

# Program 1: Simple Calculator

# This program takes two numbers as input and performs addition, subtraction, multiplication, and division operations.

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    return x / y

# Main function
def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        if num2 != 0:
            print("Result:", divide(num1, num2))
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()

# Zen of Python 2-15
import this


