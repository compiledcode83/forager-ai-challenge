# Email Validation SDK

This project is a Python SDK for interacting with the Hunter.io API, providing functionalities to validate emails, find emails based on names and domains, and count emails for a given domain.

## Project Structure

    forager-ai-challenge/
    ├── sdk/
    │ ├── init.py
    │ ├── api_client.py   # Contains the API client for Hunter.io
    │ ├── data_storage.py   # In-memory data storage implementation
    │ └── service.py   # Service layer for email validation and storage
    ├── tests/   # Contains unit tests for the SDK
    │ └── test_service.py   # Tests for the EmailValidationService
    ├── .env   # Environment variables (e.g., API key)
    ├── setup.cfg   # Configuration file for linters and type checkers
    ├── main.py   # Main application logic to demonstrate SDK usage
    └── README.md   # Project documentation

## Installation

1. **Clone the Repository**:

```
git clone https://github.com/compiledcode83/forager-ai-challenge
cd sdk_project
```

2. **Create a Virtual Environment**:

```
python -m venv venv
```

3. **Activate the Virtual Environment**:

- On macOS/Linux:

  ```
  source venv/bin/activate
  ```

- On Windows:

  ```
  venv\Scripts\activate
  ```

4. **Install Required Packages**:
   Install the necessary dependencies using pip:

```
pip install requests python-dotenv
```

5. **Set Up Environment Variables**:
   Create a `.env` file in the root directory of your project and add your Hunter.io API key:

```
HUNTER_API_KEY=your_actual_api_key_here
```

## Running the SDK

To run the main application and see the SDK in action, execute the following command:

```
python main.py
```

This will demonstrate email validation, finding an email based on provided names and domain, and search a domain.

## Testing the SDK

To run unit tests for the SDK, use the following command:

```
python -m unittest discover tests/
```

This command will discover and run all tests in the `tests` directory.
