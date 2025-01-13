from typing import Any, Dict, Optional
from sdk.api_client import HunterAPIClient
from sdk.data_storage import DataStorage


class EmailValidationService:
    def __init__(self, api_key: str) -> None:
        self.client: HunterAPIClient = HunterAPIClient(api_key)
        self.storage: DataStorage = DataStorage()

    def validate_and_store_email(self, email: str) -> Dict[str, Any]:
        result = self.client.validate_email(email)
        self.storage.create(email, result)
        return result

    def find_and_store_email(self, domain: str, first_name: str, last_name: str) -> Dict[str, Any]:
        result = self.client.find_email(domain, first_name, last_name)
        key = f"{first_name}_{last_name}@{domain}"  # Create a unique key for storage
        self.storage.create(key, result)
        return result

    def search_and_store_domain(self, domain: str) -> Dict[str, Any]:
        result = self.client.search_domain(domain)
        self.storage.create(domain, result)
        return result

    def get_email_validation_result(self, email: str) -> Optional[Dict[str, Any]]:
        return self.storage.read(email)

    def get_found_email_result(self, key: str) -> Optional[Dict[str, Any]]:
        return self.storage.read(key)

    def get_domain_search_result(self, domain: str) -> Optional[Dict[str, Any]]:
        return self.storage.read(domain)
