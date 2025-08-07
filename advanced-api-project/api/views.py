from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

# This view handles retrieving a list of all books.
class BookListView(generics.ListAPIView):
    """
    API view to list all books with advanced query capabilities.
    - **Filtering**: Use query parameters like `?title=...`, `?author__name=...`, `?publication_year=...`.
    - **Searching**: Use `?search=...` to search across book titles and author names.
    - **Ordering**: Use `?ordering=...` to sort by `title` or `publication_year`.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Add filtering, search, and ordering backends
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Enable filtering on these fields
    filterset_fields = ['title', 'publication_year', 'author']

    # Enable searching on these fields (will use a partial match)
    search_fields = ['title', 'author__name']

    # Enable ordering on these fields
    ordering_fields = ['title', 'publication_year']

# This view handles retrieving a single book by its ID.
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# This view handles creating a new book.
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# This view handles updating an existing book.
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# This view handles deleting an existing book.
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]