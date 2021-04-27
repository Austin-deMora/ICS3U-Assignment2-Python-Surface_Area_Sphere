#!/usr/bin/env python3

# Created by: Austin de Mora
# Created on: April 2021
# This program calculates the surface area of a sphere
#    with any radius

import math


def main():
    # this function calculates the surface area

    # input
    radius = int(input("Enter radius of the sphere (mm): "))

    # process
    sur_area = 4 * math.pi * radius ** 2

    # output
    print("")
    print("surface area is {0}mm².".format(sur_area))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
