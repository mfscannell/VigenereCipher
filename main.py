import VigenereDecoder

key = raw_input('Enter a key:')
vigenereDecoder = VigenereDecoder.VigenereDecoder(key)
encodedMessage = vigenereDecoder.encrypt('HELLOWORLD')
print(encodedMessage)