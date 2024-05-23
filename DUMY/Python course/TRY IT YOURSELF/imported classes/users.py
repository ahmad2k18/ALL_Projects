# Imported Admin 9-11

# users.py

class User:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
    
    def describe_user(self):
        print(f"User {self.username}: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")
    
    def greet_user(self):
        print(f"Hello {self.username}!")

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]
    
    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()

