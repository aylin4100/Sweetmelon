from django.db import models

# Create your models here.

class first(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    publishingdate=models.DateTimeField()