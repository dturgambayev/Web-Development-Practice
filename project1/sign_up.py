import csv
def sign_up():

    user_login = input('Write your login, please: ')
    while len(user_login) < 4:
        print('Please, make sure that your login contains at least 4 characters: ')
        user_login = input('Write your login, please: ')
    user_password = input('Write your password, please: ')
    while password(user_password) != 1:
        print('Please, make sure that your password is valid! ')
        user_password = input('Write your password, please: ')
        password(user_password)

    login = []
    with open('users.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            try:
                login.append(row[0])
            except:
                login = login


    if user_login in login:
        print('User already exists!')
        print('If you are willing to log in <press 2>, create a new account <press 1>, go to main menu <press 3>')
        authorization()
    else:
        with open('users.csv', 'a', newline='') as file:
            csv_writer = csv.writer(file, delimiter = ',')
            csv_writer.writerow([str(user_login), str(user_password)])
        print('Successful registration!')
        import user_account
        user_account.main(user_login)
def authorization():
    answer = input('Your option: ')
    if answer == '1':
        sign_up()
    elif answer == '2':
        import log_in
        log_in.main()
    elif answer == '3':
        import main_menu
        main_menu.main()
    else:
        print('Invalid input!')
        authorization()

def password(passw):
    special=['~',':',"'",'+','[','\\','@','^','{','%','(','-','"','*','|',',','&','<','`','}','.','_','=',']','!','>',';','?','#','$',')','/',' ']
    digit=['1','2','3','4','5','6','7','8','9','0']
    lowerletter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upperletter=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    num_special=0
    num_digit=0
    num_lowerletter=0
    num_upperletter=0
    if 16>len(passw)>9:
        for i in range (0,len(passw),1):
            if passw[i] in special:
                num_special=num_special+1
            elif passw[i] in digit:
                num_digit=num_digit+1
            elif passw[i] in lowerletter:
                num_lowerletter=num_lowerletter+1
            elif passw[i] in upperletter:
                num_upperletter=num_upperletter+1
    else:
        return 0
    if num_special>0 and num_digit>0 and num_lowerletter>0 and num_upperletter>0:
        return 1
    else:
        return 0

def main():
    sign_up()

if __name__=='__main__':
    main()