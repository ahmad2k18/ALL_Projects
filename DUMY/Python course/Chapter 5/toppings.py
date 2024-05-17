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

    