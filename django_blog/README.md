# Django Blog — Post Management

Features:
- Post model: title, content, published_date, author
- CRUD: list, detail, create, update, delete
- Permissions: only authenticated users can create; only author can edit/delete
- Templates: blog/templates/blog/*.html

Setup:
1. Create virtualenv and install requirements (Django 5.2.6)
2. Run: python manage.py migrate
3. Create superuser: python manage.py createsuperuser
4. Run server: python manage.py runserver

Testing:
- Register via /register/, create posts via /posts/new/
- Ensure edit/delete are only available to the post author
