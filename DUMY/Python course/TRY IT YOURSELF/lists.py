bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Accessing Elements in a List
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1]) # If you ask for the item at index -1, Python always returns the last item in the list

# Using Individual Values from a List
#you can use f-strings to create a message based on a value from a list

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

message = f"My first bicycle was a {bicycles[1].title()}."
print(message)

# Names 3-1
names = ['ahmad', 'amer', 'joe', 'jerry']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# Greetings 3-2
names = ['ahmad', 'amer', 'joe', 'jerry']
print(f"Hello, {names[0].title()}!")
print(f"Hello, {names[1].title()}!")
print(f"Hello, {names[2].title()}!")
print(f"Hello, {names[3].title()}!")

# Your Own List 3-3
# List of favorite modes of transportation
modes_of_transportation = ['motorcycle', 'car', 'bicycle', 'scooter']

# Print statements about each mode of transportation
for mode in modes_of_transportation:
    if mode == 'motorcycle':
        print("I would like to own a Honda motorcycle.")
    elif mode == 'car':
        print("I dream of having a Tesla car.")
    elif mode == 'bicycle':
        print("Riding a mountain bike in the countryside is refreshing.")
    elif mode == 'scooter':
        print("Using an electric scooter for short commutes is convenient.")
    else:
        print("I haven't thought about this mode of transportation yet.")
        
# Modifying Elements in a List
motorcycles = ['honda', 'yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'suzuki'
print(motorcycles)

# Adding Elements to a List
motorcycles = ['honda', 'yamaha','suzuki']
print(motorcycles)

motorcycles.append('suzuki')
print(motorcycles)

# Inserting Elements into a List
motorcycles = ['honda', 'yamaha','suzuki']
print(motorcycles)

motorcycles.insert(0,'tesla')
print(motorcycles)

# Removing Elements from a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

# Removing an Item Using the pop() Method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# Removing an Item by Value
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.remove('yamaha')
print(motorcycles)

# Popping Items from Any Position in a List

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# Remove an item by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)

print(f"\nA {too_expensive.title()} is too expensive for me.")

# Guest list 3-4
guest_list = ['ahmad', 'amer', 'joe', 'jerry']
print(f"Hello, {guest_list[0].title()}!")
print(f"Hello, {guest_list[1].title()}!")
print(f"Hello, {guest_list[2].title()}!")
print(f"Hello, {guest_list[3].title()}!")

# List of people to invite to dinner
guests = ['Albert Einstein', 'Ada Lovelace', 'Leonardo da Vinci']

# Print invitation message to each person
for guest in guests:
    print("Dear {},\nI would like to invite you to dinner. It would be an honor to have your presence.\n\nSincerely,\n[Ahmad]".format(guest))


# Changing Guest List 3-5
# Initial list of guests
guests = ['Albert Einstein', 'Ada Lovelace', 'Leonardo da Vinci']

# Print invitation message to each person
for guest in guests:
    print("Dear {},\nI would like to invite you to dinner. It would be an honor to have your presence.\n\nSincerely,\n[Ahmad]".format(guest))

# Print the name of the guest who can't make it
guest_cant_make_it = 'Ada Lovelace'
print("\nUnfortunately, {} can't make it to the dinner.".format(guest_cant_make_it))

# Modify the list to replace the guest who can't make it
guests.remove(guest_cant_make_it)
new_guest = 'Marie Curie'
guests.append(new_guest)

# Print invitation message to each remaining person
print("\nHere are the updated invitations:")
for guest in guests:
    print("Dear {},\nI would like to invite you to dinner. It would be an honor to have your presence.\n\nSincerely,\n[Ahmad]".format(guest))


# More Guests 3-6
# Initial list of guests
guests = ['Albert Einstein', 'Ada Lovelace', 'Leonardo da Vinci']

# Print invitation message to each person
for guest in guests:
    print("Dear {},\nI would like to invite you to dinner. It would be an honor to have your presence.\n\nSincerely,\n[Ahmad]".format(guest))

# Add a new guest to the beginning of the list
new_guest_beginning = 'Isaac Newton'
guests.insert(0, new_guest_beginning)

# Add a new guest to the middle of the list
new_guest_middle = 'Nikola Tesla'
guests.insert(len(guests)//2, new_guest_middle)

# Add a new guest to the end of the list
new_guest_end = 'Marie Curie'
guests.append(new_guest_end)

# Print message about the bigger table
print("\nGreat news! We found a bigger table for dinner.\n")

# Print invitation message to each person in the updated list
for guest in guests:
    print("Dear {},\nI would like to invite you to dinner. It would be an honor to have your presence.\n\nSincerely,\n[Ahmad]".format(guest))

# Shrinking Guest List 3-7
# Initial list of guests
guests = ['Albert Einstein', 'Ada Lovelace', 'Leonardo da Vinci', 'Isaac Newton', 'Nikola Tesla', 'Marie Curie']

# Print invitation message to each person
for guest in guests:
    print("Dear {},\nI would like to invite you to dinner. It would be an honor to have your presence.\n\nSincerely,\n[Ahmad]\n".format(guest))

# Inform that only two people can be invited
print("Sorry, the new dinner table won't arrive in time, and we can only invite two people for dinner.\n")

# Use pop() to remove guests until only two names remain
while len(guests) > 2:
    removed_guest = guests.pop()
    print("Sorry {}, we won't be able to invite you to dinner this time.".format(removed_guest))

# Print invitation message to each of the two people still on the list
for guest in guests:
    print("Dear {},\nYou're still invited to dinner. See you soon!\n".format(guest))

# Use del to remove the last two names from the list
del guests[:]

# Print the list to make sure it's empty
print("Updated guest list:", guests)

# Organization list
# Sorting a List Permanently with the sort() Method
cars = ['bmw', 'audi', 'toyota','subaru']
cars.sort()
print(cars)

# Sorting a List Temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

# Printing a List in Reverse Order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

# Finding the Length of a List
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars)) # Length of the list


