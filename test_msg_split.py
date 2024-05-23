import unittest
from msg_split import split_message

class TestSplitMessage(unittest.TestCase):
    def test_basic_split(self):
        message = "<p>" + "a" * 5000 + "</p>"
        result = list(split_message(message, max_len=4096))
        self.assertEqual(len(result), 2)
        self.assertTrue(all(len(fragment) <= 4096 for fragment in result))
    
    def test_exact_split(self):
        message = "<p>" + "a" * 4096 + "</p>"
        result = list(split_message(message, max_len=4096))
        self.assertEqual(len(result), 1)
        self.assertEqual(len(result[0]), 4100)  # 4096 characters + <p></p> tags
    
    def test_no_split_needed(self):
        message = "<p>Hello, world!</p>"
        result = list(split_message(message, max_len=4096))
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], message)
    
    def test_multiple_tags(self):
        message = "<p>" + "a" * 2000 + "</p><p>" + "b" * 2000 + "</p><p>" + "c" * 2000 + "</p>"
        result = list(split_message(message, max_len=4096))
        self.assertEqual(len(result), 2)
        self.assertTrue(all(len(fragment) <= 4096 for fragment in result))
    
    def test_complex_html(self):
        message = "<div><p>" + "a" * 2000 + "</p><p>" + "b" * 1000 + "</p><span>" + "c" * 1500 + "</span></div>"
        result = list(split_message(message, max_len=4096))
        self.assertEqual(len(result), 2)
        self.assertTrue(all(len(fragment) <= 4096 for fragment in result))

if __name__ == "__main__":
    unittest.main()
