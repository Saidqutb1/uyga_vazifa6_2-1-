from django.db import models

# Create your models here.
class Birds(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    mass = models.IntegerField()
    size = models.IntegerField()

    class Meta:
        db_table= 'birds'

    def __str__(self):
        return self.name


class Fishes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    mass = models.IntegerField()
    size = models.IntegerField()
    body = models.TextField()

    class Meta:
        db_table = 'fishes'

    def __str__(self):
        return self.name