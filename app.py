from flask import Flask


def create_app():
    """
    Create and configure instantiation of Flask application.
    """
    app = Flask(__name__)

    @app.route("/")
    def root():
        return 'Hello TwitOff!'

    return app
