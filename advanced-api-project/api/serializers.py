from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# Serializer for the Book model
# Purpose: Convert Book model instances to JSON and validate incoming data
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Custom validation to ensure publication_year is not in the future
    def validate_publication_year(self, value):
        """
        Ensures the publication year is not greater than the current year.
        Raises ValidationError if the year is invalid.
        """
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# Serializer for the Author model
# Purpose: Convert Author model instances to JSON and include nested book data.
class AuthorSerializer(serializers.ModelSerializer):
    # Nested BookSerializer to dynamically include all related books
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

    """
    Relationship Handling:
    - The AuthorSerializer uses the related_name='books' defined in the Book model's ForeignKey.
    - This allows Django REST Framework to automatically include all related Book instances
      when serializing an Author.
    - The books field is set to read_only=True to prevent creating books directly
      through AuthorSerializer — books are created separately via BookSerializer.
    """
