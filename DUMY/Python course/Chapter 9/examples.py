class students:
    def __init__(self,name,course):
        self.name = name
        self.course = course
    
    def info(self):  
        print(f"My name is : {self.name}  My course is : {self.course}")
# Creating student information

std1 =   students('Ahmad', 'Python')

std2 = students('Umer', 'Python')

std3 = students('Asad', 'Digital Marketing')

std4 = students('Adeel', 'PHP')

std5 = students('Anum', 'Digital Applications')

# CALLING INFORMATION

# std1.info()
# std2.info()
# std3.info()
# std4.info()
# std5.info()

# New example

class cars:
    def __init__(self,name,model,color):
        self.name = name
        self.model = model
        self.color = color
        self.odo = 0
        
    def info(self):
        print(f"My name is : {self.name}  My model is : {self.model} My color is : {self.color}")
        
    def odo(self):
        print(f"Meter Reading is {self.odo}")    # copy from sir lectures later
        
# car info 
        
car1 = cars('Honda', '2011','black')

car2 = cars('Audi', '2011','black')   


# CAll cars
car1.info()         


# Sir Example 
class students:
    def __init__(self,name,course):
        self.name = name
        self.course = course
    
    def info(self):
        print(f'My name is : {self.name} My course is : {self.course}')
    
# Create a student data (object)

std1 = students('Ahmad','Python')
std2 = students('Ali','Python')
std3 = students('osama','Digital Marketing')
std4 = students('tooba','Php')
std5 = students('imran', 'Graphics')

# Call student info method
# std3.info()
# std4.info()

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
    
# Create a cars objects

newcar = Car('audi','a7','2019')

newcar.odo = 23000
newcar.readodo()

print(newcar.getcars())


          