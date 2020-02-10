from django.urls import path
from .views import BooksViewset

urlpatterns = [
    path('', BooksViewset)
]