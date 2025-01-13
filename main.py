import os
from dotenv import load_dotenv
from typing import Any, Dict, Optional
from sdk.service import EmailValidationService


def main() -> None:
    load_dotenv()
    api_key: str = os.getenv("HUNTER_API_KEY")
    if not api_key:
        raise ValueError("HUNTER_API_KEY not found in .env file")

    service: EmailValidationService = EmailValidationService(api_key)

    # Validate and store email
    email: str = "nick@forager.ai"
    validation_result: Dict[str, Any] = service.validate_and_store_email(email)
    print("Validation Result:", validation_result)

    # Retrieve stored validation result
    stored_validation_result: Optional[Dict[str, Any]] = service.get_email_validation_result(email)
    print("Stored Result:", stored_validation_result)

    # Find and store email
    domain = "forager.ai"
    first_name = "Nick"
    last_name = "Lucas"
    find_result = service.find_and_store_email(domain, first_name, last_name)
    print("Email find Result:", find_result)

    # Retrieve stored validation result
    stored_found_result: Optional[Dict[str, Any]] = service.get_found_email_result(f"{first_name}_{last_name}@{domain}")
    print("Stored Result:", stored_found_result)

    # Search a domain
    domain_search_result = service.search_and_store_domain(domain)
    print("Domain Search Result:", domain_search_result)

    # Retrieve stored validation result
    stored_found_result: Optional[Dict[str, Any]] = service.get_domain_search_result(domain)
    print("Stored Result:", stored_found_result)


if __name__ == "__main__":
    main()
