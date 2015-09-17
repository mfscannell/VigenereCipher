class VigenereDecoder:
    def __init__(self, key):
        self.key = key
    def encrypt(self, message):
        codedMessage = ''
        keyIndex = 0
        
        for letter in message:
            letterAsInt = ord(letter)
            keyLetterAsInt = ord(self.key[keyIndex])
            codedLetterAsInt = ((letterAsInt + keyLetterAsInt - 130) % 26) + 65
            codedLetter = chr(codedLetterAsInt)
            codedMessage = codedMessage + codedLetter
            
            keyIndex = keyIndex + 1
            keyIndex = keyIndex % len(self.key)
        return codedMessage