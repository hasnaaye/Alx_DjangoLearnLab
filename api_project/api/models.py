from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.TextField()

    def __str__(self):
        return self.title
