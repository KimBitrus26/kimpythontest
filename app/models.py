from app import db, ma
from datetime import datetime


class Song(db.Model):
    __tablename__ = 'songs'
    id = db.Column(db.Integer, primary_key = True, unique=True, nullable=False)
    name_of_song = db.Column(db.String(100), nullable=False)
    duration_of_song = db.Column(db.Integer, nullable=False)
    uploaded_time = db.Column(db.DateTime, default=datetime.utcnow,nullable=False)
   

    def __init__(self, name_of_song,duration_of_song,uploaded_time):
        self.name_of_song = name_of_song
        self.duration_of_song = duration_of_song
        self.uploaded_time = uploaded_time

class SongSchema(ma.Schema):
    class Meta:
        model = Song

        sqla_session = db.session
    
        fields = ('id','name_of_song','duration_of_song','uploaded_time')

song_schema = SongSchema()
songs_schema = SongSchema(many=True)
        
class Podcast(db.Model):
    __tablename__ = 'podcasts'
    id = db.Column(db.Integer, primary_key = True, unique=True, nullable=False)
    name_of_podcast = db.Column(db.String(100), nullable=False)
    duration_of_podcast = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    host = db.Column(db.String(100), nullable=False)
    particpants = db.Column(db.String(100), nullable=True)

    def __init__(self, name_of_podcast,duration_of_podcast,host,particpants):
        self.name_of_podcast = name_of_podcast
        self.duration_of_podcast = duration_of_podcast
        self.host = host
        self.particpants = particpants

    #using getter and setter to store the list of participants

    @property
    def particpants(self):
        return [int(x) for x in self.particpants.split(",")]

    @particpants.setter
    def particpants(self, value): # append the list of strings to participant field
        self.particpants += ',%s' % value


class PodcastSchema(ma.Schema):
    class Meta:
        model = Podcast

        sqla_session = db.session
    
        fields = ('id','name_of_podcast','duration_of_podcast','host', 'participants')

podcast_schema = PodcastSchema()
podcasts_schema = PodcastSchema(many=True)   
    
class AudioBook(db.Model):
    __tablename__ = 'audiobooks'
    id = db.Column(db.Integer, primary_key = True, unique=True, nullable=False)
    title_of_audiobook = db.Column(db.String(100), nullable=False)
    author_of_the_title = db.Column(db.String(100), nullable=False)
    narrator = db.Column(db.String(100), nullable=False)
    duration_of_audiobook = db.Column(db.Integer, nullable=False)
    uploaded_time = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, title_of_audiobook, author_of_the_title, narrator, duration_of_audiobook, uploaded_time):
        self.title_of_audiobook = title_of_audiobook
        self.author_of_the_title = author_of_the_title
        self.narrator = narrator
        self.duration_of_audiobook = duration_of_audiobook
        self.uploaded_time = uploaded_time

class AudioBookSchema(ma.Schema):
    class Meta:
        model = AudioBook

        sqla_session = db.session
    
        fields = ('id','title_of_audiobook','author_of-the_title','narrator', 'duration_of_audiobook','uploaded_time')

audiobook_schema = AudioBookSchema()
audiobooks_schema = AudioBookSchema(many=True)   
    
    
                  
#programmatic creating database when running "flask run"
db.create_all()
