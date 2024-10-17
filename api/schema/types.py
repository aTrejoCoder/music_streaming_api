import graphene
from graphene_django.types import DjangoObjectType
from api.models import Artist, Album, Song, Playlist, ListeningHistory
from django.contrib.auth import get_user_model

User = get_user_model()

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


class AuthPayload(graphene.ObjectType):
    user = graphene.Field(UserType)
    jwt_token = graphene.String()
    oauth2_token = graphene.String()