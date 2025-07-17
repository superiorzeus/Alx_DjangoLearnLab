import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author = Author.objects.get(name="Chinua Achebe")
books_by_author = author.books.all()
print("Books by Chinua Achebe:", [book.title for book in books_by_author])

# 2. List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(f"Books in {library_name}:", [book.title for book in books_in_library])

# 3. Retrieve the librarian for a library
librarian = library.librarian  # reverse OneToOneField
print(f"Librarian for {library_name}:", librarian.name)
