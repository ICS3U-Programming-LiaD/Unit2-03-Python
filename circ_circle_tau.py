
#!/usr/bin/env python3
# Created by: Lia Duggan
# Created on: Sept 26th 2022
# This program asks the user for the radius of
# a circle in cm and displays it.

import constants

def main():
    # get the radius from the user
    radius = float(input("What is the radius of the circle (cm): "))

    # calculate the circumference
    circumference = constants.TAU * radius

    # display the circumference
    print("")
    print("Circumference = {} cm".format(circumference))


if __name__ == "__main__":
    main()
