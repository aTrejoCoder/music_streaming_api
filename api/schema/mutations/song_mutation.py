import graphene
from api.schema.types import SongType
from api.utils.api_response import SongResponse
from api.services.song_services import SongService

class CreateSong(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        artist_id = graphene.Int(required=True)
        album_id = graphene.Int(required=True)
        duration = graphene.String(required=True)
        audio_file = graphene.String(required=True)
        genre = graphene.String()
        release_date = graphene.Date()

    response = graphene.Field(SongResponse)

    def mutate(self, info, title, artist_id, album_id, duration, audio_file, genre=None, release_date=None):
        song_data = {
            'title': title,
            'artist_id': artist_id,
            'album_id': album_id,
            'duration': duration,
            'audio_file': audio_file,
            'genre': genre,
            'release_date': release_date
        }

        result = SongService.create_song(song_data)

        if result.is_failure():
            return CreateSong(
                response=SongResponse(
                    success=False,
                    song=None,
                    message=result.get_error_msg()
                )
            )

        return CreateSong(
            response=SongResponse(
                success=True,
                song=result.get_data(),
                message="Song created successfully"
            )
        )


class UpdateSong(graphene.Mutation):
    class Arguments:
        song_id = graphene.Int(required=True)
        title = graphene.String()
        artist_id = graphene.Int()
        album_id = graphene.Int()
        duration = graphene.String()
        audio_file = graphene.String()
        genre = graphene.String()
        release_date = graphene.Date()

    response = graphene.Field(SongResponse)

    def mutate(self, info, song_id, title=None, artist_id=None, album_id=None, duration=None, audio_file=None, genre=None, release_date=None):
        song_data = {
            'song_id': song_id,
            'title': title,
            'artist_id': artist_id,
            'album_id': album_id,
            'duration': duration,
            'audio_file': audio_file,
            'genre': genre,
            'release_date': release_date
        }

        result = SongService.update_song(song_data)

        if result.is_failure():
            return UpdateSong(
                response=SongResponse(
                    success=False,
                    song=None,
                    message=result.get_error_msg()
                )
            )

        return UpdateSong(
            response=SongResponse(
                success=True,
                song=result.get_data(),
                message="Song updated successfully"
            )
        )


class DeleteSong(graphene.Mutation):
    class Arguments:
        song_id = graphene.Int(required=True)

    response = graphene.Field(SongResponse)

    def mutate(self, info, song_id):
        result = SongService.delete_song(song_id)

        if result.is_failure():
            return DeleteSong(
                response=SongResponse(
                    success=False,
                    song=None,
                    message=result.get_error_msg()
                )
            )

        return DeleteSong(
            response=SongResponse(
                success=True,
                song=None,
                message="Song deleted successfully"
            )
        )