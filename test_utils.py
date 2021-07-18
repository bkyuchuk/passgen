import unittest
import utils
import os.path


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
        first_password = "first dummy password to save"
        second_password = "second dummy password to save"

        utils.save_password(first_password)
        utils.save_password(second_password)

        file_path = os.path.join(os.getcwd(), "passwords.txt")
        self.assertTrue(os.path.isfile(file_path))

        with open("passwords.txt") as passwords_file:
            file_lines = passwords_file.readlines()

        self.assertEqual(first_password, file_lines[0].strip())
        self.assertEqual(second_password, file_lines[1].strip())

        os.remove(file_path)

    def test_copy_to_clipboard(self):
        pass


if __name__ == "__main__":
    unittest.main()
