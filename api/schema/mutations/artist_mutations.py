import graphene
from api.services.artist_service import ArtistService
from api.utils.api_response import ArtistResponse
from api.utils.result import Result

class CreateArtist(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        bio = graphene.String(required=True)
        image = graphene.String(required=True)

    response = graphene.Field(ArtistResponse)

    def mutate(self, info, name, bio, image):
        artist_data = {
            'name': name,
            'bio': bio,
            'image': image,
        }

        artist = ArtistService.create_artist(artist_data)
        return CreateArtist(
            response=ArtistResponse(
                success=True,
                artist=artist,
                message="Artist successfully created"
            )
        )

class UpdateArtist(graphene.Mutation):
    class Arguments:
        artist_id = graphene.Int(required=True)
        name = graphene.String()
        bio = graphene.String()
        image = graphene.String()

    response = graphene.Field(ArtistResponse)

    def mutate(self, info, artist_id, name=None, bio=None, image=None):
        artist_data = {
            'artist_id': artist_id,
            'name': name,
            'bio': bio,
            'image': image,
        }

        update_result = ArtistService.update_artist(artist_data)
        if update_result.is_failure():
            return UpdateArtist(
                response=ArtistResponse(
                    success=False,
                    artist=None,
                    message=update_result.get_error_msg()
                )
            )
        
        return UpdateArtist(
            response=ArtistResponse(
                success=True,
                artist=update_result.get_data(),
                message="Artist successfully updated"
            )
        )


class DeleteArtist(graphene.Mutation):
    class Arguments:
        artist_id = graphene.Int(required=True)

    response = graphene.Field(ArtistResponse)

    def mutate(self, info, artist_id):
        delete_result = ArtistService.delete_artist(artist_id)
        if delete_result.is_failure():
            return DeleteArtist(
                response=ArtistResponse(
                    success=False,
                    artist=None,
                    message=delete_result.get_error_msg()
                )
            )
            
        return DeleteArtist(
            response=ArtistResponse(
                success=True,
                artist=None,
                message="Artist successfully deleted"
            )
        )
