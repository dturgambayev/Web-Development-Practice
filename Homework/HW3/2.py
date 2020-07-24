uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.',
           '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']


def Password():
    obj_special = 0
    obj_digit = 0
    obj_lowercase = 0
    obj_uppercase = 0
    password = input('Enter a password, please: ')
    if 9 < len(password) < 16:
        for i in range(len(password)):
            if password[i] in special:
                obj_special = obj_special + 1
            elif password[i] in digit:
                obj_digit = obj_digit + 1
            elif password[i] in lowercase:
                obj_lowercase = obj_lowercase + 1
            elif password[i] in uppercase:
                obj_uppercase = obj_uppercase + 1
    else:
        print('The password you entered is invalid. Enter a new one')
        Password()

    if obj_uppercase > 0 and obj_lowercase > 0 and obj_digit > 0 and obj_special > 0:
        print('Success')
    else:
        print('The password you entered is invalid. Enter a new one, please')
        Password()

Password()
