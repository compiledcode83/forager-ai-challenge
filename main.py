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

    email: str = "nick@forager.ai"

    # Validate and store email
    validation_result: Dict[str, Any] = service.validate_and_store_email(email)
    print("Validation Result:", validation_result)

    # Retrieve stored validation result
    stored_result: Optional[Dict[str, Any]] = service.get_email_validation_result(email)
    print("Stored Result:", stored_result)


if __name__ == "__main__":
    main()
