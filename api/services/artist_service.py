from api.models.models import Artist
from api.utils.result import Result

class ArtistService:
    def get_artist_by_id(artist_id):
        try:
            artist = Artist.objects.get(artist_id=artist_id)

            return Result.success(artist)
        except Artist.DoesNotExist:
            return Result.error(f"artist with id {artist_id} not found")

    def create_artist(data):
        artist = Artist(
            name=data.get('name'),
            bio=data.get('bio'),
            image=data.get('image')
        )

        artist.save()

        return artist


    def update_artist(data):
        try:
            artist = Artist.objects.get(artist_id=data.get('artist_id'))
            
            if data.get('name'):
                artist.name = data.get('name')
            if data.get('bio'):
                artist.bio = data.get('bio')
            if data.get('image'):
                artist.image = data.get('image')
            
            artist.save()

            return Result.success(artist)
        except Artist.DoesNotExist:
            return Result.error(f"artist with id {artist_id} not found")


    def delete_artist(artist_id):
        try:
            artist = Artist.objects.get(artist_id=artist_id)
            
            artist.delete()

            return Result.success(None)
        except Artist.DoesNotExist:
            return Result.error(f"artist with id {artist_id} not found")    
