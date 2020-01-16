# Check if Palindrome - Checks if the string entered by the user is a palindrome. 
# That is that it reads the same forwards as backwards like “racecar”

def check_palindrome(word):
    if word.lower() == word[::-1].lower():
        print("Yes it's a palindrome!")
    else:
        print("It's not a palindrome!")

if __name__ == "__main__":
    my_word = str(input("Enter word to check if a word is a palidrome: "))
    check_palindrome(my_word)