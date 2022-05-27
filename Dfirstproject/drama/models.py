from django.db import models

# Create your models here.

class Romance(models.Model):
    title = models.CharField('Title',max_length=50, blank=True)
    author = models.CharField('Author',max_length=50, blank=True)
    upload_time = models.DateTimeField(unique=True)
    content=models.TextField('content')

    def __str__(self):
        return self.title

class Mystery(models.Model):
    title = models.CharField('Title',max_length=50, blank=True)
    author = models.CharField('Author',max_length=50, blank=True)
    upload_time = models.DateTimeField(unique=True)
    content=models.TextField('content')

    def __str__(self):
        return self.title

class Disaster(models.Model):
    title = models.CharField('Title',max_length=50, blank=True)
    author = models.CharField('Author',max_length=50, blank=True)
    upload_time = models.DateTimeField(unique=True)
    content=models.TextField('content')

    def __str__(self):
        return self.title