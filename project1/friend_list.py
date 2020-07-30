import csv
import messages

def authorization(counter):
    answer = input('Your option: ')
    if answer == '1':
        search(counter)
    elif answer == '2':
        view_users(counter)
    elif answer == '3':
        import user_account
        user_account.main(counter)
    elif answer in messages.friend_list(counter):
        import beFriends
        beFriends.main(counter, answer)
    else:
        print('Invalid input!')
        authorization(counter)

def view_users(counter):
    login = []
    with open('users.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            login.append(row[0])
    num = login.index(counter)

    for i in range(len(login)):
        print(str(i + 1) + '. ' + str(login[i]))

    print('To get back, please enter <back> !')
    answer = input('Your choice: ')
    if answer == 'back' or answer == 'Back':
        main(counter)
    else:
        print('Invalid input!')
        view_users(counter)

def search(counter):

    login = []
    answer = input('Search for user: ')
    with open('users.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            login.append(row[0])

    num = login.index(counter)

    if answer in login:
        import beFriends
        beFriends.main(counter, answer)
    else:
        print('There is no entered user!')
        authorization(counter)

def friend_list(counter):
    import messages
    if len(messages.friend_list(counter)) != 1 and  len(messages.friend_list(counter)) != 0:
        print('You have ' + str(len(messages.friend_list(counter))) + ' friends.')
        print('There is a list of your friends: ')
        for i in range(len(messages.friend_list(counter))):
            print(str(i + 1) + '. ' + messages.friend_list(counter)[i])
    elif len(messages.friend_list(counter)) == 1:
        print('You have ' + str(len(messages.friend_list(counter))) + ' friend.')
        print('Here is your friends` list: ')
        for i in range(len(messages.friend_list(counter))):
            print(str(i + 1) + '. ' + messages.friend_list(counter)[i])
    else:
        print('You have ' + str(len(messages.friend_list(counter))) + ' friends.')

def main(counter):
    print('Search for users <PRESS 1>')
    print('List of all users <PRESS 2>')
    print('Back <PRESS 3>')
    friend_list(counter)
    authorization(counter)

if __name__=='__main__':
    main()