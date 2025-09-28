from django.db import models

# The Author model represents a writer who can have multiple books.
class Author(models.Model):
    # Author's full name
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# The Book model represents a single book written by an Author.
class Book(models.Model):
    # Title of the book
    title = models.CharField(max_length=200)

    # Year when the book was published
    publication_year = models.IntegerField()

    # ForeignKey creates a one-to-many relationship:
    # One Author can have many Books.
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
