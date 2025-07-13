book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()

# <QuerySet []>
# This confirms the book was deleted, as the queryset is empty.