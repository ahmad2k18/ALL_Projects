# Learning Python 10-1

# Create and write to learning_python.txt
with open('learning_python.txt', 'w') as file:
    file.write("In Python you can work with variables.\n")
    file.write("In Python you can create functions.\n")
    file.write("In Python you can use loops.\n")
    file.write("In Python you can handle files.\n")


# Read and print the content of learning_python.txt

# Method 1: Read the entire file at once
with open('learning_python.txt', 'r') as file:
    content = file.read()
    print("Reading entire file at once:")
    print(content)

# Method 2: Read the file line by line and store lines in a list
with open('learning_python.txt', 'r') as file:
    lines = file.readlines()

print("Reading file line by line:")
for line in lines:
    print(line, end='')


# Step 1: Create the learning_python.txt file
with open('learning_python.txt', 'w') as file:
    file.write("In Python you can work with variables.\n")
    file.write("In Python you can create functions.\n")
    file.write("In Python you can use loops.\n")
    file.write("In Python you can handle files.\n")

# Step 2: Read and print the file content using two methods

# Method 1: Read the entire file at once
with open('learning_python.txt', 'r') as file:
    content = file.read()
    print("Reading entire file at once:")
    print(content)

# Method 2: Read the file line by line and store lines in a list
with open('learning_python.txt', 'r') as file:
    lines = file.readlines()

print("Reading file line by line:")
for line in lines:
    print(line, end='')

# Learning C 10-2

# Define the name of the file
filename = 'learning_python.txt'

# Define the word to be replaced and its replacement
original_word = 'Python'
replacement_word = 'C'

# Open the file and process each line
with open(filename, 'r') as file:
    for line in file:
        # Replace the original word with the replacement word
        modified_line = line.replace(original_word, replacement_word)
        # Print the modified line
        print(modified_line, end='')

# Simpler Code 10-3

# Original file_reader.py script
filename = 'learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read()
    
lines = contents.splitlines()
for line in lines:
    print(line)


# Updated file_reader.py script
filename = 'learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read()
    
for line in contents.splitlines():
    print(line)
 
 
# Guest 10-4

# Prompt the user for their name
name = input("Please enter your name: Ahmad ")

# Define the filename
filename = 'guest.txt'

# Open the file in write mode and write the name to it
with open(filename, 'w') as file:
    file.write(name)

print(f"Your name has been written to {filename}.")



# Guest Book 10-5

# Define the filename
filename = 'guest_book.txt'

print("Enter 'quit' to stop entering names.")

# Open the file in append mode
with open(filename, 'a') as file:
    while True:
        # Prompt the user for their name
        name = input("Please enter your name:Ahmad ")
        
        # Check if the user wants to quit
        if name.lower() == 'quit':
            break
        
        # Write the name to the file with a newline
        file.write(name + '\n')
        print(f"Hello, {name}! Your name has been added to the guest book.")

print(f"All names have been written to {filename}.")

# Addition 10-6

def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("That's not a valid number. Please try again.")

def main():
    print("This program adds two numbers.")
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    
    result = num1 + num2
    print(f"The result of adding {num1} and {num2} is {result}.")

if __name__ == "__main__":
    main()


# Addition Calculator 10-7 it works just commented for the terminal

# def get_number(prompt):
#     while True:
#         try:
#             return int(input(prompt))
#         except ValueError:
#             print("That's not a valid number. Please try again.")

# def main():
#     while True:
#         print("This program adds two numbers.")
#         num1 = get_number("Enter the first number:5 ")
#         num2 = get_number("Enter the second number:6 ")

#         result = num1 + num2
#         print(f"The result of adding {num1} and {num2} is {result}.")

#         again = input("Would you like to add two more numbers? (yes/no): ").strip().lower()
#         if again != 'yes':
#             print("Goodbye!")
#             break

# if __name__ == "__main__":
#     main()


# Cats and Dogs 10-8

# Create cats.txt
with open('cats.txt', 'w') as file:
    file.write("Whiskers\n")
    file.write("Paws\n")
    file.write("Shadow\n")

# Create dogs.txt
with open('dogs.txt', 'w') as file:
    file.write("Rex\n")
    file.write("Buddy\n")
    file.write("Max\n")


def read_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(f"Contents of {filename}:\n{contents}")
    except FileNotFoundError:
        print(f"Sorry, the file {filename} was not found.")

