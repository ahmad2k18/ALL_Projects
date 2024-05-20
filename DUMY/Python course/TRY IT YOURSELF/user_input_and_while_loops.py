 # Rental car  7-1
def rental_car():
    car_type = input("What kind of rental car would you like? ")
    
    print(f"Let me see if I can find you a {car_type.title()}.")

rental_car()

# Restaurant seating 7-2
def check_table_availability():
    try:
        group_size = int(input("How many people are in your dinner group? "))
        
        # Check if the group size is more than eight
        if group_size > 8:
            print("You’ll have to wait for a table.")
        else:
            print("Your table is ready.")
    except ValueError:
        print("Please enter a valid number.")

check_table_availability()

# MULTIPLES OF TEN 7-3
def check_multiple_of_10():
    # Ask the user for a number
    try:
        number = int(input("Please enter a number: "))
        
        # Check if the number is a multiple of 10
        if number % 10 == 0:
            print(f"The number {number} is a multiple of 10.")
        else:
            print(f"The number {number} is not a multiple of 10.")
    except ValueError:
        print("Please enter a valid number.")

check_multiple_of_10()


