from src.VigenereCracker import VigenereCracker

filePath = raw_input('Enter the location of a dictionary:')
VigenereCracker.readDictionary(filePath)

userContinue = True

while userContinue:
    codedMessage = raw_input('Enter a coded message:')
    keyLength = raw_input('Enter a key length:')
    keyLength = int(keyLength)
    firstWordLength = raw_input('Enter a first word length:')
    firstWordLength = int(firstWordLength)
    
    vigenereCracker = VigenereCracker(keyLength)
    vigenereCracker.crackMessage(codedMessage, firstWordLength)
    
    userContinueText = raw_input('Continue?')
    
    if (userContinueText[0].lower() == 'n'):
        userContinue = False