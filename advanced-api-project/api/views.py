from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

# Create your views here.

# This view handles a list of books and the creation of new books.
# GET /api/books/ will list all books.
# POST /api/books/ will create a new book.
class BookListCreateView(generics.ListCreateAPIView):
    """
    API view for listing all books or creating a new book.
    - list(): Returns a list of all Book instances.
    - create(): Creates a new Book instance from the request data.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # IsAuthenticatedOrReadOnly allows unauthenticated users to perform read-only actions (GET, HEAD, OPTIONS)
    # and authenticated users to perform all actions (including POST, PUT, DELETE).

# This view handles retrieving, updating, and deleting a single book.
# GET /api/books/<pk>/ will retrieve a book.
# PUT /api/books/<pk>/ will update a book.
# PATCH /api/books/<pk>/ will partially update a book.
# DELETE /api/books/<pk>/ will delete a book.
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, or deleting a specific book.
    - retrieve(): Returns the details of a single Book instance.
    - update(): Updates an existing Book instance.
    - destroy(): Deletes a Book instance.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]