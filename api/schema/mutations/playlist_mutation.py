import graphene
from api.services.playlist_service import PlaylistService
from api.services.user_services import UserService
from api.services.song_services import SongService
from api.utils.result import Result
from api.utils.api_response import PlaylistResponse

class CreatePlaylist(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        user_id = graphene.Int(required=True)
        song_id_list = graphene.List(graphene.Int, required=True)

    response = graphene.Field(PlaylistResponse)

    def mutate(self, info, name, user_id, song_id_list):
        user_result = UserService.get_user_by_id(user_id)
        if user_result.is_failure():
            return CreatePlaylist(
                response=PlaylistResponse(
                    success = False,
                    playlist = None,
                    message = user_result.get_error_msg(),
                )
            ) 

        songs_result = SongService.get_songs_by_id_list(song_id_list)
        if songs_result.is_failure():
            return CreatePlaylist(
                response=PlaylistResponse(
                    success = False,
                    playlist = None,
                    message = songs_result.get_error_msg(),
                )
            ) 

        data = {
            'name' : name,
            'user' : user_result.get_data(),
            'songs' : songs_result.get_data(),
        }

        playlist = PlaylistService.create_playlist(data)

        return CreatePlaylist(
            response=PlaylistResponse(
                success = True,
                playlist = playlist,
                message = f"Playlist succesfully create to user with id {user_id}",
            )
        )


class UpdatePlaylistName(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        playlist_id = graphene.Int(required=True)
        user_id = graphene.Int(required=True)

    response = graphene.Field(PlaylistResponse)

    def mutate(self, info, name, playlist_id, user_id):
        playlist_update_data = {
            'name' : name,
            'playlist_id' : playlist_id,
            'user_id' : user_id,
        }

        update_result = PlaylistService.update_playlist_name(playlist_update_data)
        if update_result.is_failure():
            return UpdatePlaylistName(
                response=PlaylistResponse(
                    success = False,
                    playlist = None,
                    message = update_result.get_error_msg(),
                )
            ) 

        return UpdatePlaylistName(
            response=PlaylistResponse(
                success = True,
                playlist = update_result.get_data(),
                message = f"Playlist succesfully updated",
            )
        )


class DeletePlaylist(graphene.Mutation):
    class Arguments:
        playlist_id = graphene.Int(required=True)
        user_id = graphene.Int(required=True)
        
    response = graphene.Field(PlaylistResponse)

    def mutate(self, info, playlist_id, user_id):
        delete_result = PlaylistService.delete_playlist(playlist_id, user_id)
        if delete_result.is_failure():
            return DeletePlaylist(
                response=PlaylistResponse(
                    success = False,
                    playlist = None,
                    message = delete_result.get_error_msg(),
                )
            ) 

        return DeletePlaylist(
            response=PlaylistResponse(
                success = True,
                playlist = None,
                message = "Playlist succesfully deleted",
            )
        )
