from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    owner = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'restaurants'

    def __str__(self):
        return self.name


class Cafe(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    owner = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'cafes'

    def __str__(self):
        return self.name
