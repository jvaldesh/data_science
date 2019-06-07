import sys

g = float(sys.argv[1])
r = float(sys.argv[2])

ve = (2 * g * r * 1000)**(0.5)

print("La velocidad de escape es: {}".format(ve))