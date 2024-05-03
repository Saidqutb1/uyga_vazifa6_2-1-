from django.db import models

# Create your models here.
class Trees(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    max_grown = models.IntegerField()
    place_grown = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'trees'

    def __str__(self):
        return self.name


class Flowers(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    max_grown = models.IntegerField()
    body = models.TextField()

    class Meta:
        db_table = 'flowers'

    def __str__(self):
        return self.name