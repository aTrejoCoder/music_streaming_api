import graphene
from api.schema.types import UserType, ArtistType, AlbumType, SongType

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