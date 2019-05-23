# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Album(models.Model):
    artist=models.CharField( max_length=150)
    tittle=models.CharField( max_length=50)
    genre=models.CharField( max_length=50)

    def __str__(self):
            return self.artist + ' - ' + self.tittle + ' - ' + self.genre
        

class Song(models.Model):
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    file_type=models.CharField( max_length=50)
    song_tittle=models.CharField(max_length=50)
    def __str__(self):
        return self.file_type + ' -' +self.song_tittle 
