def compile():
    answer = input('Hello, choose your option: ')
    if answer == '1':
        import sign_up
        sign_up.main()
    elif answer == '2':
        import  log_in
        log_in.main()
    else:
        exit()

def main():
    print('Registration <PRESS 1>')
    print('Log-In <PRESS 2>')
    print('Exit <PRESS 3>')
    compile()

if __name__=='__main__':
    main()