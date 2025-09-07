from django.urls import path
from relationship_app.views import add_book
from relationship_app.views import edit_book
from relationship_app.views import(
    register_view, login_view, logout_view,
    list_books, add_book, edit_book, delete_book,
    LibraryDetailView,
    admin_view, librarian_view, member_view
)

app_name = 'relationship_app'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('books/', list_books, name='list_books'),
    path('books/add/', add_book, name='add_book'),           # must exist
    path('books/<int:pk>/edit/', edit_book, name='edit_book'), # must exist
    path('books/<int:pk>/delete/', delete_book, name='delete_book'),

    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
]
