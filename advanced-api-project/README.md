📘 Advanced API Project – Django REST Framework
Overview

This project is a Django REST Framework (DRF) based API that demonstrates:

Custom models (Author and Book).

Custom serializers with nested relationships and validation.

Generic views for CRUD operations.

Permissions to protect API endpoints.

The API is structured to allow read-only access for public users, and restricted create/update/delete access for authenticated users.

🚀 Features
Models

Author

name (string)

Can have many related books.

Book

title (string)

publication_year (integer)

author (foreign key → Author)

Serializers

BookSerializer

Serializes all book fields.

Custom validation: prevents publication_year from being set in the future.

AuthorSerializer

Serializes id, name, and all related books (nested BookSerializer).

Views (Generic DRF Views)

BookListView – GET /api/books/ → List all books. (public)

BookDetailView – GET /api/books/<id>/ → Retrieve one book by ID. (public)

BookCreateView – POST /api/books/create/ → Add a new book. (authenticated)

BookUpdateView – PUT/PATCH /api/books/<id>/update/ → Update a book. (authenticated)

BookDeleteView – DELETE /api/books/<id>/delete/ → Delete a book. (authenticated)

🔑 Permissions

Public (unauthenticated users):

Can list all books.

Can retrieve single books.

Authenticated users:

Can create, update, and delete books.

(DRF permission classes used: AllowAny and IsAuthenticated).

🛠 Installation & Setup

Clone the repo & navigate to the folder:

git clone <repo-url>
cd advanced-api-project


Create and activate virtual environment:

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows


Install dependencies:

pip install django djangorestframework


Apply migrations:

python manage.py migrate


Create a superuser (for admin access):

python manage.py createsuperuser


Run the server:

python manage.py runserver

📡 API Endpoints
Books
Method	Endpoint	Description	Auth Required
GET	/api/books/	List all books	No
GET	/api/books/<id>/	Get book by ID	No
POST	/api/books/create/	Create new book	Yes
PUT	/api/books/<id>/update/	Update book by ID	Yes
PATCH	/api/books/<id>/update/	Partially update book	Yes
DELETE	/api/books/<id>/delete/	Delete book by ID	Yes