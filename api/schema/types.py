from graphene_django.types import DjangoObjectType
from api.models.models import User, Artist, Album, Song, Playlist, ListeningHistory


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("user_id", "email", "username", "first_name", "last_name", "created_at", "updated_at")


class ArtistType(DjangoObjectType):
    class Meta:
        model = Artist
        fields = ("artist_id", "name", "bio", "image")


class SongType(DjangoObjectType):
    class Meta:
        model = Song
        fields = ("song_id", "title", "artist", "album", "duration", "audio_file", "genre", "release_date")


class AlbumType(DjangoObjectType):
    class Meta:
        model = Album
        fields = ("album_id", "title", "artist", "album", "duration", "audio_file", "genre", "release_date")


class PlaylistType(DjangoObjectType):
    class Meta:
        model = Playlist    
        fields = ("playlist_id", "name", "user", "songs", "created_at", "updated_at")


class ListeningHistoryType(DjangoObjectType):
    class Meta:
        model = ListeningHistory
        fields = ("listeninghistory_id", "user", "songs", "created_at", "updated_at")