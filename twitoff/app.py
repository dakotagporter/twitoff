from flask import Flask, render_template
from .models import DB, User, Tweet, insert_example_users


def create_app():
    """
    Create and configure instantiation of Flask application.
    """
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite3:///db.sqlite3'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    DB.init_app(app)

    @app.route("/")
    def root():
        DB.drop_all()
        DB.create_all()
        insert_example_users()

        users = User.query.all()
        return render_template('base.html', title="Home", users=users)

    return app
