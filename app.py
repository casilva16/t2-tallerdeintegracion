from flask_sqlalchemy import SQLAlchemy
from flask import Flask,  request, jsonify
from flask_marshmallow import Marshmallow
from base64 import b64encode
# from models import Artist, Album, Track
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)


##### Modelos/Clases #####
class Artist(db.Model):
    name = db.Column(db.String(100), unique=True)
    age = db.Column(db.Integer)
    id = db.Column(db.String, primary_key=True)
    albums = db.Column(db.String)
    tracks = db.Column(db.String)
    artist_url = db.Column(db.String)

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.id = b64encode(self.name.encode()).decode('utf-8')
        self.albums = 'http://localhost:5000/artists/'+self.id+'/albums'
        self.tracks = 'http://localhost:5000/artists/'+self.id+'/tracks'
        self.artist_url = 'http://localhost:5000/artists/'+self.id


# Modelo Album 
class Album(db.Model):
  name = db.Column(db.String(100), unique=True)
  genre = db.Column(db.String)
  artist_id = db.Column(db.String, db.ForeignKey('artist.id'), nullable=False)
  id = db.Column(db.String, primary_key=True)
  artist = db.Column(db.String)
  tracks = db.Column(db.String)
  album_url = db.Column(db.String)


  def __init__(self, name, genre, artist_id):
    self.name = name
    self.genre = genre
    self.artist_id = artist_id
    # encode id
    album_encode = b64encode(self.name.encode()).decode('utf-8')
    self.id = (album_encode+self.artist_id)
    if len(self.id)>22:
      self.id = self.id[:22]
    self.artist = 'http://localhost:5000/artists/'+self.artist_id
    self.tracks = 'http://localhost:5000/albums/'+self.id+'/tracks'
    self.album_url = 'http://localhost:5000/albums/'+self.id


# Modelo Track-- revisaar --
class Track(db.Model):
  id = db.Column(db.String, primary_key=True)
  album_id = db.Column(db.String, db.ForeignKey('album.id'), nullable=False)
  name = db.Column(db.String(100), unique=True)
  duration = db.Column(db.Float)
  times_played = db.Column(db.Integer)
  artist = db.Column(db.String)
  album = db.Column(db.String)
  track_url = db.Column(db.String)


  def __init__(self, name, duration, album_id):
    self.name = name
    self.album_id = album_id   
    self.duration = duration
    name_encode = b64encode(self.name.encode()).decode('utf-8')
    self.id = (name_encode+album_id)
    if len(self.id)>22:
      self.id = self.id[:22]

    self.times_played = 0
    self.artist = 'http://localhost:5000/artists/'+self.id  # artist id no sel
    self.tracks = 'http://localhost:5000/albums/'+self.album_id
    self.track_url = 'http://localhost:5000/albums/'+self.id
  

####### SCHEMAS ######
# Artist schema
class ArtistSchema(ma.Schema):
  class Meta:
    fields = ( 'id', 'name', 'age', 'albums', 'tracks', 'artist_url')

class AlbumSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'genre', 'artist_id', 'artist', 'tracks', 'album_url')

class TrackSchema(ma.Schema):
  class Meta:
    fields = ('id', 'albumm_id', 'name', 'duration', 'times_played', 'artist', 'album', 'track_url')


# Init schema
artist_schema = ArtistSchema()
artists_schema = ArtistSchema(many=True)

album_schema = AlbumSchema()
albums_schema = AlbumSchema(many=True) 

track_schema = TrackSchema()
tracks_schema = TrackSchema(many=True)


#### ROUTES ####
#Create a artist (route)
@app.route('/artists', methods=['POST'])
def add_artist():
    res = request.json
    name = str(res['name'])
    res2 = request.json
    age = int(res2['age'])

    new_artist = Artist(name, age)
    #print("NEW artist name and id ", new_artist.name, new_artist.id)
    db.session.add(new_artist)
    db.session.commit()

    return artist_schema.jsonify(new_artist), 201
    

# Get all artist
@app.route('/artists', methods=['GET'])
def get_artists():
  all_artists = Artist.query.all()
  result = artists_schema.dump(all_artists)
  return jsonify(result)


# get single artist
@app.route('/artists/<id>', methods=['GET'])
def get_artist(id):
  artist = Artist.query.get(id)
  return artist_schema.jsonify(artist)


# update an artist
@app.route('/artists/<id>', methods=['PUT'])
def update_artist(id):
  artist = Artist.query.get(id)

  name = request.json['name']
  age = request.json['age']

  artist.name = name
  artist.age = age

  db.session.commit()
  return artist_schema.jsonify(artist)


#delete an artist
@app.route('/artists/<id>', methods=['DELETE'])
def delete_artist(id):
  artist = Artist.query.get(id)
  db.session.delete(artist)
  db.session.commit()
  return artist_schema.jsonify(artist)


#Create an Album 
@app.route('/artists/<artist_id>/albums', methods=['POST'])
def add_album(artist_id):
    res = request.json
    name = str(res['name'])
    res2 = request.json
    genre = str(res2['genre'])
    
    new_album = Album(name, genre, artist_id)
    db.session.add(new_album)
    db.session.commit()

    return album_schema.jsonify(new_album), 201


#delete an album
@app.route('/albums/<album_id>', methods=['DELETE'])
def delete_album(id):
  album = Album.query.get(id)
  db.session.delete(album)
  db.session.commit()
  return album_schema.jsonify(album)


# get all albums of an artist
@app.route('/artists/<artist_id>/albums', methods=['GET'])
def get_artist(artist_id):
    all_artists = Artist.query.all()
  result = artists_schema.dump(all_artists)

  album = Artist.query.get(id)
  return artist_schema.jsonify(artist)


# Create a Track
@app.route('/albums/<album_id>/tracks', methods=['POST'])
def add_album(album_id):
    res = request.json
    name = str(res['name'])
    res2 = request.json
    duration = str(res2['duration'])
    
    new_track = Track(name, duration, album_id)
    db.session.add(new_track)
    db.session.commit()

    return track_schema.jsonify(new_track), 201

#delete a Track
@app.route('/tracks/<track_id>', methods=['DELETE'])
def delete_track(id):
  track = Track.query.get(id)
  db.session.delete(track)
  db.session.commit()
  return track_schema.jsonify(track)


#run server
if __name__ == '__main__':
    app.run(debug=True)
