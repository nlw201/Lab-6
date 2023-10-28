def encoder():
    userint = input("Enter an 8 character long password that only includes digits:")
    password = ''
    for i in userint:
        codewheel = {'0': '3', '1': '4', '2': '5', '3': '6', '4': '7',
                     '5': '8', '6': '9', '7': '0', '8': '1', '9': '2'}
        password += codewheel[i]
    print(password)


encoder()
