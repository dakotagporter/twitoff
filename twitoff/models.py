"""SQLAlchemy models and utility functions for TwitOff"""

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

DB = SQLAlchemy()
MIGRATE = Migrate()


# User Table
class User(DB.Model):
    """Twitter users corresponding to Tweets"""
    # primary id column
    id = DB.Column(DB.BigInteger, primary_key=True)
    # name column
    name = DB.Column(DB.String, nullable=False)
    # keeps track of users most recent tweets
    newest_tweet_id = DB.Column(DB.BigInteger)  # FIX!!

    def __repr__(self):
        return f"<User: {self.name}>"


# Tweet Table
class Tweet(DB.Model):
    """Tweet text and data"""
    # primary id column
    id = DB.Column(DB.BigInteger, primary_key=True)
    # text column of character length 300
    text = DB.Column(DB.Unicode(300))
    # column containing vector processed tweets
    vect = DB.Column(DB.PickleType, nullable=False)
    # foreign key - user.id
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'),
                        nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))

    def __repr__(self):
        return f"<Tweet: {self.text}>"
