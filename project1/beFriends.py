
import messages

def friend_request(counter, answer):
    if messages.request(counter, answer) == 1:
        print('You`re already friends!')
        authorization(counter, answer)
    else:
        choice = input('Are you willing to send a request to user ' + str(answer) + '? ')

        if choice == 'yes' or choice == 'Yes' or choice == 'YES' or choice == 'Yup' or choice == 'YUP' or choice == 'yup' or choice == 'sure' or choice == 'Sure' or choice == 'SURE':
            messages.friend_message(counter, answer, 'Friend request!')
            authorization(counter, answer)
        elif choice == 'no' or choice == 'No' or choice == 'NO' or choice == 'nope' or choice == 'Nope' or choice == 'NOPE':
            authorization(counter, answer)

def friend_chat(counter, answer):
    if messages.request(counter, answer) != 1:
        print('You`re allowed to send messages only to your friend. Send friend request to '+str(answer) + ' if you want to message!')
        authorization(counter, answer)
    else:
        message = input('Type your message: ')
        messages.friend_message(counter, answer, message)
        authorization(counter, answer)

def unfriend(counter, answer):
    if messages.request(counter, answer) == 1:
        messages.friend_delete(counter, answer)
        print('You`re not friend with ' + str(answer) + ' anymore')
    else:
        print(str(answer) + ' is not your friend!')
        authorization(counter, answer)


def authorization(counter, answer):
    choice = input('Your option: ')
    if choice == '1':
        friend_request(counter, answer)
    elif choice == '2':
        friend_chat(counter, answer)
    elif choice == '3':
        unfriend(counter, answer)
    elif choice == '4':
        import user_account
        user_account.main(counter)
    else:
        print('Invalid input!')
        authorization(counter, answer)

def main(counter, answer):
    print('Send a friend request <PRESS 1>')
    print('Start to chat <PRESS 2>')
    print('Unfriend <PRESS 3>')
    print('Back <PRESS 4>')
    authorization(counter, answer)
if __name__=='__main__':
    main()