cars = ['Audi','Honda','H','Suzuki','YellowFoxy','KIA']
for company in cars:
    print (f"{company.title()}, This a company list!")
    print ("For loop ended")
    
#range functions
    for value in range(1,5):
        print (value)
        
#list functions
    cars = ['Audi','Honda','H','Suzuki','YellowFoxy','KIA']
    print (cars)
    print (cars[0])
    print (cars[1])
    print (cars[2])
    print (cars[3])
    
# sir example of list functions
num = list(range(0,9))
print (num)

#even numbers
even_num = list(range(0,10,2))
print (even_num)

#square 
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print (squares)

# Slicing a list
players = ['Ahmad', 'Hang', 'Maham', 'Usama', 'Alice']
print (players)

print (players[0:5])
print (players[2:])

# looping through size
print("Here are the players")
for player in players[2:]:
    print (player.title())
# Copy a list of players
copy_players = players[:3]
print("Here are the players old list)")
print(player)
print("Now copy the players list")
print(copy_players)

# Lists
std = ['Ahmad', 'Omar', 'Imran', 'Ahsan']
print(std)
print(std[1])

# Tuples
std_1 = ()