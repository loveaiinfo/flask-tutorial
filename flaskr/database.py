from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
import click
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

def init_db():
  db.create_all()

@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    with current_app.app_context():
      init_db()
    click.echo('Initialized the database.')

def init_app(app):
    db.init_app(app)
    app.cli.add_command(init_db_command)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    def verify_password(self, password):
      return check_password_hash(self.password, password)

def add_user(username, password):
  user = User(username=username, password=generate_password_hash(password))
  db.session.add(user)
  db.session.commit()


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    body = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))