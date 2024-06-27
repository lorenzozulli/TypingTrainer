import unittest

from Model import Test

class TestAdministrator(unittest.TestCase):
    def setUp(self):
        self.test1 = Test.Test()
        self.test1.setIdentifier(1)

        self.test2 = Test.Test()
        self.test2.setIdentifier(2)

        self.miaListaTest = [
            self.test1,
            self.test2
        ]
    def eliminaTest(self, identifier):
        try:
            for i in self.miaListaTest:
                if identifier == i.getIdentifier():
                    self.miaListaTest.remove(i)
            return True
        except Exception:
            return False
    
    def testEliminaTest(self):
        result = self.eliminaTest(1)
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
