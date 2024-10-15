import graphene
from api.utils.api_response import AlbumResponse
from api.services.album_service import AlbumService
from api.schema.types import AlbumType
from api.utils.result import Result

class Query(graphene.ObjectType):
    get_album_by_id = graphene.Field(AlbumResponse ,user_id=graphene.Int(required=True))
    get_albums_by_autor_id = graphene.Field(AlbumResponse, user_id=graphene.Int(required=True))
    all_albums = graphene.List(AlbumType)


    def resolve_all_albums(self, info, **kwargs):
        return Album.objects.all()


    def resolve_get_album_by_id(self, info, album_id):
        result = AlbumService.get_album_by_id(album_id)
        if result.is_failure():
            return AlbumResponse(
                success=False,
                album=None,
                message=result.get_error_msg()
            )
        
        return AlbumResponse(
                success=True,
                album=result.get_data(),
                message="album successfully fetched"
            )

    def resolve_get_albums_by_artist_id(self, info, artist_id):
        result = AlbumService.get_albums_by_artist(artist_id)
        if result.is_failure():
            return AlbumResponse(
                success=False,
                album=None,
                message=result.get_error_msg()
            )
       
        return AlbumResponse(
                success=True,
                album=result.get_data(),
                message="albums successfully fetched"
            )
        
