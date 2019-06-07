import sys

year = 2000
while year <= 2019:

    if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        print("El año {} es bisiesto".format(year))
    else:
        print("El año {} NO es bisiesto".format(year))

    year += 1
