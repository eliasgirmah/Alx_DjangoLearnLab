from django.urls import path
from relationship_app.views import (
    register_view, login_view, logout_view,
    list_books, add_book, edit_book, delete_book,
    LibraryDetailView,
    admin_view, librarian_view, member_view
)

app_name = 'relationship_app'

urlpatterns = [
    # Authentication URLs
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    # Book URLs
    path('books/', list_books, name='list_books'),
    path('books/add/', add_book, name='add_book'),
    path('books/<int:pk>/edit/', edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', delete_book, name='delete_book'),

    # Library Detail
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Role-Based Views
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
]
