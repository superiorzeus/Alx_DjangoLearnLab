from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
# Create your models here.

# The Author model stores basic information about a book's author.
# It has a one-to-many relationship with the Book model.
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# The Book model represents a book and its details.
# It links to an Author via a ForeignKey, meaning an author can have many books.
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

    def clean(self):
        # Custom validation to ensure publication_year is not in the future.
        if self.publication_year > date.today().year:
            raise ValidationError(
                'Publication year cannot be in the future.'
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)