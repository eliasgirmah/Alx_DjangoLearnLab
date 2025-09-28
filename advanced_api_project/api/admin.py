from django.contrib import admin
from .models import Author, Book

# Register Author model to admin site
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Columns to display in admin
    search_fields = ('name',)       # Search by author name

# Register Book model to admin site
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publication_year', 'author')
    list_filter = ('publication_year',)  # Filter books by year
    search_fields = ('title',)
