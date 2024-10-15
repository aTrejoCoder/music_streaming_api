from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password, check_password


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255, unique=True) 
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username 
    

class Artist(models.Model):
    artist_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    bio =  models.TextField(blank=True)
    image = models.ImageField(upload_to='artist_images/', blank=True, null=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    album_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, related_name='albums', on_delete=models.CASCADE)
    release_date = models.DateField();
    cover_image = models.ImageField(upload_to='album_covers/', blank=True, null=True)

    def __str__(self):
        return self.title


class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, related_name='songs', on_delete=models.CASCADE)
    album = models.ForeignKey(Album, related_name='albums', on_delete=models.CASCADE)
    duration = models.DurationField()
    audio_file =  models.FileField(upload_to='songs/')
    genre = models.CharField(max_length=100, blank=True)
    release_date = models.DateField()


class Playlist(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='playlists', on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song, related_name='playlists', blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True) 


class ListeningHistory(models.Model):
    user = models.ForeignKey(User, related_name='listening_history', on_delete=models.CASCADE)
    song = models.ForeignKey(Song, related_name='listening_history', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'song')
