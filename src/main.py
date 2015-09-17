from src.VigenereDecoder import VigenereDecoder

key = raw_input('Enter a key:')
vigenereDecoder = VigenereDecoder(key)
encodedMessage = vigenereDecoder.encrypt('HELLOWORLD')
decodedMessage = vigenereDecoder.decrypt('HFLMOXOSLE')
print(encodedMessage)
print(decodedMessage)