def main():
    filenames = ['cats.txt', 'dogs.txt']
    
    for filename in filenames:
        read_file(filename)

if __name__ == "__main__":
    main()
 
 
# Silent Cats and Dogs 10-9

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(f"Contents of {filename}:\n{contents}")
    except FileNotFoundError:
        # Fail silently if the file is not found
        pass

def main():
    filenames = ['cats.txt', 'dogs.txt']
    
    for filename in filenames:
        read_file(filename)

if __name__ == "__main__":
    main()


# Common words 10-10 it doesn't work cause i dont have that project DIRECTORY

# import os

# def count_word_occurrences(file_path, word):
#     """Count occurrences of a word in a file."""
#     with open(file_path, 'r', encoding='utf-8') as file:
#         text = file.read().lower()  # Convert text to lowercase to make the count case-insensitive
#     return text.count(word)

# def analyze_texts(directory):
#     """Analyze text files in the given directory."""
#     results = {}
#     for filename in os.listdir(directory):
#         if filename.endswith('.txt'):
#             file_path = os.path.join(directory, filename)
#             count_the = count_word_occurrences(file_path, 'the')
#             count_the_space = count_word_occurrences(file_path, 'the ')
#             results[filename] = {'the': count_the, 'the ': count_the_space}
#     return results

# def print_results(results):
#     """Print the results in a readable format."""
#     for filename, counts in results.items():
#         print(f"File: {filename}")
#         print(f"Occurrences of 'the': {counts['the']}")
#         print(f"Occurrences of 'the ': {counts['the ']}")
#         print()

# # Directory containing text files from Project Gutenberg
# directory = 'path_to_your_text_files_directory'

# # Analyze the text files and print the results
# results = analyze_texts(directory)
# print_results(results)
 
 
# Favorite Number 10-11

import json

def store_favorite_number():
    favorite_number = input("What's your favorite number? ")
    filename = 'favorite_number.json'
    with open(filename, 'w') as file:
        json.dump(favorite_number, file)
    print("Favorite number stored successfully!")

if __name__ == "__main__":
    store_favorite_number()


import json

def read_favorite_number():
    filename = 'favorite_number.json'
    with open(filename) as file:
        favorite_number = json.load(file)
    print("I know your favorite number! It's", favorite_number)

if __name__ == "__main__":
    read_favorite_number()


# Favorite number remembered 10-12

import json

def store_favorite_number():
    favorite_number = input("What's your favorite number? ")
    filename = 'favorite_number.json'
    with open(filename, 'w') as file:
        json.dump(favorite_number, file)
    print("Favorite number stored successfully!")

def read_favorite_number():
    filename = 'favorite_number.json'
    try:
        with open(filename) as file:
            favorite_number = json.load(file)
        print("I know your favorite number! It's", favorite_number)
    except FileNotFoundError:
        store_favorite_number()

if __name__ == "__main__":
    read_favorite_number()
 
 
# User Dictionary 10-13

import json

def get_user_info():
    user_info = {}
    user_info['username'] = input("Enter your username: ")
    user_info['first_name'] = input("Enter your first name: ")
    user_info['last_name'] = input("Enter your last name: ")
    return user_info

def store_user_info(user_info):
    filename = 'user_info.json'
    with open(filename, 'w') as file:
        json.dump(user_info, file)
    print("User information stored successfully!")

def get_stored_user_info():
    try:
        filename = 'user_info.json'
        with open(filename) as file:
            user_info = json.load(file)
        return user_info
    except FileNotFoundError:
        return None

def print_user_summary(user_info):
    if user_info:
        print("User Information Summary:")
        for key, value in user_info.items():
            print(f"{key.title()}: {value}")
    else:
        print("No user information found.")

def remember_user():
    user_info = get_stored_user_info()
    if user_info:
        print("Welcome back, " + user_info['username'] + "!")
    else:
        print("Welcome! Let's get some information about you.")
        user_info = get_user_info()
        store_user_info(user_info)

    print_user_summary(user_info)

if __name__ == "__main__":
    remember_user()
 

# Verify User 10-14 

import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        correct_username = input(f"Is {username} your username? (yes/no) ").lower()
        if correct_username == 'no':
            username = get_new_username()
        else:
            print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()
