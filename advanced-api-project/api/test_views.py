from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITests(APITestCase):
    """
    Test suite for the Book API endpoints.
    """

    def setUp(self):
        """
        Set up initial data for all tests. This includes a user,
        an authenticated client, and several Author and Book objects.
        """
        # Create a user for authenticated requests
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Create two authors
        self.author1 = Author.objects.create(name='Frank Herbert')
        self.author2 = Author.objects.create(name='J.R.R. Tolkien')

        # Create some books
        self.book1 = Book.objects.create(
            title='Dune',
            author=self.author1,
            publication_year=1965
        )
        self.book2 = Book.objects.create(
            title='The Hobbit',
            author=self.author2,
            publication_year=1937
        )
        self.book3 = Book.objects.create(
            title='The Lord of the Rings',
            author=self.author2,
            publication_year=1954
        )

        # Define the URLs for the endpoints
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book1.pk})

    # --- CRUD Tests for Authenticated Users ---

    def test_book_list_authenticated(self):
        """
        Ensure the book list is accessible by an authenticated user.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_book_create_authenticated(self):
        """
        Ensure an authenticated user can create a new book.
        """
        data = {
            'title': 'The Hitchhiker\'s Guide to the Galaxy',
            'author': self.author1.pk,
            'publication_year': 1979
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)
        self.assertEqual(response.data['title'], data['title'])

    def test_book_detail_authenticated(self):
        """
        Ensure an authenticated user can retrieve a book's details.
        """
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Dune')

    # --- Permission Tests for Unauthenticated Users ---

    def test_book_create_unauthenticated_denied(self):
        """
        Ensure an unauthenticated user cannot create a book,
        expecting a 403 Forbidden response.
        """
        self.client.logout()  # Logout the authenticated client
        data = {
            'title': 'The Silmarillion',
            'author': self.author2.pk,
            'publication_year': 1977
        }
        response = self.client.post(self.create_url, data, format='json')
        # Expecting 403 because an unauthenticated user lacks permission
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Book.objects.count(), 3)

    # --- Query Capability Tests ---

    def test_book_filter_by_title(self):
        """
        Ensure filtering by title works correctly.
        """
        response = self.client.get(self.list_url, {'title': 'Dune'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Dune')

    def test_book_filter_by_author(self):
        """
        Ensure filtering by author works correctly.
        """
        response = self.client.get(self.list_url, {'author': self.author2.pk})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        # Check if the titles are correct
        titles = {item['title'] for item in response.data}
        self.assertIn('The Hobbit', titles)
        self.assertIn('The Lord of the Rings', titles)

    def test_book_search(self):
        """
        Ensure searching by partial match works correctly.
        """
        response = self.client.get(self.list_url, {'search': 'Ring'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'The Lord of the Rings')

    def test_book_ordering_by_title_ascending(self):
        """
        Ensure ordering by title in ascending order works correctly.
        """
        response = self.client.get(self.list_url, {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check the order of titles
        titles = [item['title'] for item in response.data]
        self.assertEqual(titles, ['Dune', 'The Hobbit', 'The Lord of the Rings'])

    def test_book_ordering_by_publication_year_descending(self):
        """
        Ensure ordering by publication year in descending order works correctly.
        """
        response = self.client.get(self.list_url, {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check the order of titles based on publication year
        titles = [item['title'] for item in response.data]
        self.assertEqual(titles, ['Dune', 'The Lord of the Rings', 'The Hobbit'])