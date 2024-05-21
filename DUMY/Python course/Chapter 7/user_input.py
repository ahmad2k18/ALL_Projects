message = input("Please enter your username and password for authentication (optional): ")
print(message)


# Sir example
height = input("Please enter height: ")
height = int(height)
 
if height >= 48:
 print("You are tall enough to ride!")
else:
    print("You'll be able to ride when you're a little older.")
    

# even odd example
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
 print(f"\nThe number {number} is even.")
else:
 print(f"\nThe number {number} is odd.")    
 
# Modulo operator

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
 print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
    
# while loop in action

current_number = 1
while current_number <= 5:
 print(current_number)
 current_number += 1

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

# Letting the User Choose When to Quit

message = ""
while message!= 'quit':
 message = input(prompt)
 if message!= 'quit':
  print(message)
 
 
# Another quit example

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
 message = input(prompt)
 print(message)  
 
# using a flag

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
        
# using break to exit a loop

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
 city = input(prompt)
 if city == 'quit':
  break
 else:
  print(f"I'd love to go to {city.title()}!")
  
# using continue in a loop

current_number = 0
while current_number < 10:
 current_number += 1
 if current_number % 2 == 0:
  continue
 print(current_number)
 
# avoiding infinite loop

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

# while True:
#  city = input(prompt)
#  if city == 'quit':
#      print("Please enter a city you have visited")
     
# another example
# x = 1
# while x <= 5:
#   print(x)
# x += 1
 
# This loop runs forever! use it as experiment loop
# x = 1
# while x <= 5:
#   print(x)


      
     
     