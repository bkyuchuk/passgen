import unittest

# When only 'passgen' is typed, the program should output:
#   (in purple)Generated Password: (in green)I!!^Cz%%
#   (in yellow)Password copied to clipboard.

# 1. The program should generate an 8 char password.
# 2. The password should contain letters, special chars and numbers.
# 3. The password should be copied to the clipboard.


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
