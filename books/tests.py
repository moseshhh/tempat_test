from django.test import TestCase
from .models import Books

class BaseViewTest(TestCase):
    def setUp(self):
        # add test data
         Books.objects.create(title= "Harry Potter", author= "JK Rownling")
         Books.objects.create(title="Kafka on the Shore",author="Haruki Murakami")
         Books.objects.create(title="let it be", author="Kazuo Iziguro")
    
    
