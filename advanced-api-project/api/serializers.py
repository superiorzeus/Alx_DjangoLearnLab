from rest_framework import serializers
from .models import Author, Book
from datetime import date

# BookSerializer handles the serialization of the Book model.
# It includes a custom validation method to ensure the publication_year is valid.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year']

    def validate_publication_year(self, value):
        """
        Checks that the publication year is not in the future.
        """
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# AuthorSerializer serializes the Author model.
# It includes a nested BookSerializer to show the author's related books.
# The 'books' field name matches the 'related_name' in the Author model's ForeignKey.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']