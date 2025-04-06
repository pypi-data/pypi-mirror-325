# User Management

A Python package for managing user-related operations using Firebase Authentication.

## Installation

You can install the package using pip:

```bash
pip install user-management
```

## Prerequisites

1. A Firebase project
2. Firebase service account credentials (as a JSON file or dictionary)
   - Go to Firebase Console
   - Project Settings > Service Accounts
   - Generate New Private Key

## Usage

```python
from user_management import FirebaseClient, FirebaseUser

# Initialize the client with your service account credentials
# Method 1: Using a credentials file path (recommended)
client = FirebaseClient("path/to/firebase-credentials.json")

# Method 2: Using a credentials dictionary
client = FirebaseClient({
    "type": "service_account",
    "project_id": "your-project-id",
    "private_key_id": "key-id",
    "private_key": "-----BEGIN PRIVATE KEY-----\n...",
    "client_email": "firebase-adminsdk...iam.gserviceaccount.com",
    "client_id": "...",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/..."
})

# Create a new user
user = client.create_user(
    email="user@example.com",
    password="securepassword123",
    display_name="John Doe"
)
print(f"Created user: {user.uid}")

# Get user information
user = client.get_user(uid="user123")
print(f"User email: {user.email}")

# Update user
updated_user = client.update_user(
    uid="user123",
    display_name="John Smith",
    email="new.email@example.com"
)

# Set custom claims (e.g., for role-based access)
client.set_custom_claims("user123", {"admin": True})

# Verify a Firebase ID token
token_claims = client.verify_token("firebase-id-token")
print(f"User ID: {token_claims['uid']}")

# Delete a user
client.delete_user("user123")
```

## Features

- User creation and management
- User information retrieval and updates
- Custom claims management
- JWT token verification
- Type-safe with Pydantic models
- Full Firebase Authentication integration
- Flexible initialization with file path or credentials dictionary
- Strong type hints and documentation

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.