from django.shortcuts import render
from .models import Books
from .serializers import BookSerializer
from rest_framework import viewsets, generics

class BooksViewset(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
