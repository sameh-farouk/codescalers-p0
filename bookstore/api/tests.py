from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
from .models import Book

#isbn,title,author_last_name,author_first_name,page_count,description
class BookTests(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            isbn='96752126-9',
            title='Harry Potter',
            author_last_name='Rowling',
            author_first_name='JK',
            page_count=290,
            description='the book description'
        )

    def test_book_listing(self):
        url = reverse('book-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Harry Potter')

    def test_book_detail_view_for_non_exists_book(self):
        no_response = self.client.get('api/books/1234567890/', format='json')
        self.assertEqual(no_response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_create_book(self):
        """
        Ensure we can create a new book object via post.
        """
        url = reverse('book-list')
        data = {'isbn':'96712116-1',
            'title':'New Star',
            'author_last_name':'Khaled',
            'author_first_name':'Roshdy',
            'page_count':250,
            'description':'the book description'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        
    def test_partly_update_book(self):
        """
        Ensure we can partly update a book object via patch.
        """
        data = {'isbn':'96712116-2'}
        response = self.client.patch(self.book.get_absolute_url(), data, format='json', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get(self.book.get_absolute_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, '96712116-2')

    def test_delete_book(self):
        """
        Ensure we can delete a book object via delete.
        """
        response = self.client.delete(self.book.get_absolute_url())        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
    