from flask.json import jsonify
from flask import Flask, redirect
from src.constants.http_status_codes import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
import os
from src.auth import auth
from src.bookmarks import bookmarks
from src.database import db, Bookmark
from flask_jwt_extended import JWTManager


def create_app(test_config=None):
    app = Flask(__name__,instance_relative_config=True)
    
    if test_config is None: 
        app.config.from_mapping(
            SECRET_KEY=os.environ.get
            ("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DB_URI"),
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            JWT_SECRET_KEY=os.environ.get('JWT_SECRET_KEY')
        )
    else:
        app.config.from_mapping(test_config)
    
    db.app=app
    db.init_app(app)
    
    JWTManager(app)
    app.register_blueprint(auth)
    app.register_blueprint(bookmarks)
    
    @app.get('/<short_url>')
    def redirect_to_url(short_url):
        bookmark = Bookmark.query.filter_by(short_url = short_url).first_or_404()
        
        if bookmark:
            bookmark.visits = bookmark.visits + 1
            db.session.commit()
            
            return redirect(bookmark.url)
        
    @app.errorhandler(HTTP_404_NOT_FOUND)
    def handle_404(e):
        return jsonify({'error': 'Not Found'}), HTTP_404_NOT_FOUND
    
    @app.errorhandler(HTTP_500_INTERNAL_SERVER_ERROR)
    def handle_500():
        return jsonify({'error': 'Something went wrong, we are sorting it out'}), HTTP_500_INTERNAL_SERVER_ERROR
     
    return app