import csv
import messages

def setMessages(counter):
    if len(messages.friend_list(counter)) != 1 and len(messages.friend_list(counter)) != 0:
        print('You have ' + str(len(messages.friend_list(counter))) + ' friends.')
        print('Here is a list of your friends: ')
        for i in range(len(messages.friend_list(counter))):
            print(str(i + 1) + '. ' + messages.friend_list(counter)[i])

        print('To write a message, please enter the user`s <login> you want to message! To get back, please enter <back>!')
        answer = input('Your option: ')
        if answer == 'back':
            autorization(counter)
        elif answer in messages.friend_list(counter):
            message = input('Type your message: ')
            messages.friend_message(counter, answer, message)
            autorization(counter)
        else:
            print('Invalid input!')
            autorization(counter)

    elif len(messages.friend_list(counter)) == 1:
        print('You have ' + str(len(messages.friend_list(counter))) + ' friend.')
        print('Here is your friends` list:')
        for i in range(len(messages.friend_list(counter))):
            print(str(i + 1) + '. ' + messages.friend_list(counter)[i])
        print('To write a message, please enter the user`s <login> you want to message! To get back, please enter <back>!')
        answer = input('Your option: ')
        if answer == 'back' or answer == 'Back':
            autorization(counter)
        elif answer in messages.friend_list(counter):
            message = input('Type your message: ')
            messages.friend_message(counter, answer, message)
            autorization(counter)
        else:
            print('Invalid input!')
            autorization(counter)
    else:
        print('You have ' + str(len(messages.friend_list(counter))) + ' friends.')
        print('You have no friends! To write a message to anyone, please become friends with him/her/it/them and etc.')
        autorization(counter)

def view_messages(counter):
    user_login = []
    user_message = []

    with open('messages.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            try:
                if row[0] == counter:
                    user_login.append(row[1])
                    user_message.append(row[2])
                else:
                    user_login = user_login
                    user_message = user_message
            except:
                user_login = user_login
                user_message = user_message

    user_login = [i for i in user_login]
    user_message = [i for i in user_message]

    if len(user_login) == 0:
        print('0 messages')
        autorization(counter)

    for i in range(len(user_login)):
        print(str(i + 1) + '. You sent a message to: ' + str(user_login[i]))

    print('To read a message, please enter its <number>! To get back, please enter <back>!')
    answer = input('Your option: ')
    while answer != 'back' or answer != 'Back':
        try:
            print('There is a message to ' + str(user_login[int(answer) - 1]) + ' from ' + str(counter))
            print(user_message[int(answer) - 1])
            answer = input('Your option: ')
        except:
            print('Invalid input!')
            answer = input('Your option: ')
    autorization(counter)

def getMessages(counter):
    user_login = []
    user_message = []
    with open('messages.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            try:
                if row[0] == counter:
                    user_login.append(row[1])
                    user_message.append(row[2])
                else:
                    user_message = user_message
                    user_login = user_login
            except:
                user_message = user_message
                user_login = user_login

    user_login = [i for i in user_login]
    user_message = [i for i in user_message]

    if len(user_login) < 6:
        user_login = user_login[::-1]
        user_message = user_message[::-1]
    else:
        user_login = user_login[:len(user_login) - 6:-1]
        user_message = user_message[:len(user_message) - 6:-1]

    for i in range(len(user_login)):
        print(str(i + 1) + '. You sent a message to: ' + str(user_login[i]))

    if len(user_login) == 0:
        print('0 messages')
        autorization(counter)

    answer = input('Your option: ')
    while answer != 'back':
        try:
            print('There is a message to ' + str(user_login[int(answer) - 1]) + ' from ' + str(counter))
            print(user_message[int(answer) - 1])
            answer = input('Your option: ')
        except:
            print('Invalid input!')
            answer = input('Your option: ')
    autorization(counter)

def autorization(counter):
    answer = input('Your option: ')
    if answer == '1':
        getMessages(counter)
    elif answer == '2':
        view_messages(counter)
    elif answer == '3':
        setMessages(counter)
    elif answer == '4':
        import user_account
        user_account.main(counter)
    else:
        print('Invalid input!')
        autorization(counter)

def main(counter):
    print('View my last 5 messages <PRESS 1>')
    print('View all my messages <PRESS 2>')
    print('Write a message <PRESS 3>')
    print('Back <PRESS 4>')
    autorization(counter)
if __name__=='__main__':
    main()