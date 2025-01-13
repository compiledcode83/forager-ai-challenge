from typing import Any, Dict, Optional
import requests


class HunterAPIClient:
    BASE_URL: str = "https://api.hunter.io/v2/"

    def __init__(self, api_key: str) -> None:
        self.api_key: str = api_key

    def validate_email(self, email: str) -> Dict[str, Any]:
        return self._get("email-verifier", {"email": email})

    def find_email(self, domain: str, first_name: str, last_name: str) -> Dict[str, Any]:
        return self._get("email-finder", {"domain": domain, "first_name": first_name, "last_name": last_name})

    def search_domain(self, domain: str) -> Dict[str, Any]:
        return self._get("domain-search", {"domain": domain})

    def _get(self, endpoint: str, params: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        if params is None:
            params = {}
        params['api_key'] = self.api_key

        response = requests.get(f"{self.BASE_URL}{endpoint}", params=params)
        response.raise_for_status()  # Raise an error for bad responses

        return response.json()
