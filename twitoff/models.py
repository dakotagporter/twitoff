"""SQLAlchemy models and utility functions for TwitOff"""

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


# User Table
class User(DB.Model):
    """Twitter users corresponding to Tweets"""
    # primary id column
    id = DB.Column(DB.BigInteger, primary_key=True)
    # name column
    name = DB.Column(DB.String, nullable=False)

    def __repr__(self):
        return f"<User: {self.name}>"


# Tweet Table
class Tweet(DB.Model):
    """Tweet text and data"""
    # primary id column
    id = DB.Column(DB.BigInteger, primary_key=True)
    # text column of character length 300
    text = DB.Column(DB.Unicode(300))
    # foreign key - user.id
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))

    def __repr__(self):
        return f"<Tweet: {self.text}>"


def insert_example_users():
    """Will get error if ran twice since data already exists"""
    dakota = User(id=1, name='Dakota')
    elonmusk = User(id=2, name="elonmusk")
    DB.session.add('Dakota')  # Adds user
    DB.session.add('elonmusk')  # Adds user
    DB.session.commit()
