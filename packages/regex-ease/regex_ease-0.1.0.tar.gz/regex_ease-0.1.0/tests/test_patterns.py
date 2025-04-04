import unittest
from regex_ease.validators import Validators

class TestEasyRegex(unittest.TestCase):
    def test_valid_email(self):
        self.assertTrue(Validators.is_valid_email("test@example.com"))

    def test_invalid_email(self):
        self.assertFalse(Validators.is_valid_email("invalid-email"))
        self.assertFalse(Validators.is_valid_email("missing@domain"))
    
    def test_get_domain(self):
        self.assertEqual(Validators.get_email_domain("user@example.com"), "example.com")
        self.assertIsNone(Validators.get_email_domain("invalidemail"))

if __name__ == "__main__":
    unittest.main()