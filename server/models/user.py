#!/usr/bin/python3
"""
Model for users table
maps tables to python objects and
prints the official string representation of the class
"""


from server import db
from datetime import datetime


class User(db.Model):
    """
    creates a class User which represents the users table
    Map the ORM to python object
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(120), nullable=False)
    lastname = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    phone_number = db.Column(db.String(60), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    listings = db.relationship('Listing', backref='user',
                               cascade='all, delete-orphan')
    sender = db.relationship('Conversation', backref='sender',
                             foreign_keys='Conversation.sender_id',
                             cascade='all, delete-orphan')
    receiver = db.relationship('Conversation', backref='receiver',
                               foreign_keys='Conversation.recipient_id',
                               cascade='all, delete-orphan')
    """messages = db.relationship('Message', backref='users',
                                  cascade='all, delete, delete-orphan')"""

    def __repr__(self):
        """
        Prints official string representation of the User class
        """
        return f'User({self.id}, {self.firstname}, {self.lastname}, \
                {self.email}, {self.phone_number}, {self.created_at})'