# dictionary example
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# another dictionary example
cars = {'color': 'black', 'model': '2021'}

print(cars['color'])

print(cars['model'])

# adding new key value pair

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

# another example
cars['Company_name'] = 'Audi'
print(cars['Company_name'])
print(cars)

vehicles = {}
print(vehicles)

vehicles['Display Cars'] = 5
print(vehicles)

vehicles['Display Cars'] = 10

print(vehicles['Display Cars'])

# modifying value in dictionary

alien_0['color'] = 'yellow'
print(alien_0)

# deleting key value pair

del alien_0['points']
print(alien_0)

# looping through a dictionary

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# using a looping in dictionaries
user = {
    'username': 'admin',
    'firstname': 'ahmad',
    'lastname': 'ali',
}

for key, value in user.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")


# nesting dictionary
car_0 = {'color': 'black', 'model': '2019',}
cars_1 = {'color': 'white', 'model': '2020',}
car_2 = {'color': 'blue', 'model': '1999',}

cars = [car_0, cars_1, car_2]

for car in cars:
    print(car)
    
# Another example
new_cars = [] 

for car_number in range(30):
    n_car = {'color': 'black', 'model': '2019',}
    new_cars.append(n_car)
       
for c in new_cars[:5]:
    print(c)
print('.......')        

# Accessing values in dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# starting with empty dictionary

favorite_languages = {}

if favorite_languages:
    for name, language in favorite_languages.items():
        print(f"{name.title()}'s favorite language is {language.title()}.")
    else:
        print("We need to find some users!")
            
# modifying values in a  dictionary
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
Dictionaries  = 95
alien_0['color'] = 'yellow'
print (f"The alien is now {alien_0['color']}.")

# Looping through all key-value pairs

favorite_languages = {
    'jen': 'python',
   'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
    
# Looping through all keys in a dictionary

favorite_languages = {
    'jen': 'python',
   'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in favorite_languages.keys():
    print(name.title())
    
# Looping Through a Dictionary’s Keys in a Particular Order

favorite_languages = {
    'jen': 'python',
   'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
    
# A list of dictionaries

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color':'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# make an empty list for storing aliens

aliens = []

# make 30 green aliens

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5,'speed':'slow'}
    aliens.append(new_alien)
    
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] ='medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] ='red'
        alien['speed'] = 'fast'
        alien['points'] = 15
    else:
        alien['color'] = 'green'
        alien['speed'] ='slow'
        alien['points'] = 5
        
# show how many alien have been created

print(f"Total number of aliens: {len(aliens)}")

for alien in aliens[0:5]:
    print(alien)
            
# a list in a dictionary

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

# a dictionary in a dictionary

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
   'mcurie': {
        'first':'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
    