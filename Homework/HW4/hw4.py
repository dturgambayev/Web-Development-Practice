def compile():
    answer = input('Hello Daniyar! Which file do you want to compile? <between 1 and 3> ')
    if answer == '1':
        import cypher
        cypher.main()
    elif answer == '2':
        import guess
        guess.main()
    elif answer == '3':
        import time_machine
        time_machine.main()
    else:
        exit()

def main():
    compile()

if __name__=='__main__':
    main()