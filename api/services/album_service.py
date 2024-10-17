from api.models import Album, Artist
from api.utils.result import Result

class AlbumService:
    def get_album_by_id(album_id):
        try:
            album = Album.objects.get(album_id=album_id)
            return Result.success(album)
        except Album.DoesNotExist:
            return Result.error(f"Album with id {album_id} not found")

    def get_albums_by_artist(artist_id):
        try:
            artist = Artist.objects.get(artist_id=artist_id)
            albums = Album.objects.filter(artist=artist)
            return Result.success(albums)
        except Artist.DoesNotExist:
            return Result.error(f"Artist with id {artist_id} not found")

    def create_album(data):
        try:
            artist = Artist.objects.get(artist_id=data.get('artist_id'))
            album = Album(
                title=data.get('title'), 
                artist=artist,
                release_date=data.get('release_date'),
                cover_image=data.get('cover_image')
            )
            album.save()
            return Result.success(album)
        except Artist.DoesNotExist:
            return Result.error(f"Artist with id {data.get('artist_id')} not found")

    def update_album(data):
        try:
            album = Album.objects.get(album_id=data.get('album_id'))
            if data.get('artist_id'):
                artist = Artist.objects.get(artist_id=data.get('artist_id'))
                album.artist = artist

            if data.get('title'):
                album.title = data.get('title')
            if data.get('release_date'):
                album.release_date = data.get('release_date')
            if data.get('cover_image'):
                album.cover_image = data.get('cover_image')

            album.save() 
            return Result.success(album)  
        except Album.DoesNotExist:
            return Result.error(f"Album with id {data.get('album_id')} not found")
        except Artist.DoesNotExist:
            return Result.error(f"Artist with id {data.get('artist_id')} not found")

    def delete_album(album_id):
        try:
            album = Album.objects.get(album_id=album_id)
            album.delete()
            return Result.success(None)
        except Album.DoesNotExist:
            return Result.error(f"Album with id {album_id} not found")
