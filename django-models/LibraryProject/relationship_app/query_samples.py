import os
import django
import sys


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# -----------------------------
# 1️⃣ Query all books by a specific author
# -----------------------------
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()  # related_name from Book model
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name: {author_name}")

# -----------------------------
# 2️⃣ List all books in a library
# -----------------------------
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()  # ManyToMany relation
        print(f"Books in library '{library_name}':")
        for book in books:
            print(f"- {book.title} by {book.author.name}")
    except Library.DoesNotExist:
        print(f"No library found with name: {library_name}")

# -----------------------------
# 3️⃣ Retrieve the librarian for a library
# -----------------------------
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian  # OneToOne relation
        print(f"Librarian for '{library_name}': {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with name: {library_name}")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to library '{library_name}'")

# -----------------------------
# Example usage
# -----------------------------
if __name__ == '__main__':
    books_by_author("J.K. Rowling")
    print("\n")
    books_in_library("Central Library")
    print("\n")
    librarian_for_library("Central Library")
