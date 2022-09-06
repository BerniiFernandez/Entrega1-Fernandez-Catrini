from distutils.command.upload import upload
from django.db import models

# Create your models here.

class HBO(models.Model):
    photo = models.ImageField(upload_to='images')
    qualification = models.IntegerField()
    title = models.CharField(max_length=300)

class Disney(models.Model):
    photo = models.ImageField(upload_to='images')
    qualification = models.IntegerField()
    title = models.CharField(max_length=300)