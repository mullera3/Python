#Fast Exponentiation - Ask the user to enter 2 integers a and b and output a^b
import math

def exponentiation(a,b):

    if b == 0:
        a = 1
        print(a)
    elif b == 1:
        print(a)
    else:
        print(pow(a,b))


if __name__ == "__main__":
    u = int(input("Enter first number: "))
    v = int(input("Enter second number: "))
    exponentiation(u,v)