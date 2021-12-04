import uuid
from dataclasses import dataclass
from datetime import datetime
from src import db


@dataclass
class Song(db.Model):
    id: str
    name: str
    duration: int
    uploaded_time: str

    id = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    uploaded_time = db.Column(db.DateTime, default=datetime.utcnow)


@dataclass
class Podcast(db.Model):
    id: str
    name: str
    uploaded_time: int
    host: str
    participants: str

    id = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    uploaded_time = db.Column(db.DateTime, default=datetime.utcnow)
    host = db.Column(db.String(100), nullable=False)
    participants = db.Column(db.String(1100), nullable=True)


@dataclass
class Audiobook(db.Model):
    id: str
    title: str
    author: str
    narrator: str
    duration: int
    uploaded_time: str

    id = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    narrator = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    uploaded_time = db.Column(db.DateTime, default=datetime.utcnow)
