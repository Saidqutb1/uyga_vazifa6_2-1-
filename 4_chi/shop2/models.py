from django.db import models

# Create your models here.
class Phone(models.Model):
    brand = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    price = models.IntegerField(default=0)
    color = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'phones'

    def __str__(self):
        return self.model


class Book(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    release_year = models.DateField(blank=True, null=True)
    price = models.IntegerField(default=0)
    genre = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'books'

    def __str__(self):
        return self.title