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







