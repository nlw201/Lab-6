import sys

# Encode function
def encoder():
    # Takes user input
    userint = input("Enter an 8 character long password that only includes digits:")
    #makes password a global function
    global password
    password = ''
    # For loop to decode each digit
    for i in userint:
        codewheel = {'0': '3', '1': '4', '2': '5', '3': '6', '4': '7',
                     '5': '8', '6': '9', '7': '0', '8': '1', '9': '2'}
        password += codewheel[i]
    print(password)

# Decode function
def decoder():
    decoded = ''
    # Decodes each individual digit in the string
    for num in password:
        # Casts the string as an int to apply math functions and then back to a string
        decoded += str((int(num) - 3) % 10)
    print(f'The encoded password is {password}, and the original password is {decoded}.')


def main():
    # Looping menu
    choose = int(input('Menu \n'
                       '---- \n'
                       '1. Encode Password \n'
                       '2. Decode Password \n'
                       '3. Exit \n'))
    if choose == 1:
        encoder()

    if choose == 2:
        decoder()

    if choose == 3:
        x = False
        sys.exit()
    # While loop that runs as long as the user doesn't choose option 3 
    while choose != 3:
        main()

# Starts the loop
main()
