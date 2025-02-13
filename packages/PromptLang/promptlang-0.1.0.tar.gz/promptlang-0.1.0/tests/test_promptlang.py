import unittest
from promptlang import PromptLang

class TestPromptLang(unittest.TestCase):
    def setUp(self):
        self.data = {"user": {"name": "Alice", "age": 25}}
        self.cache = {}
        self.pl = PromptLang(self.data, self.cache)

    def test_get_nested_value(self):
        self.assertEqual(self.pl.get_nested_value("user.name"), "Alice")
        self.assertEqual(self.pl.get_nested_value("user.age"), 25)
        self.assertIsNone(self.pl.get_nested_value("user.address"))

    def test_generate_prompt(self):
        template = "Hello, {user.name}! Your age is {user.age}."
        result = self.pl.generate_prompt(template)
        self.assertEqual(result, "Hello, Alice! Your age is 25.")

if __name__ == "__main__":
    unittest.main()