#!/usr/bin/env python3

# Created by: Andrew-Ten-Den
# Created on: February 25 2022
# This program calculates the area and perimeter of a circle
# with a radius of 5 mm

import math


def main():
    # This program calculates the area and the perimeter of a circle
    print("If a circle has a radius of: ")
    print("5 mm")
    print("")
    print("Area is {} mm².".format(math.pi * 5**2))
    print("Perimeter is {} mm.".format(2 * math.pi * 5))
    print("")
    print("Problem Solved")


if __name__ == "__main__":
    main()
