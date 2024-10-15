import graphene
from api.schema.types import SongType
from api.models.models import Song
from api.utils.api_response import SongResponse
from api.services.song_services import SongService
from api.utils.result import Result

class Query(graphene.ObjectType):
    all_songs = graphene.List(SongType)
    get_song_by_id = graphene.Field(SongType, song_id=graphene.Int(required=True))
    get_song_by_autor_id = graphene.Field(SongType, autor_id=graphene.Int(required=True))


    def resolve_all_songs(self, info, **kwargs):
        return Song.objects.all()

    def resolve_get_song_by_id(self, info, song_id):
        result = SongService.get_song_by_id(song_id)
        if result.is_failure():
            return SongResponse(
                success=False,
                song=None,
                message=result.get_error_msg()
            )
        
        return SongResponse(
            success=True,
            song=result.get_data(),
            message="Song successfully fetched"
        )

    def resolve_get_songs_by_artist_id(self, info, artist_id):
        result = SongService.get_songs_by_artist_id(artist_id)
        if result.is_failure():
            return SongResponse(
                success=False,
                song=None,
                message=result.get_error_msg()
            )
        
        return SongResponse(
            success=True,
            song=result.get_data(),
            message="Songs successfully fetched"
        )
