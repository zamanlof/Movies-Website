from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.CharField(
        max_length=100, default='default.jpg')  # Image filename

    def __str__(self):
        return self.title
