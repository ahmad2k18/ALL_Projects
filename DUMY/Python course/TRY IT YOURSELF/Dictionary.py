# Person 6-1
person_info = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York'
}
print(f"First Name: {person_info['first_name']}")
print(f"Last Name: {person_info['last_name']}")
print(f"Age: {person_info['age']}")
print(f"City: {person_info['city']}")

# Favorite Name 6-2
favorite_numbers = {
    'Alice': 7,
    'Bob': 13,
    'Charlie': 42,
    'Diana': 23,
    'Edward': 5
}

for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")
    
# Glossary 6-3  
glossary = {
    'variable': 'A storage location paired with an associated symbolic name, which contains some known or unknown quantity of information referred to as a value.',
    'function': 'A block of organized, reusable code that is used to perform a single, related action.',
    'loop': 'A programming construct that repeats a group of commands.',
    'list': 'A collection of items in a particular order.',
    'dictionary': 'A collection of key-value pairs.'
}
for word, meaning in glossary.items():
    print(f"{word.capitalize()}:\n\t{meaning}\n")
  
# Glossary 6-4
# Initial glossary of Python terms
glossary = {
    "variable": "A named location used to store data in memory.",
    "function": "A block of code which only runs when it is called.",
    "loop": "A control structure used to repeat a block of code.",
    "dictionary": "A collection of key-value pairs.",
    "list": "A collection of ordered items."
}

# Add new terms to the glossary
glossary.update({
    "tuple": "An immutable sequence of values.",
    "set": "A collection of unique items.",
    "class": "A blueprint for creating objects.",
    "inheritance": "A way to form new classes using classes that have already been defined.",
    "exception": "An event that disrupts the normal flow of a program."
})

# Loop through the dictionary and print each term and its definition
for term, definition in glossary.items():
    print(f"{term.title()}: {definition}")
    
# Rivers 6-5
# Dictionary containing major rivers and the countries they run through
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'
}

# Loop to print a sentence about each river
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# Loop to print the name of each river
print("\nRivers included in the dictionary:")
for river in rivers.keys():
    print(river.title())

# Loop to print the name of each country
print("\nCountries included in the dictionary:")
for country in rivers.values():
    print(country.title())

# Polling 6-6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# List of people
people_to_poll = ['jen', 'sarah', 'edward', 'phil', 'michael', 'david']

# Loop through the list of people who should take the poll
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for taking the poll.")
    else:
        print(f"{person.title()}, please take our favorite languages poll!")
        
# people 6-7
person1 = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York'
}

# Two new dictionaries representing different people
person2 = {
    'first_name': 'Jane',
    'last_name': 'Smith',
    'age': 25,
    'city': 'Los Angeles'
}

person3 = {
    'first_name': 'Mike',
    'last_name': 'Johnson',
    'age': 35,
    'city': 'Chicago'
}

# Store all three dictionaries in a list called people
people = [person1, person2, person3]

# Loop through the list of people and print everything about each person
for person in people:
    print(f"First Name: {person['first_name']}")
    print(f"Last Name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}\n")
    
# pets 6-8
pet1 = {
    'animal': 'dog',
    'owner': 'Alice'
}

pet2 = {
    'animal': 'cat',
    'owner': 'Bob'
}

pet3 = {
    'animal': 'hamster',
    'owner': 'Charlie'
}

pet4 = {
    'animal': 'parrot',
    'owner': 'Diana'
}

pet5 = {
    'animal': 'rabbit',
    'owner': 'Eve'
}

# Store all pet dictionaries in a list called pets
pets = [pet1, pet2, pet3, pet4, pet5]

# Loop through the list of pets and print everything about each pet
for pet in pets:
    print(f"Animal: {pet['animal'].title()}")
    print(f"Owner: {pet['owner'].title()}\n")
    
# favorite places 6-9
# Dictionary called favorite_places
favorite_places = {
    'alice': ['paris', 'new york', 'tokyo'],
    'bob': ['sydney', 'cape town'],
    'charlie': ['london', 'berlin', 'amsterdam']
}

# Loop through the dictionary and print each person’s name and their favorite places
for person, places in favorite_places.items():
    print(f"{person.title()}'s favorite places are:")
    for place in places:
        print(f"- {place.title()}")
    print()
    
# favorite number 6-10
favorite_numbers = {
    'alice': [7, 12, 15],
    'bob': [3, 11, 19],
    'charlie': [2, 8, 10, 20],
}

for person, numbers in favorite_numbers.items():
    print(f"{person.title()}'s favorite numbers are: {', '.join(map(str, numbers))}")
    
# cities 6-11
cities = {
    'new york': {
        'country': 'united states',
        'population': '8.4 million',
        'fact': 'New York City is known as "The Big Apple".'
    },
    'tokyo': {
        'country': 'japan',
        'population': '9.7 million',
        'fact': 'Tokyo is the largest metropolitan area in the world.'
    },
    'london': {
        'country': 'united kingdom',
        'population': '8.9 million',
        'fact': "London's iconic landmark is the Big Ben clock tower."
    }
}

# Loop through the dictionary and print each city along with its information
for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"Country: {info['country'].title()}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")

# Extensions 6-12
favorite_languages = {
    'jen': {'language': 'python', 'proficiency': 'intermediate'},
    'sarah': {'language': 'c', 'proficiency': 'beginner'},
    'edward': {'language': 'ruby', 'proficiency': 'advanced'},
    'phil': {'language': 'python', 'proficiency': 'expert'}
}

# Add a new person to the dictionary and give them a favorite language
favorite_languages['michael'] = {'language': 'java', 'proficiency': 'intermediate'}
favorite_languages['david'] = {'language': 'python', 'proficiency': 'beginner'}

# Loop through the dictionary and print each person’s name and their favorite language
def print_favorite_languages_by_proficiency():
    print("Favorite Languages by Proficiency:")
    sorted_languages = sorted(favorite_languages.items(), key=lambda x: x[1]['proficiency'])
    for person, data in sorted_languages:
        print(f"{person.title()} is proficient in {data['language'].title()} ({data['proficiency'].title()})")

print_favorite_languages_by_proficiency()
    
    
    
    
        
    

