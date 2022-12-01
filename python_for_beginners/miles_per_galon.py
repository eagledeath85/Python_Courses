import random

car_tank_gallons_capacity = random.randint(10, 25)
max_number_of_miles = random.randint(200, 400)

MPG = max_number_of_miles // car_tank_gallons_capacity

print("The tank capacity is " + str(car_tank_gallons_capacity))
print("The maximum number of miles your car can travel is " + str(max_number_of_miles))
print("Your car consumes " + str(MPG) + " gal per miles")

