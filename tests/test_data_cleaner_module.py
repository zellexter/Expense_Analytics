import unittest
from Data_Cleaner_Module import capitalize, convert_str, convert_float

class TestCapitalize(unittest.TestCase):

    def test_capitalize_single_word(self):
        self.assertEqual(capitalize("hello"), "Hello")

    def test_capitalize_multiple_words(self):
        self.assertEqual(capitalize("hello world"), "Hello World")

    def test_capitalize_with_numbers(self):
        self.assertEqual(capitalize("hello 123 world"), "Hello 123 World")

    def test_capitalize_with_punctuation(self):
        self.assertEqual(capitalize("hello, world!"), "Hello, World!")

    def test_capitalize_already_capitalized(self):
        self.assertEqual(capitalize("Hello World"), "Hello World")

    def test_capitalize_mixed_case(self):
        self.assertEqual(capitalize("hElLo WoRlD"), "Hello World")

    def test_capitalize_empty_string(self):
        self.assertEqual(capitalize(""), "")

    def test_capitalize_only_spaces(self):
        self.assertEqual(capitalize("   "), "   ")

    def test_capitalize_with_leading_spaces(self):
        self.assertEqual(capitalize("   hello world"), "   Hello World")

    def test_capitalize_with_trailing_spaces(self):
        self.assertEqual(capitalize("hello world   "), "Hello World   ")

if __name__ == '__main__':
    unittest.main()

    
class TestConvertStr(unittest.TestCase):

    def test_convert_str_integer(self):
        self.assertEqual(convert_str(123), "123")

    def test_convert_str_float(self):
        self.assertEqual(convert_str(3.14), "3.14")

    def test_convert_str_boolean(self):
        self.assertEqual(convert_str(True), "True")
        self.assertEqual(convert_str(False), "False")

    def test_convert_str_none(self):
        self.assertEqual(convert_str(None), "None")

    def test_convert_str_list(self):
        self.assertEqual(convert_str([1, 2, 3]), "[1, 2, 3]")

    def test_convert_str_dict(self):
        self.assertEqual(convert_str({"a": 1, "b": 2}), "{'a': 1, 'b': 2}")

    def test_convert_str_already_string(self):
        self.assertEqual(convert_str("hello"), "hello")

    def test_convert_str_empty_string(self):
        self.assertEqual(convert_str(""), "")

    def test_convert_str_special_characters(self):
        self.assertEqual(convert_str("!@#$%^&*()"), "!@#$%^&*()")

    def test_convert_str_unicode(self):
        self.assertEqual(convert_str("こんにちは"), "こんにちは")


class TestConvertFloat(unittest.TestCase):

    def test_convert_float_integer(self):
        self.assertEqual(convert_float(5), 5.0)

    def test_convert_float_negative(self):
        self.assertEqual(convert_float(-3.14), -3.14)

    def test_convert_float_zero(self):
        self.assertEqual(convert_float(0), 0.0)

    def test_convert_float_string(self):
        self.assertEqual(convert_float("2.718"), 2.718)

    def test_convert_float_scientific_notation(self):
        self.assertEqual(convert_float("1e-3"), 0.001)

    def test_convert_float_large_number(self):
        self.assertEqual(convert_float(1000000000), 1000000000.0)

    def test_convert_float_small_number(self):
        self.assertEqual(convert_float(0.000001), 0.000001)

    def test_convert_float_infinity(self):
        self.assertEqual(convert_float(float('inf')), float('inf'))

    def test_convert_float_negative_infinity(self):
        self.assertEqual(convert_float(float('-inf')), float('-inf'))

    def test_convert_float_invalid_string(self):
        with self.assertRaises(ValueError):
            convert_float("not a number")

    def test_convert_float_none(self):
        with self.assertRaises(TypeError):
            convert_float(None)

    def test_convert_float_bool(self):
        self.assertEqual(convert_float(True), 1.0)
        self.assertEqual(convert_float(False), 0.0)
