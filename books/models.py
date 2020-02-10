from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    review = models.TextField()
    rating = models.IntegerField()
    isborrowed = models.BooleanField()
