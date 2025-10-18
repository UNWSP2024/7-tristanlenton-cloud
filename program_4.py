import math


def distance (cord1, cord2):
    total = math.sqrt((cord2(0) - cord1(0)) ^ 2 + (cord2(1) - cord1(1)) ^ 2 + (cord2(2) - cord1(2)) ^ 2)
    return total
try:
    cord1 = (int(input("Cordinate x: ")), int(input("Cordinate y: ")), int(input("Cordinate z: ")))
    cord2 = (int(input("Cordinate x: ")), int(input("Cordinate y: ")), int(input("Cordinate z: ")))
    distance = distance(cord1, cord2)
    print(distance)
except ValueError:
    print("Invalid input")