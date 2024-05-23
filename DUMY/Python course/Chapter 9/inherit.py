# Electric cars example

class cars:
    def __init__(self,name,model,color):
        self.name = name
        self.model = model
        self.color = color
        
    def info(self):
        print(f"My name is : {self.name}  My model is : {self.model} My color is : {self.color}")
        
        
class Electriccar(cars):
    def __init__(self,name,model,color):
        super().__init__(name,model,color)
        
elec_car = Electriccar('Tesla','Electric Car' , 2024)

elec_car.info()

# Sir Example
class  Car:
    # Attributes Define
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odo = 0
    def getcars(self):
        name =f'{self.make} , {self.model}, {self.year}'
        return name.title()
    
    def readodo(self):
        print(f'Meterreading is {self.odo}')
        
        
# Inheritance
class Electriccar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # create a child attribute
        self.battery_size = 40
    
    def battery(self):
        print(f'Batery size is : {self.battery_size}KWH')
        
elec_car = Electriccar('tesla','electric car',2024)
print(elec_car.getcars())
elec_car.odo = 15000
elec_car.readodo()
elec_car.battery()