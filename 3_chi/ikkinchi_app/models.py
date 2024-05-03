from django.db import models

# Create your models here.


class School(models.Model):
    school_number = models.IntegerField(default=1)
    status = models.CharField(max_length=255, blank=True, null=True)
    student = models.IntegerField(default=0)

    class Meta:
        db_table = 'school'

    def __str__(self):
        return self.school_number


class University(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    courses = models.CharField(max_length=255, blank=True, null=True)
    student = models.IntegerField(default=0)

    class Meta:
        db_table = 'university'

    def __str__(self):
        return self.name
