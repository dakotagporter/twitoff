"""Prediction of user based on tweet embeddings"""

import numpy as np
from sklearn.linear_model import LogisticRegression
from .models import User
from .twitter import vectorize_tweet


def predict_user(user0_name, user1_name, hypo_tweet_text):
    """
    Determine and return which user is more likely to say given 'tweet'.

    Args:
        user0_name (str): 1st user to compare
        user1_name (str): 2nd user to compare
        hypo_tweet_text (str): hypothetical tweet

    Returns:
        0 or 1: a.k.a. user0 or user1
    """

    # Get users from database
    user0 = User.query.filter(User.name == user0_name).one()
    user1 = User.query.filter(User.name == user1_name).one()

    # Get vectors from each users' tweets
    user0_vects = np.array([tweet.vect for tweet in user0.tweets])
    user1_vects = np.array([tweet.vect for tweet in user1.tweets])

    # Vertically stack vectors to train model
    vects = np.vstack([user0_vects, user1_vects])

    # Generate labels for vects array
    labels = np.concatenate(
        [np.zeros(len(user0.tweets)), np.ones(len(user1.tweets))])

    # Train model
    log_reg = LogisticRegression().fit(vects, labels)

    # Using nlp to generate embeddings - hypo_tweet_text
    hypo_tweet_vect = vectorize_tweet(hypo_tweet_text).reshape(1, -1)

    return log_reg.predict(hypo_tweet_vect)
