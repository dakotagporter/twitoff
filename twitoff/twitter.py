"""Retrieve Tweets, embeddings, etc. and push to database."""

from os import getenv
import tweepy
import spacy
from .models import DB, Tweet, User

TWITTER_AUTH = tweepy.OAuthHandler(
    getenv("TWITTER_API_KEY"), getenv("TWITTER_API_SECRET"))
TWITTER = tweepy.API(TWITTER_AUTH)

nlp = spacy.load("my_model")


def vectorize_tweet(tweet_text):
    return nlp(tweet_text).vector


def add_or_update_user(username):
    try:
        """Adds or updates user (username) to our database."""
        twitter_user = TWITTER.get_user(username)
        db_user = (User.query.get(twitter_user.id)) or User(
            id=twitter_user.id, name=username)
        DB.session.add(db_user)

        tweets = twitter_user.timeline(
            count=200,
            exclude_replies=True,
            include_rts=False,
            tweet_mode="Extended"
        )

        for tweet in tweets:
            db_user.newest_tweet_id = tweets[0].id
            vectorized_tweet = vectorize_tweet(tweet.text)
            db_tweet = Tweet(id=tweet.id, text=tweet.text,
                             vect=vectorized_tweet)
            db_user.tweets.append(db_tweet)
            DB.session.add(db_tweet)

    except Exception as e:
        print(f"Error processing {username}: {e}")
        raise e

    else:
        DB.session.commit()
