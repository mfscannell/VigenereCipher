

class VigenereCracker:
    key = ''
    keyLength = 2
    candidateKeys = []
    candidateMessages = []
    validWords = []
    
    @staticmethod
    def readDictionary(dictionaryFilePath):
        fileReader = open(dictionaryFilePath, 'r')
        fileContents = fileReader.read()
        fileReader.close()
        VigenereCracker.validWords = fileContents.split()
    
    def __init__(self, keyLength):
        self.keyLength = keyLength
        
    def crackMessage(self, codedMessage, firstWordLength):
        self.key = self.getInitialCandidateKey(self.keyLength)
        
        while len(self.key) == self.keyLength:
            candidateMessage = self.decrypt(codedMessage)
            
            firstWord = candidateMessage[:firstWordLength]
            
            if firstWord in VigenereCracker.validWords:
                self.candidateMessages.append(candidateMessage)
                self.candidateKeys.append(self.key)
                print(self.key + ':' + candidateMessage)
            
            self.key = self.incrementCandidateKey(self.key)
    
    def getInitialCandidateKey(self, keyLength):
        i = 0
        candidateKey = ''
        
        while i < keyLength:
            candidateKey = candidateKey + 'A'
            i = i + 1
            
        return candidateKey
    
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
    
    def incrementCandidateKey(self, candidateKey):
        candidateKeyListInt = self.convertKeyToListInt(candidateKey)
        candidateKeyListInt = self.incrementKey(candidateKeyListInt)
        candidateKey = self.convertListToString(candidateKeyListInt)
        return candidateKey
            
    def convertKeyToListInt(self, key):
        keyListInt = list(key)
        
        for i in range(len(key)):
            keyListInt[i] = ord(keyListInt[i])
            
        return keyListInt
    
    def incrementKey(self, key):
        carryOver = 1
        listIndex = len(key) - 1
        while carryOver > 0:
            if listIndex == -1:
                key = [65] + key
            else:
                key[listIndex] = key[listIndex] + 1
            
            if key[listIndex] > 90:
                key[listIndex] = 65
                carryOver = 1
                listIndex = listIndex - 1
            else:
                carryOver = 0
                
        return key
    
    def convertListToString(self, key):
        for i in range(len(key)):
            key[i] = chr(key[i])
            
        return ''.join(key)
    
    def printMessages(self):
        for message in self.candidateMessages:
            print(message)
    