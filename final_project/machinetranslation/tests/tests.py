import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_not_equal_fr_to_en(self):
        data = None
        result = french_to_english(data)
        self.assertNotEqual(result,"" , "Should be null")

    def test_not_equal_en_to_fr(self):
        data = None
        result = english_to_french(data)
        self.assertNotEqual(result,"" , "Should be null")

    def test_equal_en_to_fr(self):
        data= "Hello"
        result = english_to_french(data)
        self.assertEqual(result, "Bonjour", "Should be Bonjour")

    def test_equal_fr_to_en(self):
        data= "Bonjour"
        result = french_to_english(data)
        self.assertEqual(result, "Hello", "Should be Hello")

if __name__ == "__main__":
    unittest.main()

