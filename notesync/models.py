from django.db import models

# Create your models here.


class Band(models.Model):
    name = models.CharField(max_length=150)
    genre = models.CharField(max_length=50)


class Song(models.Model):
    title = models.CharField(max_length=150)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
