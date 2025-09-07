from django.urls import path
from . import views

app_name = 'relationship_app'

urlpatterns = [
    # -----------------------------
    # Authentication URLs
    # -----------------------------
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # -----------------------------
    # Book Views
    # -----------------------------
    path('books/', views.list_books, name='list_books'),
    path('books/add/', views.add_book, name='add_book'),               # <-- add_book
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),   # <-- edit_book
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),

    # -----------------------------
    # Library Views
    # -----------------------------
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # -----------------------------
    # Role-Based Views
    # -----------------------------
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
]
