class VigenereDecoder:
    def __init__(self, key):
        self.key = key
    def encrypt(self, message):
        codedMessage = ''
        keyIndex = 0
        
        for messageLetter in message:
            messageLetterAsInt = ord(messageLetter)
            keyLetterAsInt = ord(self.key[keyIndex])
            codedLetterAsInt = ((messageLetterAsInt + keyLetterAsInt - 130) % 26) + 65
            codedLetter = chr(codedLetterAsInt)
            codedMessage = codedMessage + codedLetter
            
            keyIndex = keyIndex + 1
            keyIndex = keyIndex % len(self.key)
            
        return codedMessage
    
    def decrypt(self, codedMessage):
        message = ''
        keyIndex = 0
        
        for codedLetter in codedMessage:
            codeLetterAsInt = ord(codedLetter)
            keyLetterAsInt = ord(self.key[keyIndex])
            messageLetterAsInt = ((codeLetterAsInt - keyLetterAsInt + 130) % 26) + 65
            messageLetter = chr(messageLetterAsInt)
            message = message + messageLetter
            
            keyIndex = keyIndex + 1
            keyIndex = keyIndex % len(self.key)
            
        return message