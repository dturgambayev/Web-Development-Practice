import csv

def log_in():
    createLogin = input('Write your login, please: ')
    createPassword = input('Write your password, please: ')
    login = []
    password = []
    with open('users.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            try:
                login.append(row[0])
                password.append(row[1])
            except:
                login = login
                password = password

    if createLogin in login and createPassword in password:
        print('Login successful!')
        import user_account
        user_account.main(createLogin)
    else:
        print('User doesnt exist or wrong password!')
        log_in()

def authorization():
    answer = input('Your option: ')
    if answer == '1':
        log_in()
    elif answer == '2':
        import register
        register.main()
    elif answer == '3':
        import main_menu
        main_menu.main()
    else:
        print('Invalid input, re-enter your option: ')
        authorization()

def main():
    log_in()

if __name__=='__main__':
    main()