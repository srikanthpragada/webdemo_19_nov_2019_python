from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=30, null=False)
    author = models.CharField(max_length=50, null=False)
    publisher = models.CharField(max_length=20, null=True, blank=True)
    price = models.FloatField()

    def __str__(self):
        return f"{self.title} - {self.price}"


