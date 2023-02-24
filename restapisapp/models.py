from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Book(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)
    pages = models.IntegerField()

    def __str__(self):
        return self.name


class Playlistsong(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    artist = models.CharField(max_length=100, null=True, blank=True)
    album = models.CharField(max_length=100, null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Playlist(models.Model):
    playlist_name = models.CharField(max_length=100, null=True, blank=True)
    songname = models.CharField(max_length=100, null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.playlist_name
