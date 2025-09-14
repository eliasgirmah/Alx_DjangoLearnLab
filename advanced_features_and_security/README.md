# advanced_features_and_security

This project is a Django application that demonstrates advanced features and security practices, including the implementation of a custom user model.

## Project Structure

```
advanced_features_and_security/
├── manage.py
├── advanced_features_and_security/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── accounts/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   ├── migrations/
│   │   └── __init__.py
│   └── templates/
│       └── accounts/
│           └── profile.html
├── templates/
│   └── base.html
├── static/
│   └── css/
│       └── base.css
├── requirements.txt
├── .gitignore
└── README.md
```

## Features

- Custom user model extending `AbstractUser` with additional fields:
  - `date_of_birth`: DateField for storing the user's date of birth.
  - `profile_photo`: ImageField for storing the user's profile photo.
  
- User management views for registration and profile updates.

- Admin interface for managing users effectively.

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd advanced_features_and_security
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```
   python manage.py migrate
   ```

5. **Create a superuser:**
   ```
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```
   python manage.py runserver
   ```

## Usage

- Access the admin panel at `http://127.0.0.1:8000/admin` to manage users.
- Visit the user profile page to view and edit user information.

## License

This project is licensed under the MIT License.