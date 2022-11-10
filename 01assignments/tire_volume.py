#v is the volume in liters,
#π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
#w is the width of the tire in millimeters,
#a is the aspect ratio of the tire, and
#d is the diameter of the wheel in inches.
#205 = w   60R = a  15 = d
#v = pi * w**2 * a (w * a + 2,540) / 10,000,000,000

# inputs are w, a, and d. 
import math
from datetime import datetime

w_input = input("Enter the width of the tire in mm (Ex 205): ")
a_input = input("Enter the aspect ratio of the tire (Ex 60): ")
d_input = input("Enter the diameter of the wheel in inches (Ex 15): ")

width = int(w_input)
aspect_ratio = int(a_input)
diameter = int(d_input)

volume = ((math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000)

print(f"The volume you be lookin for is {volume:.2f} liters ")

# Gets the current date from the computer's operating system.
# Opens a text file named volumes.txt for appending.
# Appends to the end of the volumes.txt file one line of text that contains the following five values:
# current date
# width of the tire
# aspect ratio of the tire
# diameter of the wheel
# volume of the tire

current_date = datetime.now()
print(f"{current_date:%Y-%m-%d}")

tire_width_string = str(width)
tire_aspect_string = str(aspect_ratio)
tire_diameter_string = str(diameter)

with open("volume.txt", "a") as file:
    print(f"{current_date:%Y-%m-%d}, {tire_width_string}, {tire_aspect_string}, {tire_diameter_string}, {volume:.2f} ", file=file)
