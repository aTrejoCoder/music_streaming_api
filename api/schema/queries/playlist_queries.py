import graphene
from api.services.playlist_service import PlaylistService
from api.utils.result import Result
from api.utils.api_response import PlaylistResponse

class Query:
    playlist_id = graphene.Field(PlaylistResponse, playlist_id=graphene.Int(required=True))

    def resolve_get_playlist_by_id(self, info, playlist_id):
        result = PlaylistService.get_playlist_by_id(playlist_id);
        if result.is_failure():
            return PlaylistResponse(
                success = False,
                playlist = None,
                message = result.get_error_msg(),
            )
        
        return PlaylistResponse(
                success = True,
                playlist = result.get_data(),
                message = "playlist succesfully fetched"
            )

    def resolve_get_playlists_by_user_id(self, info, user_id):
        esult = PlaylistService.get_playlist_by_user_id(user_id);
        if result.is_failure():
            return PlaylistResponse(
                success = False,
                playlist = None,
                message = result.get_error_msg(),
            )
        
        return PlaylistResponse(
                success = True,
                playlist = result.get_data(),
                message = "playlists succesfully fetched"
            ) 