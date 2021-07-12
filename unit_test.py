import unittest
import being_test


class TestCap(unittest.TestCase):

    def test_a_word(self):
        text = 'python'
        result = being_test.capi_txt(text)
        self.assertEqual(result, 'Python')
        #result == expected result

    def test_multiple_words(self):
        text = 'a python'
        result = being_test.capi_txt(text)
        self.assertEqual(result, 'A Python')


if __name__ == '__main__':
    unittest.main()


