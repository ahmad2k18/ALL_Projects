# defining the function

def main():
    print("Hello World")

main()

# passing information to a function

def main(username , lastname , email , password):
    print(f"Hello , {username.title()} {lastname.title()} {email.lower()} {password.lower()}")

main("Mark" , "John" , "markjhon@gmail.com" , "markjhon") 
main("Mark" , "John" , "mark@gmail.com" , "dummy")  
main("Mark" , "John" , "jhon@gmail.com" , "heaven")

# keywords arguments

def main(username, lastname, email, password):
    print(f"Hello, {username.title()} {lastname.title()} {email.lower()} {password.lower()}")

main(username="Mark", lastname="John", email="markjhon@gmail.com", password="markjhon")
main(lastname="John", password="heaven", email="jhon@gmail.com", username="Mark")

# sir example
def details(name,age):
    print(f"Enter name: and age: {name}{age}")

details(name='ahmad',age=25)  

# default value function parameter

def subject(sub_name,marks=50):
    print(f"My marks is {marks}")
    print(f"My subject name is {sub_name}")

subject (sub_name='Pythons',marks=50)

# avoid arguments error

def info_1(firstname,lastname):
    print(f"Enter firstname: {firstname.upper()} and lastname: {lastname.upper()}")
    
info_1(firstname = 'Ahmad',lastname = 'Butt ')    # make error when pass 1 argument

# return values

def add(num1,num2):
    return num1 + num2

print(add(10,20))

# return multiple values

def add(num1,num2):
    return num1 + num2,num1 - num2,num1 * num2,num1 / num2

print(add(10,20))

# more examples 
def formatted_name(firstname,lastname):
    full_name = f"{firstname},{lastname}"
    return full_name.upper()
information = formatted_name('ahmad' , 'butt')

print(information)

# return dictionary
def build_person(first_name, last_name):
   person = {'First': first_name, 'Last': last_name}
   return person
musician = build_person('Oggy', 'hendrix')
print(musician)

# positional arguments

def add(num1,num2):
    return num1 + num2

print(add(10,20))

# keyword arguments

def add(num1,num2):
    return num1 + num2

print(add(num1=10,num2=20))

# passing a list in the function

def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
        
usernames = ['Alice', 'Bob', 'Tyson', 'Ivan', 'Shawn']   

greet_users(usernames)

# multiple number of arguments
def make_pizzas(*toppings):
    print(toppings)
    
make_pizzas('chilli')
make_pizzas('green_chilli','bbq','extra_cheese')

# Importing an Entire Module it use in making two py files that are in the same folder

def make_pizza(size, *toppings):
 """Summarize the pizza we are about to make."""
 print(f"\nMaking a {size}-inch pizza with the following toppings:")
 for topping in toppings:
  print(f"- {topping}")

import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
                
