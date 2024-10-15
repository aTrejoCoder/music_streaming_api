from api.models.models import Song, Artist
from api.utils.result import Result

class SongService:
    def get_song_by_id(song_id):
        try:
            song = Song.objects.get(song_id=song_id)
            return Result.success(song)
        except Song.DoesNotExist:
            return Result.error(f"song with id {song_id} not found")

    def get_songs_by_artist_id(artist_id):
        try:
            artist = Artist.objects.get(artist_id=artist_id)
            songs = Song.objects.filter(artist=artist) 
            return Result.success(songs)
        except Artist.DoesNotExist:
            return Result.error(f"artist with id {artist_id} not found")

    def create_song(data):
        try:
            artist = Artist.objects.get(artist_id=data.get('artist_id'))
            song = Song(
                title=data.get('title'),
                artist=artist,  
                album=data.get('album'),
                duration=data.get('duration'),
                audio_file=data.get('audio_file'),
                genre=data.get('genre'),  
                release_date=data.get('release_date'),
            )
            song.save()  
            return Result.success(song) 
        except Artist.DoesNotExist:
            return Result.error(f"artist with id {data.get('artist_id')} not found")

    def delete_song(song_id):
        try:
            song = Song.objects.get(song_id=song_id)
            song.delete()
            return Result.success(None)
        except Song.DoesNotExist:
            return Result.error(f"song with id {song_id} not found")
