from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# <Book: 1984>
# This indicates the successful creation of a Book instance with title "1984".