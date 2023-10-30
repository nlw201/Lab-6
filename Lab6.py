import sys


def encoder():
    userint = input("Enter an 8 character long password that only includes digits:")
    global password
    password = ''
    for i in userint:
        codewheel = {'0': '3', '1': '4', '2': '5', '3': '6', '4': '7',
                     '5': '8', '6': '9', '7': '0', '8': '1', '9': '2'}
        password += codewheel[i]
    print(password)


def decoder():
    decoded = ''
    for num in password:
        decoded += str((int(num) - 3) % 10)
    print(f'The encoded password is {password}, and the original password is {decoded}.')


def main():
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

    while choose != 3:
        main()


main()
