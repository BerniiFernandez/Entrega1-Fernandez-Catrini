from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Netflix(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images')
    date = models.DateField()
    author = models.CharField(max_length=50)
    qualification = models.DecimalField(max_digits=2, decimal_places=1)
    body = RichTextField()

    def __str__(self):
        return self.title

class Prime(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images')
    date = models.DateField()
    author = models.CharField(max_length=50)
    qualification = models.DecimalField(max_digits=2, decimal_places=1)
    body = RichTextField()

    def __str__(self):
        return self.title
    
class HBO(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images')
    date = models.DateField()
    author = models.CharField(max_length=50)
    qualification = models.DecimalField(max_digits=2, decimal_places=1)
    body = RichTextField()

    def __str__(self):
        return self.title

class Disney(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images')
    date = models.DateField()
    author = models.CharField(max_length=50)
    qualification = models.DecimalField(max_digits=2, decimal_places=1)
    body = RichTextField()

    def __str__(self):
        return self.title
