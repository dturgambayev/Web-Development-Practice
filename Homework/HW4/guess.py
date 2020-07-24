import random

def guess_game():
    user_name = input('Hello! What is your name? ')
    number = random.randint(1, 10000)
    guesses_taken = 0
    print('Well, ' + user_name + ', I am thinking of a number between 1 and 10000.')
    while True:
        guess = input('Take a guess: ')
        guess = int(guess)
        guesses_taken = guesses_taken + 1
        if guess < number:
            print('My number is greater.')
        if guess > number:
            print('My number is less.')
        if guess == number:
            guesses_taken = str(guesses_taken)
            print('Good job, ' + user_name + '! You guessed my number in ' + guesses_taken + ' guesses!')
            break

def main():
    guess_game()

if  __name__=='__main__':
    main()