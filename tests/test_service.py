import os
import unittest
from dotenv import load_dotenv
from sdk.service import EmailValidationService


class TestEmailValidationService(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        load_dotenv()
        cls.api_key = os.getenv("HUNTER_API_KEY")
        if not cls.api_key:
            raise ValueError("HUNTER_API_KEY not found in .env file")

    def setUp(self):
        self.service = EmailValidationService(self.api_key)

    def test_validate_and_store_email(self):
        email = "nick@forager.ai"
        result = self.service.validate_and_store_email(email)
        self.assertIsNotNone(result)
        self.assertEqual(result['data']['email'], email)

    def test_get_email_validation_result(self):
        email = "nick@forager.ai"
        self.service.validate_and_store_email(email)
        stored_result = self.service.get_email_validation_result(email)
        self.assertIsNotNone(stored_result)


if __name__ == "__main__":
    unittest.main()
