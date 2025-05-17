import random
import os

# Necessary lists
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Clears the terminal
clear_terminal()

print("Welcome to the PyPassword Generator!")

def main():

    # Inputs
    nr_letters = int(input("\nHow many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))


    # Empty character list
    random_characters = []

    # Appends the character list with letters
    for number in range(0,nr_letters):
        random_characters.append(random.choice(letters))

    # Appends the character list with symbols
    for number in range(0,nr_symbols):
        random_characters.append(random.choice(symbols))

    # Appends the character list with numbers
    for number in range(0,nr_numbers):
        random_characters.append(random.choice(numbers))

    # Shuffles the character list
    random.shuffle(random_characters)

    # Fills the Password Variable with the randomized characters
    password = ""
    for character in random_characters:
        password += character

    # Check to see if the user had any inputs
    if password == "":
        print("\nThe password does not contain any characters!")
        input("\nPress to retry!")
        main()
    else:
        clear_terminal()
        print(f'''
            
            Your new password contains:
            
              -{nr_letters} letters.
              -{nr_symbols} symbols. 
              -{nr_numbers} numbers.
            
            Password: {password}
                  
            ''')
        retry = input("\nDo you want to generate a new password? y/n?\n").lower()
        if retry == "y":
            clear_terminal()
            main()
        else:
            clear_terminal()
            print("\nThanks for using my Password Generator!")
            return
if __name__ == "__main__":
    main()
