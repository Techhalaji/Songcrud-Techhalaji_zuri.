from django.db import models

class Artiste(models.Model):
    First_name = models.Charfield(max lenght = 50) 
    Last_name = models.Integer(max lenght =  10) 
    Age = models.Integer()

class Song(models.Model):
    Title = models.Charfield(max lenght = 50)
    Date_released = models.Integer(max lenght =  10)
    Artiste_id = models.Integer()
    Likes = models.Integer()

class Lyric(model.Models):
    Content = models.Charfield(max lenght = 5000)
    Likes = models.Integer()
    Song_id = models.Integer()

# Create your models here.
