from database import Base
from models.album_model import Album
from models.artist_model import Artist
from models.genre_model import Genre
from models.playlist_model import Playlist
from models.song_model import Song
from models.user_model import User
from models.artisttosong import ArtistToSong
from models.songtoplaylist import SongToPlaylist

Base = declarative_base()