from django.db import models

# Create your models here.
class Smartphone(models.Model):
    brand = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    price = models.IntegerField(default=0)
    color = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'smartphones'

    def __str__(self):
        return self.model


class Laptop(models.Model):
    brand = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    price = models.IntegerField(default=0)
    color = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'laptops'

    def __str__(self):
        return self.model
