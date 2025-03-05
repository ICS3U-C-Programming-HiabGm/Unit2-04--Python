# Created by: Hiab G
# Date: Wed, Feb. 28th
# This program asks the user for the radius and then calculates the circumference and area of a circle using tau.
import math


def main():
    # Get the radius from the user
    radius = float(input("Enter the radius of the circle (mm): "))

    # Calculate the circumference and area
    circumference = radius * 2 * math.pi
    area = math.pi * radius **2

    # Display the circumference
    print("Circumference = {} mm".format(circumference))
    print("area = {} mm".format(area))

if __name__ == "__main__":
    main()
