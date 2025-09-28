from rest_framework import generics, permissions
from .models import Author
from .serializers import AuthorSerializer


class AuthorListView(generics.ListAPIView):
    """
    GET /authors/
    Lists all authors with their nested books.
    Public access.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]


class AuthorDetailView(generics.RetrieveAPIView):
    """
    GET /authors/<id>/
    Retrieves a single author and their books.
    Public access.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]


class AuthorCreateView(generics.CreateAPIView):
    """
    POST /authors/create/
    Creates a new author.
    Authenticated users only.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]


class AuthorUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH /authors/<id>/update/
    Updates an existing author.
    Authenticated users only.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]


class AuthorDeleteView(generics.DestroyAPIView):
    """
    DELETE /authors/<id>/delete/
    Deletes an author (and their books).
    Authenticated users only.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]
