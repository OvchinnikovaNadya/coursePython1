# Тест на базе unittest
import unittest
import strings

class TestUpper(unittest.TestCase):
    def test_one_word(self):
        text = 'hello!'
        result = strings.upper_text(text)
        self.assertEqual(result, 'HELLO!')
        self.assertNotEqual(result, 'hello!')

    def test_multiple_worlds(self):
        text = 'мой пк'
        result = strings.upper_text(text)
        self.assertEqual(result, 'МОЙ ПК')

if __name__ == '__main__':
    unittest.main()
