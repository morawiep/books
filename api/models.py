from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=128)
    authors = models.ManyToManyField(Author, related_name="authors", blank=True)
    published_date = models.CharField(max_length=4)
    categories = models.ManyToManyField(Category, related_name="category", blank=True)
    average_ratings = models.IntegerField(null=True, blank=True)
    ratings_count = models.IntegerField(null=True, blank=True)
    thumbnail = models.CharField(max_length=256, default='')

    def __str__(self):
        return self.title