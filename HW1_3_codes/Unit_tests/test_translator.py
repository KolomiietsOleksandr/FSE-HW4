import unittest
from translator import CustomTranslator

class TestCustomTranslator(unittest.TestCase):
    def setUp(self):
        self.translator = CustomTranslator()

    def test_translation_uk(self):
        translation = self.translator.translate("online", "uk")
        self.assertEqual(translation, "в мережі")

    def test_translation_unknown_language(self):
        translation = self.translator.translate("online", "en")
        self.assertEqual(translation, "online")

if __name__ == '__main__':
    unittest.main()

#python3 -m unittest test_translator.py
