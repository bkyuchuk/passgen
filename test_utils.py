import unittest
import utils


class TestUtils(unittest.TestCase):
    def test_create_password_default(self):
        result = utils.create_password()
        self.assertEqual(len(result), 8)

    def test_create_password_no_numbers(self):
        result = utils.create_password(length=20, has_numbers=False)

        self.assertEqual(len(result), 20)
        self.assertFalse(any(number in utils.NUMBERS for number in result))

    def test_create_password_no_symbols(self):
        result = utils.create_password(length=20, has_symbols=False)

        self.assertEqual(len(result), 20)
        self.assertFalse(any(element in utils.SYMBOLS for element in result))

    def test_generate_password(self):
        # Generate password of length 20 with letters, numbers and symbols.
        available_chars = "".join([utils.ALPHA, utils.NUMBERS, utils.SYMBOLS])
        result = utils.generate_password(length=20, chars=available_chars)

        self.assertEqual(len(result), 20)
        self.assertTrue(any(character in utils.ALPHA for character in result))
        self.assertTrue(any(number in utils.NUMBERS for number in result))
        self.assertTrue(any(element in utils.SYMBOLS for element in result))

    def test_save_password(self):
        pass

    def test_copy_to_clipboard(self):
        pass


if __name__ == "__main__":
    unittest.main()
