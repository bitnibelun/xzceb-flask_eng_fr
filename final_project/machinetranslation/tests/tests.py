from .translator import english_to_french, french_to_english
import unittest

class TestTranslate(unittest.TestCase):
    def test_englishToFrench_null(self):
        englishText = None
        result = english_to_french(englishText)
        self.assertEqual(result, "Bonjour")

    def test_englishToFrench(self):
        englishText = "Hello"
        result = english_to_french(englishText)
        self.assertEqual(result, "Bonjour")

    def test_frenchToEnglish_null(self):
        frenchText = None
        result = french_to_english(frenchText)
        self.assertEqual(result, "Hello")

    def test_frenchToEnglish(self):
        frenchText = "Bonjour"
        result = french_to_english(frenchText)
        self.assertEqual(result, "Hello")

if __name__ == '__main__':
    unittest.main()
