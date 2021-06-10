"""Program to print Fibonnaci Series of n terms"""

def main():
    n = int(input("Enter the no. of terms : "))
    a,b = 0,1
    print(a,b,sep=", ",end="")
    for i in range(n-2):
        c = a + b;
        print(",",c,end="")
        a,b = b,c;

if __name__ == '__main__':
    main()