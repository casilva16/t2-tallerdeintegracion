#from flask_sqlalchemy import SQLAlchemy
#from flask import Flask, request, jsonify
#from flask_marshmallow import Marshmallow
#from app import db
#import os


#db = import db


# # Modelos/Clases
# class Artist(db.Model):
#     id = db.Column(db.String, primary_key=True)
#     name = db.Column(db.String(100), unique=True)
#     age = db.Column(db.Integer)
#     albums = db.Column(db.String)
#     tracks = db.Column(db.String)
#     self = db.Column(db.String)

#     def __init__(self, name, age):
#         self.id = b64encode(self.name.encode()).decode('utf-8')
#         self.name = name
#         self.age = age
#         self.albums = "http://localhost:5000/artists/"+self.id+"/albums"
#         self.tracks = "http://localhost:5000/artists/"+self.id+"/tracks"
#         self.self = "http://localhost:5000/artists/"+self.id


# # Modelo Album 
# class Album(db.Model):
#   id = db.Column(db.String, primary_key=True)
#   #artist_id = db.Column(db.String, db.ForeignKey('artist.id'), nullable=False)
#   name = db.Column(db.String(100), unique=True)
#   genre = db.Column(db.String)
#   artist = db.Column(db.String)
#   tracks = db.Column(db.String)
#   self_url = db.Column(db.String)


#   def _init_(self, name, genre, artist_id):
#     self.name = name
#     self.id = b64encode(self.name.encode()).decode('utf-8')
#     self.artist_id = artist_id
#     self.genre = genre
#     self.artist = 'http://localhost:5000/artists/'+self.id
#     self.tracks = 'http://localhost:5000/albums/'+self.id+"tracks"
#     self.self_url = 'http://localhost:5000/albums/'+self.id


# # Modelo Track-- revisaar --
# class Track(db.Model):
#   id = db.Column(db.String, primary_key=True)
#   #artist_id = db.Column(db.String, db.ForeignKey('artist.id'), nullable=False)
#   #album_id = 
#   name = db.Column(db.String(100), unique=True)
#   duration = db.Column(db.Float)
#   times_played = db.Column(db.Integer)
#   artist = db.Column(db.String)
#   album = db.Column(db.String)
#   self_url = db.Column(db.String)


#   def _init_(self, artist_id):
#     self.name = name
#     self.id = b64encode(self.name.encode()).decode('utf-8')
#     self.artist_id = artist_id
#     self.duration = duration
#     self.times_played = times_played
#     self.artist = 'http://localhost:5000/artists/'+self.id
#     self.tracks = 'http://localhost:5000/albums/'+self.id+"tracks"
#     self.self_url = 'http://localhost:5000/albums/'+self.id

