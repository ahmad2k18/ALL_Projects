# Message 8-1
# function display_message
def display_message():
    print("I am learning about functions and how to use them in Python in this chapter.")

display_message()

# Favorite book 8-2
#  function favorite_book
def favorite_book(title):
    print(f"One of my favorite books is {title}.")

favorite_book("Alice in Wonderland")

# T-shirts 8-3
# function make_shirt
def make_shirt(size, message):
    print(f"The shirt size is {size} and the message printed on it is: '{message}'")

# positional arguments
make_shirt("Large", "I love Python")

# using keyword arguments
make_shirt(size="Medium", message="Coding is fun!")

# Large shirts 8-4
# function make_shirt with default parameters
def make_shirt(size="Large", message="I love Python"):
    print(f"The shirt size is {size} and the message printed on it is: '{message}'")

# large shirt with the default message
make_shirt()

# medium shirt with the default message
make_shirt(size="Medium")

#shirt of any size with a different message
make_shirt(size="Small", message="Python rocks!")

# cities 8-5
# Define the function describe_city with a default parameter for the country
def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")

# function for three different cities
describe_city("Reykjavik", "Iceland")
describe_city("Tokyo", "Japan")
describe_city("Paris", "France")

# city names 8-6
# function city_country
def city_country(city, country):
    return f"{city.title()}, {country.title()}"

# function with three city-country pairs
print(city_country("santiago", "chile"))
print(city_country("tokyo", "japan"))
print(city_country("paris", "france"))

# Album 8-7
# function make_album
def make_album(artist, title, songs=None):
    album = {'artist': artist, 'title': title}
    if songs:
        album['songs'] = songs
    return album

# representing different albums
album1 = make_album("Artist 1", "Album 1")
album2 = make_album("Artist 2", "Album 2", songs=12)
album3 = make_album("Artist 3", "Album 3")

print(album1)
print(album2)
print(album3)

# users albums 8-8
# function make_album
def make_album(artist, title, songs=None):
    album = {'artist': artist, 'title': title}
    if songs:
        album['songs'] = songs
    return album

# Define a quit value
quit_value = 'quit'

while True:
    # Prompt the user to enter the artist and title of an album
    artist = input("Enter the artist of the album (or 'quit' to exit): ")
    if artist.lower() == quit_value:
        break
    title = input("Enter the title of the album (or 'quit' to exit): ")
    if title.lower() == quit_value:
        break

    album_info = make_album(artist, title)
    print(album_info)


# Messages 8-9
def show_messages(messages):
    """Print each message in the list of messages."""
    for message in messages:
        print(message)

# List of text messages
messages = [
    "Hello, world!",
    "Python is fun.",
    "Let's write some code.",
    "Have a great day!",
    "Keep learning new things."
]

show_messages(messages)

# Sending messages 8-10
def show_messages(messages):
    """Print each message in the list of messages."""
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Print each message and move it to the sent_messages list."""
    while messages:
        current_message = messages.pop(0)  # Remove the message from messages
        print(current_message)             # Print the message
        sent_messages.append(current_message)  # Add it to sent_messages

# List of text messages
messages = [
    "Hello, world!",
    "Python is fun.",
    "Let's write some code.",
    "Have a great day!",
    "Keep learning new things."
]

# List hold sent messages
sent_messages = []

# list of messages
send_messages(messages, sent_messages)

# Print both lists to verify the messages
print("Original messages list (should be empty):", messages)
print("Sent messages list:", sent_messages)

# Archived messages 8-11
def show_messages(messages):
    """Print each message in the list of messages."""
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Print each message and move it to the sent_messages list."""
    while messages:
        current_message = messages.pop(0)  # Remove the message from messages
        print(current_message)             # Print the message
        sent_messages.append(current_message)  # Add it to sent_messages

# List of text messages
messages = [
    "Hello, world!",
    "Python is fun.",
    "Let's write some code.",
    "Have a great day!",
    "Keep learning new things."
]

# Make a copy of the list of messages
messages_copy = messages[:]

# hold sent messages
sent_messages = []

#copy of the list of messages
send_messages(messages_copy, sent_messages)

# Print both lists to verify the original list
print("Original messages list:", messages)
print("Sent messages list:", sent_messages)


# Sandwiches 8-12
def make_sandwich(*items):
    """Print a summary of the sandwich that is being ordered."""
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

# Call the function three times with different numbers of arguments
make_sandwich('ham', 'cheese', 'lettuce')
make_sandwich('turkey', 'bacon', 'avocado', 'tomato')
make_sandwich('peanut butter', 'jelly')

# User Profile 8-13
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

# EXAMPLE 2
# from user_profile import build_profile

# # Building a profile with first and last names and three other key-value pairs
# my_profile = build_profile('John', 'Doe', location='New York', field='Software Development', hobby='Photography')

# Print the profile
# print(my_profile)

# EXAMPLE 3
# # Assuming this is from user_profile.py
# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user."""
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile

# Building a profile with first and last names and three other key-value pairs
my_profile = build_profile('John', 'Doe', location='New York', field='Software Development', hobby='Photography')

# Print the profile
print(my_profile)


# Cars 8-14
def make_car(manufacturer, model, **car_info):
    """Build a dictionary containing everything we know about a car."""
    car = {
        'manufacturer': manufacturer,
        'model': model,
    }
    for key, value in car_info.items():
        car[key] = value
    return car

#  required information and additional key-value pairs
car = make_car('subaru', 'outback', color='blue', tow_package=True)

#  verify the information is stored correctly
print(car)


# styling functions 8-17
# 1st Program [ Fibonacci Sequence ]
def fibonacci(n):
    """
    Generate Fibonacci sequence up to n terms.

    Parameters:
    n (int): Number of terms in the Fibonacci sequence.

    Returns:
    list: A list containing the Fibonacci sequence.
    """
    fib_sequence = []
    a, b = 0, 1
    while len(fib_sequence) < n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def main():
    terms = 10
    print(f"Fibonacci sequence up to {terms} terms: {fibonacci(terms)}")

if __name__ == "__main__":
    main()


# 2nd Program [ Prime Number Checker ]

def is_prime(number):
    """
    Check if a number is a prime number.

    Parameters:
    number (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def main():
    num = 29
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

if __name__ == "__main__":
    main()

# 3rd Program [ Factorial Calculation ]

def factorial(n):
    """
    Calculate the factorial of a number.

    Parameters:
    n (int): The number to calculate the factorial of.

    Returns:
    int: The factorial of the number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    number = 5
    print(f"The factorial of {number} is {factorial(number)}.")

if __name__ == "__main__":
    main()



