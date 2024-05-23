# Imported Restaurant 9-10

# restaurant.py

class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"{self.name} serves wonderful {self.cuisine_type} cuisine.")
    
    def open_restaurant(self):
        print(f"{self.name} is now open!")

