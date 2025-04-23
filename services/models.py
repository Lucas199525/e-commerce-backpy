from django.db import models

# Create your models here.
class Services(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    details = models.TextField()
    region = models.TextField()
    category = models.TextField()
    notice = models.TextField()
