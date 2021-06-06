import math

def main():
    r = float(input("Input the radius of the circle : "))
    area = math.pi*(r**2)
    print("The area of the circle with radius {} units is : {} sq.units".format(r,area))

if __name__ == '__main__':
    main()
