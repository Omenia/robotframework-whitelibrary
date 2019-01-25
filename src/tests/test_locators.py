import unittest
from WhiteLibrary import WhiteLibrary


class TestLocatorParsing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lib = WhiteLibrary()

    def test_no_delimiter(self):
        prefix, value = self.lib._parse_locator("id")
        self.assertEqual(prefix, "id")
        self.assertEqual(value, "id")

    def test_delimiter_colon(self):
        prefix, value = self.lib._parse_locator("index:15")
        self.assertEqual(prefix, "index")
        self.assertEqual(value, "15")

    def test_delimiter_equals(self):
        prefix, value = self.lib._parse_locator("class_name:ComboBox")
        self.assertEqual(prefix, "class_name")
        self.assertEqual(value, "ComboBox")

    def test_delimiter_colon_first(self):
        prefix, value = self.lib._parse_locator("text:=")
        self.assertEqual(prefix, "text")
        self.assertEqual(value, "=")

    def test_delimiter_equals_first(self):
        prefix, value = self.lib._parse_locator("text=Value:")
        self.assertEqual(prefix, "text")
        self.assertEqual(value, "Value:")

    def test_locator_value_contains_delimiter_symbol(self):
        prefix, value = self.lib._parse_locator("text:Value:")
        self.assertEqual(prefix, "text")
        self.assertEqual(value, "Value:")
