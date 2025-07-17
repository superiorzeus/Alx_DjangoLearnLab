from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Library

# Create your views here.
# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to show details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # prefetch related books and authors
        context['library'] = Library.objects.prefetch_related('books__author').get(pk=self.kwargs['pk'])
        return context
