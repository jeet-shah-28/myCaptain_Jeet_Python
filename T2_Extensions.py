def main():
    filename = input("Input the Filename : ")
    extsname = "python" if filename.split('.')[-1] == "py" else filename.split('.')[-1]
    print("The extension of the file is : "+extsname)

if __name__ == '__main__':
    main()