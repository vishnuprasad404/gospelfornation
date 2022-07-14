from turtle import title
from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=255)
    venue = models.CharField(max_length=255)
    time_from = models.CharField(max_length=255)
    time_to = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    image = models.ImageField(upload_to="event", null=False)
    def __str__(self) -> str:
        return self.title

class Photo(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="photos", null=False)
    def __str__(self) -> str:
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    image = models.ImageField(upload_to="thumbnail", null=False)
    def __str__(self) -> str:
        return self.title