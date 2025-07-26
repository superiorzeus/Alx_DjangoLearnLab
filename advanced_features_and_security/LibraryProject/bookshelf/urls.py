from django.urls import path
from . import views

app_name = 'bookshelf' # Important for namespacing URLs

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('books/create/', views.book_create, name='book_create'),
    path('books/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),
    path('books/<int:pk>/view/', views.book_detail, name='book_detail'),
]