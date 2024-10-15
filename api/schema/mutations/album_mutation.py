import graphene
from api.services.album_service import AlbumService
from api.utils.api_response import AlbumResponse

class CreateAlbum(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        artist_id = graphene.Int(required=True)
        release_date = graphene.DateTime(required=True)
        image = graphene.String(required=True)
    
    response = graphene.Field(AlbumResponse)

    def mutate(self, info, title, artist_id, release_date, image):
        album_data = {
            'title': title,
            'artist_id': artist_id,
            'release_date': release_date,
            'cover_image': image
        }
    
        create_result = AlbumService.create_album(album_data)
        if create_result.is_failure():
            return CreateAlbum(
            response=AlbumResponse(
                success=False,
                album=None,
                message=create_result.get_error_msg(),
            )
        )

        return CreateAlbum(
            response=AlbumResponse(
                success=True,
                album=album,
                message='album succesfully created'
            )
        )

class UpdateAlbum(graphene.Mutation):
    class Arguments:
        album_id = graphene.Int(required=True)
        title = graphene.String()
        artist = graphene.String()
        release_date = graphene.DateTime()
        image = graphene.String()

    response = graphene.Field(AlbumResponse)

    def mutate(self, info, album_id, title=None, artist=None, release_date=None, image=None):
        album_data = {
            'album_id': album_id,
            'title': title,
            'artist': artist,
            'release_date': release_date,
            'image': image
        }

        update_result = AlbumService.update_album(album_data)
        if update_result.is_failure():
            return UpdateAlbum(
                response=AlbumResponse(
                    success=False,
                    album=None,
                    message=update_result.get_error_msg()
                )
            )
        
        return UpdateAlbum(
            response=AlbumResponse(
                success=True,
                album=update_result.get_data(),
                message="Album successfully updated"
            )
        )

class DeleteAlbum(graphene.Mutation):
    album_id = graphene.Int(required=True)

    response = graphene.Field(AlbumResponse)

    def mutate(self, info, album_id):
        deleteResult = AlbumService.delete_album(album_id)
        if deleteResult.is_failure():
            return DeleteAlbum(
                response=AlbumResponse(
                    success=False,
                    artist=None,
                    message=update_result.get_error_msg()
            ))
            
        return DeleteAlbum(
            response=AlbumResponse(
                success=True,
                artist=None,
                message="album succesfully deleted"
            ))    

        


