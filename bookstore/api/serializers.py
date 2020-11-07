from rest_framework import serializers 
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    # isbn,title,author_last_name,author_first_name,page_count,description
    class Meta:
        model = Book
        fields = ('id',
                  'isbn',
                  'title',
                  'author_last_name',
                  'author_first_name',
                  'page_count',
                  'description')

