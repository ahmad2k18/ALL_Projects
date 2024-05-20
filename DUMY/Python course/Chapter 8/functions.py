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