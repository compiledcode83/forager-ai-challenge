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

    def test_find_and_store_email(self):
        domain = "forager.ai"
        first_name = "Nick"
        last_name = "Lucas"

        result = self.service.find_and_store_email(domain, first_name, last_name)
        key = f"{first_name}_{last_name}@{domain}"
        stored_result = self.service.get_found_email_result(key)

        self.assertIsNotNone(result)
        self.assertEqual(result['data']['email'], stored_result['data']['email'])

    def test_search_and_storedomain(self):
        domain = "forager.ai"

        result = self.service.search_and_store_domain(domain)

        stored_count_result = self.service.get_domain_search_result(domain)

        self.assertIsNotNone(result)
        self.assertEqual(result['data']['domain'], stored_count_result['data']['domain'])


if __name__ == "__main__":
    unittest.main()
