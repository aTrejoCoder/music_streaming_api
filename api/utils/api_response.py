import graphene
from api.schema.types import UserType, ArtistType, AlbumType, SongType, PlaylistType

class UserResponse(graphene.ObjectType):
    success = graphene.Boolean()
    user = graphene.Field(UserType) 
    message = graphene.String()

class ArtistResponse(graphene.ObjectType):
    success = graphene.Boolean()
    artist = graphene.Field(ArtistType) 
    message = graphene.String()

class AlbumResponse(graphene.ObjectType):
    success = graphene.Boolean()
    album = graphene.Field(AlbumType) 
    message = graphene.String()

class SongResponse(graphene.ObjectType):
    success = graphene.Boolean()
    song = graphene.Field(SongType) 
    message = graphene.String()

class PlaylistResponse(graphene.ObjectType):
    success = graphene.Boolean()
    playlist = graphene.Field(PlaylistType) 
    message = graphene.String()

class AuthResponse(graphene.ObjectType):
    success = graphene.Boolean()
    jwt_token = graphene.String() 
    oauth2_token = graphene.String()
    user = graphene.Field(UserType)
    message = graphene.String()