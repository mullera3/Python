#Fizzbuzz 
#Created by Amani Muller

# Fizz Buzz - Write a program that prints the numbers from 1 to 100. 
# But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. 
# For numbers which are multiples of both three and five print “FizzBuzz”.

if __name__ == "__main__":
    for numbers in range(1,101):
        if numbers % 3 == 0 and numbers % 5 == 0:
            print("FizzBuzz")

        elif numbers % 5 == 0:
            print("Buzz")
    
        elif numbers % 3 == 0:
            print("Fizz")
        else:
            print(numbers)

