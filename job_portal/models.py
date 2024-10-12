from django.db import models


# Create your models here.
class Job(models.Model):
    # id starts at 1 and autoincrements
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    salary = models.IntegerField()
    is_active = models.BooleanField(default=False)
