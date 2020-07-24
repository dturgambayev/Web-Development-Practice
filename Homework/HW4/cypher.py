def encrypt(text):
    text = text.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in text:
        if letter in alpha:
            letter_index = (alpha.find(letter) + 5) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result

def decrypt(text):
    text = text.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in text:
        if letter in alpha:
            letter_index = (alpha.find(letter) - 5) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result

def main():
    decision = input("Are you willing to encrypt or decrypt your message? ")
    message = input("Enter your message, please: ")

    if (decision == 'Encrypt' or decision == 'encrypt'):
        print ("Your message: " + message)
        print ("Your encrypted message: " + encrypt(message))
    elif (decision == 'Decrypt' or decision == 'decrypt'):
        print ("Your message: " + message)
        print ("Your decrypted message: " + decrypt(message))

if  __name__=='__main__':
    main()
