from django.db import models

# Create your models here.
class Bank(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    owner = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'banks'

    def __str__(self):
        return self.name


class ClothingStore(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    owner = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'clothing_stores'

    def __str__(self):
        return self.name

