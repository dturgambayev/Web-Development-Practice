import csv
import messages

def authorization(counter):
    answer = input('Your option: ')
    if answer == '1':
        last_messages(counter)
    elif answer == '2':
        new_messages(counter)
    elif answer == '3':
        all_messages(counter)
    elif answer == '4':
        import user_account
        user_account.main(counter)
    else:
        print('Invalid input!')
        authorization(counter)

def new_messages(counter):
    user_login = []
    user_messages = []

    with open('new_messages.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            try:
                if row[1] == counter:
                    user_login.append(row[0])
                    user_messages.append(row[2])
                else:
                    user_login = user_login
                    user_messages = user_messages
            except:
                user_login = user_login
                user_messages = user_messages

    user_login = [i for i in user_login]
    user_messages = [i for i in user_messages]

    if len(user_login) == 0:
        print('0 unread messages')
        authorization(counter)

    for i in range(len(user_login)):
        print(str(i + 1) + '. You got a message from: ' + str(user_login[i]))

    print('To read the message, please enter its <number>! To get back, please enter <back>!')
    answer = input('Your choice: ')
    while answer != 'back':
        try:
            print('You got a message from ' + str(user_login[int(answer) - 1]) + ' to ' + str(counter))
            print(user_messages[int(answer) - 1])

            if user_messages[int(answer) - 1] == 'Friend request!' and messages.request(counter, user_login[int(answer) - 1]) == 0:
                choice = input('Do you want to accept a friend request? ')
                if choice == 'yes' or choice == 'Yes' or choice == 'YES' or choice == 'Yup' or choice == 'YUP' or choice == 'yup' or choice == 'sure' or choice == 'Sure' or choice == 'SURE':
                    with open('friends.csv', 'a', newline = '') as file:
                        csv_writer = csv.writer(file, delimiter = ',')
                        csv_writer.writerow([str(counter), str(user_login[int(answer) - 1])])
                    messages.friend_message('Admin: ', str(user_login[int(answer) - 1]), str('Your friend request to user: ' + str(counter) + ' was accepted!'))
                    last_messages(counter)
                else:
                    last_messages(counter)
            else:
                authorization(counter)

            answer = input('Your option: ')
        except:
            print('Invalid input!')
            answer = input('Your option: ')
    authorization(counter)

def last_messages(counter):
    user_login = []
    user_message = []

    with open('new_messages.csv', 'w', newline = '') as file:
        csv_writer = csv.writer(file, delimiter = ',')
        csv_writer.writerow(['sep=,'])
    with open('messages.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            try:
                if row[1] == counter:
                    user_login.append(row[0])
                    user_message.append(row[2])
                else:
                    user_login = user_login
                    user_message = user_message

            except:
                user_login = user_login
                user_message = user_message

    user_login = [i for i in user_login]
    user_message = [i for i in user_message]

    if len(user_login) < 6:
        user_login = user_login[::-1]
        user_message = user_message[::-1]
    else:
        user_login = user_login[:len(user_login) - 6:-1]
        user_message = user_message[:len(user_message) - 6:-1]

    for i in range(len(user_login)):
        print(str(i + 1)+'. You got a message from: ' + str(user_login[i]))

    if len(user_login) == 0:
        print('0 unread messages')
        authorization(counter)
    answer = input('Your option: ')
    while answer != 'back' or answer != 'Back':
        try:
            print('There is a message from: ' + str(user_login[int(answer) - 1]) + ' to ' + str(counter))
            print(user_message[int(answer) - 1])
            if user_message[int(answer) - 1] == 'Friend request!' and messages.request(counter, user_login[int(answer) - 1]) == 0:
                choice = input('Do you want to accept friend request? ')
                if choice == 'yes' or choice == 'Yes' or choice == 'YES' or choice == 'Yup' or choice == 'YUP' or choice == 'yup' or choice == 'sure' or choice == 'Sure' or choice == 'SURE':
                    with open('friends.csv', 'a', newline = '') as file:
                        csv_writer = csv.writer(file, delimiter = ',')
                        csv_writer.writerow([str(counter), str(user_login[int(answer) - 1])])
                    messages.friend_message(str('Admin: ', str(user_login[int(answer) - 1]), str('Your friend request to user: ' + str(counter) + ' was accepted!')))
                    last_messages(counter)
                else:
                    last_messages(counter)
            else:
                authorization(counter)
            answer = input('Your option: ')
        except:
            print('Invalid input!')
            answer = input('Your option: ')
    authorization(counter)

def all_messages(counter):
    user_login = []
    user_message = []

    with open('new_messages.csv', 'w', newline = '') as file:
        csv_writer = csv.writer(file, delimiter = ',')
        csv_writer.writerow(['sep=,'])
    with open('messages.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            try:
                if row[1] == counter:
                    user_login.append(row[0])
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
        print('0 unread messages')
        authorization(counter)
    for i in range(len(user_login)):
        print(str(i + 1) + '. You got a message from: ' + str(user_login[i]))

    print('To read the message, please enter its <number>! To get back, please enter <back>!')
    answer = input('Your option: ')
    while answer != 'back' or answer != 'Back':
        try:
            print('There is a message from ' + str(user_login[int(answer) - 1]) + ' to ' + str(counter))
            print(user_message[int(answer) - 1])

            if user_message[int(answer) - 1] == 'Friend request!' and messages.request(counter, user_login[int(answer) - 1]) == 0:
                choice = input('Do you want to accept friend request? ')
                if choice == 'yes' or choice == 'Yes' or choice == 'YES' or choice == 'Yup' or choice == 'YUP' or choice == 'yup' or choice == 'sure' or choice == 'Sure' or choice == 'SURE':
                    with open('friends.csv', 'a', newline = '') as file:
                        csv_writer = csv.writer(file, delimiter = ',')
                        csv_writer.writerow([str(counter), str(user_login[int(answer) - 1])])

                    messages.friend_message(str('Admin: ', str(user_login[int(answer) - 1]), str('Your friend request was accepted!')))
                    all_messages(counter)
                else:
                    all_messages(counter)
            else:
                authorization(counter)
            answer = input('Your option: ')
        except:
            print('Invalid input!')
            answer = input('Your option: ')
    authorization(counter)

def main(counter):
    print('View the last 5 messages <PRESS 1>')
    print('View all unread messages <PRESS 2>')
    print('View all messages <PRESS 3>')
    print('Back <PRESS 4>')
    authorization(counter)

if __name__=='__main__':
    main()