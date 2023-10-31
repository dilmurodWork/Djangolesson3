# 6 create model after then make migrations and migrate, create superuser
from django.db import models


class BookModel(models.Model):
    name = models.CharField(max_length=255, verbose_name="Books name")
    author = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
