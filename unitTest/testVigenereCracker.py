
import unittest
from src.VigenereCracker import VigenereCracker

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInitialCandidateKeyLength(self):
        vigenereCracker = VigenereCracker(9, 4)
        initialCandidateKey = vigenereCracker.getInitialCandidateKey(9)
        self.assertTrue(len(initialCandidateKey) == 9)
        self.assertTrue(initialCandidateKey == 'AAAAAAAAA')

    def testInitialCandidateKeyContent(self):
        vigenereCracker = VigenereCracker(9, 4)
        initialCandidateKey = vigenereCracker.getInitialCandidateKey(9)
        self.assertTrue(initialCandidateKey == 'AAAAAAAAA')

    def testIncrementCandidateKey(self):
        vigenereCracker = VigenereCracker(3, 4)
        startKey = 'ABC'
        endKey = vigenereCracker.incrementCandidateKey(startKey)
        self.assertTrue(endKey == 'ABD')

    def testIncrementCandidateKeyIncr(self):
        vigenereCracker = VigenereCracker(3, 4)
        startKey = 'ABZ'
        endKey = vigenereCracker.incrementCandidateKey(startKey)
        self.assertTrue(endKey == 'ACA')

    def testIncrementCandidateKeyRoll(self):
        vigenereCracker = VigenereCracker(3, 4)
        startKey = 'ZZZ'
        endKey = vigenereCracker.incrementCandidateKey(startKey)
        self.assertTrue(endKey == 'AAAA')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
