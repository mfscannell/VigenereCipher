from VigenereDecoder import VigenereDecoder

key = raw_input('Enter a key:')
vigenereDecoder = VigenereDecoder(key)

userContinue = True


while userContinue:
    message = raw_input('Enter a message:')
    encodedMessage = vigenereDecoder.encrypt(message)
    decodedMessage = vigenereDecoder.decrypt(encodedMessage)
    print(encodedMessage)
    print(decodedMessage)
    userContinueText = raw_input('Continue?')
    
    if (userContinueText[0].lower() == 'n'):
        userContinue = False