from django.db import models

# Create your models here.

class Author(models.Model):
    firstName=models.CharField(max_length=25)
    lastName=models.CharField(max_length=25)
    age=models.IntegerField()

    def __str__(self):
        return self.firstName

class Book(models.Model):
    bookName=models.CharField(max_length=25)
    authors=models.ManyToManyField(Author)

