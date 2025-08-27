from django.contrib import admin
from .models import Book
# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=('title', 'author', 'published_year')
    list_filter=('title', 'published_year')
    search_fields=('title', 'published_year')
    