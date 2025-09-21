from rest_framework import generics
from rest_framework import viewsets
from.models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    """
    API view to list all books.
    """
    queryset = Book.objects.all()           # Fetch all books from the database
    serializer_class = BookSerializer       # Use BookSerializer to convert to JSON

class BookViewSet(viewsets.ModelViewSet):
    """
    API view to list all books or create a new book.
    """
    queryset = Book.objects.all()           # Fetch all books from the database
    serializer_class = BookSerializer       # Use BookSerializer to convert to/from JSON