from django.db import models

# Create your models here.


class Band(models.Model):
    """
    Model representing a band of music:

    Attributes:
        name (str): The name of the band.
        genre (str): The type of music the band plays.
    """
    name = models.CharField(max_length=150)
    genre = models.CharField(max_length=50)


class Song(models.Model):
    """
    Model representing a class.

    Attributes:
        title (str): The name of the song.
        band (Band): The band that performed the song.
                     Linked as a foreign key.
    """
    title = models.CharField(max_length=150)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
