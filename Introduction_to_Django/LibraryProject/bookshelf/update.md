book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)

# Nineteen Eighty-Four
# This confirms the title was updated from "1984" to "Nineteen Eighty-Four".