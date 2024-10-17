import graphene
from api.schema.mutations.user_mutations import CreateUser, UpdateUser, DeleteUser  
from api.schema.mutations.artist_mutations import CreateArtist, UpdateArtist, DeleteArtist  
from api.schema.mutations.album_mutation import CreateAlbum, UpdateAlbum, DeleteAlbum  
from api.schema.mutations.song_mutation import CreateSong, UpdateSong, DeleteSong  
from api.schema.mutations.auth_mutations import SignUpMutation, LoginMutation
from api.schema.mutations.playlist_mutation import CreatePlaylist, UpdatePlaylistName, DeletePlaylist

from api.schema.queries.user_queries import Query as UserQuery
from api.schema.queries.artist_queries import Query as ArtistQuery
from api.schema.queries.album_queries import Query as AlbumQuery
from api.schema.queries.song_queries import Query as SongQuery
from api.schema.queries.playlist_queries import Query as PlaylistQuery


from api.schema.types import PlaylistType, ListeningHistoryType


class Query(UserQuery, ArtistQuery, AlbumQuery, SongQuery, PlaylistQuery, graphene.ObjectType):
    all_playlists = graphene.List(PlaylistType)
    all_listening_histories = graphene.List(ListeningHistoryType)

    def resolve_all_playlists(self, info, **kwargs):
        return Playlist.objects.all()

    def resolve_all_listening_histories(self, info, **kwargs):
        return ListeningHistory.objects.all()


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()

    create_artist = CreateArtist.Field()
    update_artist = UpdateArtist.Field()
    delete_artist = DeleteArtist.Field()

    create_album = CreateAlbum.Field()
    update_album = UpdateAlbum.Field()
    delete_album = DeleteAlbum.Field()

    create_song = CreateSong.Field()
    update_song = UpdateSong.Field()
    delete_song = DeleteSong.Field()

    create_playlist = CreatePlaylist.Field()
    update_playlist_name = UpdatePlaylistName.Field()
    delete_playlist = DeletePlaylist.Field()

    singup = SignUpMutation.Field()
    login = LoginMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
