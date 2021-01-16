"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db=SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

#models go below
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer,  primary_key=True, autoincrement=True)
               
    first_name = db.Column(db.String(25),
                     nullable=False)

    last_name = db.Column(db.String(25),
                     nullable=False)
    image_url = db.Column(db.String, 
                    nullable=True)
    posts= db.relationship("Post", backref="user", cascade="all, delete-orphan")
    
    

class Post(db.Model):

    __tablename__="posts"

    id = db.Column(db.Integer,  primary_key=True, autoincrement=True)
    title=db.Column(db.String(50),
                nullable=False, unique=True)
    content=db.Column(db.String,
                nullable=False)
    created_at=db.Column(db.DateTime, nullable=False,
                default=datetime.utcnow)

    user_id=db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))

    tags = db.relationship('Tag',
                               secondary='post_tags',
                               backref='posts')
    


class Tag(db.Model):

    __tablename__="tags"
    
    id = db.Column(db.Integer,  primary_key=True, autoincrement=True)
    name=db.Column(db.String(40), nullable=False, unique=True)

class PostTag(db.Model):

    __tablename__="post_tags"

    post_id = db.Column(db.Integer,
                       db.ForeignKey("posts.id", ondelete="CASCADE"),
                       primary_key=True)
                       #together they are the primary key (the two columns)
    tag_id = db.Column(db.Integer,
                          db.ForeignKey("tags.id", ondelete="CASCADE"),
                          primary_key=True)