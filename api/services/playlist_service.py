from api.models import Playlist
from api.utils.result import Result

class PlaylistService:
    def get_playlist_by_id(playlist_id):
        try: 
            playlist = Playlist.objects.get(playlist_id=playlist_id)
            return Result.success(playlist)
        except Playlist.DoesNotExist:
            return Result.error(f"Playlist with id {playlist_id} not found")

    def get_playlist_by_user_id(user_id):
        playlists = Playlist.objects.filter(user_id=user_id)
        if playlists.exists():
            return Result.success(playlists)
        return Result.error(f"No playlists found for user with id {user_id}")

    def create_playlist(data):
        playlist = Playlist(
            name = data.get('name'),
            user = data.get('user'),
        )

        playlist.save()

        songs = data.get('songs')
        if songs: 
            playlist.songs.set(songs)

        return playlist

    def update_playlist_name(update_data):
        try: 
            playlist_id = update_data.get('playlist_id')
            user_id = update_data.get('user_id')

            playlist = Playlist.objects.get(playlist_id=playlist_id, user_id=user_id)

            playlist.name = update_data.get('name')

            playlist.save()

            return Result.success(playlist)
        except Playlist.DoesNotExist:
            return Result.error(f"Playlist with id {playlist_id} for user {user_id} not found")

    def delete_playlist(playlist_id, user_id):
        try: 
            playlist = Playlist.objects.get(playlist_id=playlist_id, user_id=user_id)
            playlist.delete()

            return Result.success(None)
        except Playlist.DoesNotExist:
            return Result.error(f"Playlist with id {playlist_id} for user {user_id} not found")

    def add_songs_to_playlist(playlist_id, songs):
        try: 
            playlist = Playlist.objects.get(playlist_id=playlist_id)
            playlist.songs.add(*songs)

            return Result.success("Songs added to playlist successfully")
        except Playlist.DoesNotExist:
            return Result.error(f"Playlist with id {playlist_id} not found")
        except Exception as e:
            return Result.error(f"An error occurred: {str(e)}")

    def remove_songs_from_playlist(playlist_id, songs):
        try: 
            playlist = Playlist.objects.get(playlist_id=playlist_id)
            playlist.songs.remove(*songs)
            
            return Result.success("Songs removed from playlist successfully")
        except Playlist.DoesNotExist:
            return Result.error(f"Playlist with id {playlist_id} not found")
        except Exception as e:
            return Result.error(f"An error occurred: {str(e)}")
