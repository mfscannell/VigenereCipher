import unittest

from src.VigenereDecoder import VigenereDecoder

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testEncrypt(self):
        vigenereDecoder = VigenereDecoder('AB')
        codedMessage = vigenereDecoder.encrypt('HELLOWORLD')
        self.assertTrue(codedMessage == 'HFLMOXOSLE')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()