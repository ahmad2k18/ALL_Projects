requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
 print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
 print("Adding pepperoni.")
 if 'extra cheese' in requested_toppings:
  print("Adding extra cheese.")
print("\nFinished making your pizza!")

# Using if statements with lists
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
 print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

# Checking that list is not 
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
if requested_toppings:
 for requested_topping in requested_toppings:
  print(f"Adding {requested_topping}.")
 print("\nFinished making your pizza!")
 
# Using Multiple Lists
 available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
 requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
 for requested_topping in requested_toppings:
  if requested_topping in available_toppings:
   print(f"Adding {requested_topping}.")
  else:
      print(f"Sorry, we don't have {requested_topping}.")
      
# Another example
available_toppings = ['mushrooms', 'olives', 'green peppers',
 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
 if requested_topping in available_toppings:
  print(f"Adding {requested_topping}.")
else:
 print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")  

# numerical comparisons
answer = 17
if answer != 42:
 print("That is not the correct answer. Please try again!")
 
# checking multiple conditions
 requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
if'mushrooms' in requested_toppings:
 print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
 print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
  print("Adding extra cheese.")
  print("\nFinished making your pizza!")
   
# Simple examples
# 1. Check if a number is greater than another
x = 10
if x > 5:
    print("1. True")
else:
    print("1. False")
# Prediction: True

# 2. Check if a string contains another string
string = "hello world"
if "world" in string:
    print("2. True")
else:
    print("2. False")
# Prediction: True

# 3. Check if a list is empty
my_list = []
if not my_list:
    print("3. True")
else:
    print("3. False")
# Prediction: True

# 4. Check if two variables are equal
a = 5
b = 10
if a == b:
    print("4. True")
else:
    print("4. False")
# Prediction: False

# 5. Check if a variable is of a certain type
var = 3.14
if isinstance(var, float):
    print("5. True")
else:
    print("5. False")
# Prediction: True

# 6. Check if a value is in a list
my_list = [1, 2, 3, 4, 5]
if 3 in my_list:
    print("6. True")
else:
    print("6. False")
# Prediction: True

# 7. Check if a dictionary has a specific key
my_dict = {"name": "Alice", "age": 30}
if "name" in my_dict:
    print("7. True")
else:
    print("7. False")
# Prediction: True

# 8. Check if a set contains a specific element
my_set = {1, 2, 3}
if 4 in my_set:
    print("8. True")
else:
    print("8. False")
# Prediction: False

# 9. Check if a string is numeric
string = "1234"
if string.isnumeric():
    print("9. True")
else:
    print("9. False")
# Prediction: True

# 10. Check if the length of a list is greater than a value
my_list = [1, 2, 3]
if len(my_list) > 5:
    print("10. True")
else:
    print("10. False")



    