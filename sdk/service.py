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

    def get_email_validation_result(self, email: str) -> Optional[Dict[str, Any]]:
        return self.storage.read(email)
