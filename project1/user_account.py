import csv

def authorization(counter):
    answer = input('Your option: ')
    if answer == '1':
        import friend_list
        friend_list.main(counter)
    elif answer == '2':
        import inbox
        inbox.main(counter)
    elif answer == '3':
        import outbox
        outbox.main(counter)
    elif answer == '4':
        import main_menu
        main_menu.main()
    elif answer == '5':
        exit()
    else:
        print('Invalid input!')
        authorization(counter)

def account(counter):
    login = []
    password = []
    with open('users.csv') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            try:
                login.append(row[0])
                password.append(row[1])
            except:
                login = login
                password = password

    num = login.index(counter)
    print('Your login: ' + login[num])
    print('-' * 10)
    print('Your password: ' + password[num])
    print('-' * 10)

def main(counter):
    print('Friends <PRESS 1>')
    print('Inbox <PRESS 2>')
    print('Outbox <PRESS 3>')
    print('Log Out <PRESS 4>')
    print('Exit <PRESS 5>')
    account(counter)
    authorization(counter)

if __name__=='__main__':
    main()