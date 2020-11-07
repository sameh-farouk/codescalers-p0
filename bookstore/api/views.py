from django.shortcuts import render

# Create your views here.
from . models import Book
from .serializers import BookSerializer
from rest_framework import viewsets, mixins
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author_first_name', 'author_last_name']
    search_fields = ['title', '=isbn']
    ordering_fields = ['isbn', 'title', 'author_first_name', 'author_last_name']
    ordering = ['id']
    