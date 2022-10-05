from datetime import datetime
import math

"""
CSE 111 - Lauren Snyder
A program that calculates the volume of space inside a tire when given the tire size ie. 205/60R15.
Values printed to a text file: volumes.txt
"""

width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ration = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

diameter_calculation =  ((width * aspect_ration) + (2540 * diameter))
all_calculation = (math.pi * width**2 * aspect_ration * diameter_calculation ) 
volume = all_calculation / 10000000000 

print(f'\nThe approximate volume is {volume:.2f} liters\n')

wants_tires = input(f'Would you like to purchase tires of these dimensions? Please enter (\"yes\" or \"no\"): ')

# Get the current date and time
current_date_and_time = datetime.now()

# Open a text file named volumes.txt in append mode.
with open("volumes.txt", "at") as volumes_file:

    if wants_tires == 'yes':
        telephone_number = input(f'\nExcellent! Please enter your phone #. An agent will call you with our best price.\n')

        # print date, width, aspect_ratio, diameter, volume AND telephone #
        print(f'{current_date_and_time:%Y-%m-%d}, {width}, {aspect_ration}, {diameter}, {volume:.2f}, {telephone_number}', sep=" ", end="\n", file=volumes_file, flush=False)
    
    else:
        print(f'{current_date_and_time:%Y-%m-%d}, {width}, {aspect_ration}, {diameter}, {volume:.2f},', sep=" ", end="\n", file=volumes_file, flush=False)

