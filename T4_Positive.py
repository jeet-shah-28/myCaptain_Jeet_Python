def main():
    nos = input("Enter the list of nos : ").split(",")
    pstve = [int(n) for n in nos if int(n) > 0]
    print("List of positive numbers is :",pstve)

if __name__ == '__main__':
    main()