# Using the range() Function

for value in range(1,5):
    print(value)
    
# Using the range() Function to Make a List of Numbers

numbers = list(range(1,6))
print(numbers)

# Seeing the world 3-8
# List of places to visit
places_to_visit = ['Japan', 'Italy', 'New Zealand', 'Egypt', 'Canada']

# Print the list in its original order
print("Original order:", places_to_visit)

# Print the list in alphabetical order using sorted()
print("Alphabetical order:", sorted(places_to_visit))

# Print the list in its original order to show it's unchanged
print("Original order:", places_to_visit)

# Print the list in reverse-alphabetical order using sorted()
print("Reverse-alphabetical order:", sorted(places_to_visit, reverse=True))

# Print the list in its original order to show it's unchanged
print("Original order:", places_to_visit)

# Change the order of the list using reverse()
places_to_visit.reverse()
print("Reversed order:", places_to_visit)

# Change the order of the list again using reverse()
places_to_visit.reverse()
print("Original order:", places_to_visit)

# Sort the list in alphabetical order using sort()
places_to_visit.sort()
print("Alphabetical order:", places_to_visit)

# Sort the list in reverse-alphabetical order using sort()
places_to_visit.sort(reverse=True)
print("Reverse-alphabetical order:", places_to_visit)

# Dinner Guests 3-9
# Initial list of guests
guests = ['Albert Einstein', 'Ada Lovelace', 'Leonardo da Vinci', 'Isaac Newton', 'Nikola Tesla', 'Marie Curie']

# Print invitation message to each person
for guest in guests:
    print("Dear {},\nI would like to invite you to dinner. It would be an honor to have your presence.\n\nSincerely,\n[Ahmad]\n".format(guest))

# Inform that only two people can be invited
print("Sorry, the new dinner table won't arrive in time, and we can only invite two people for dinner.\n")

# Use len() to print the number of people invited to dinner
print("Number of people invited to dinner:", len(guests))

# Every function 3-10
# Create a list containing various items
items_list = ['Mount Everest', 'Amazon River', 'Italy', 'Tokyo', 'Python', 'Coffee']

# Print the original list
print("Original list:", items_list)

# Append a new item to the list
items_list.append('Spanish')
print("After appending:", items_list)

# Insert a new item at a specific index
items_list.insert(2, 'Nile River')
print("After inserting:", items_list)

# Remove an item from the list
items_list.remove('Coffee')
print("After removing:", items_list)

# Pop an item from a specific index
popped_item = items_list.pop(3)
print("Popped item:", popped_item)
print("After popping:", items_list)

# Sort the list alphabetically
items_list.sort()
print("After sorting alphabetically:", items_list)

# Reverse the list
items_list.reverse()
print("After reversing:", items_list)

# Count occurrences of an item in the list
count_python = items_list.count('Python')
print("Number of 'Python' occurrences:", count_python)

# Clear the list
items_list.clear()
print("After clearing the list:", items_list)

# Intentional Error 3-11
# Sample list
my_list = [1, 2, 3, 4, 5]

try:
    # Trying to access an index that doesn't exist
    print(my_list[10])
except IndexError:
    # Handling the index error
    print("Index out of range! Please ensure the index is within the list bounds.")



