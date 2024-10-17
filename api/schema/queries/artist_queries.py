import graphene
from api.services.artist_service import ArtistService
from api.utils.result import Result
from api.schema.types import ArtistType
from api.models import Artist
from api.utils.api_response import ArtistResponse

class Query(graphene.ObjectType):
    get_artist_by_id = graphene.Field(ArtistResponse, artist_id=graphene.Int(required=True)) 
    all_artists = graphene.List(ArtistType)

    def resolve_all_artists(self, info, **kwargs):
        return Artist.objects.all()

    def resolve_get_artist_by_id(self, info, artist_id):
        result = ArtistService.get_artist_by_id(artist_id=artist_id)
        if result.is_failure():
            return ArtistResponse(
                success=False,
                artist=None,
                message=result.get_error_msg()
            )

        return ArtistResponse(
                success=True,
                artist=result.get_data(),
                message="artist data successfully fetched"
        )

        
    
