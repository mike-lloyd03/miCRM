from datetime import datetime

from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), index=True)
    last_name = db.Column(db.String(120), index=True)
    email = db.Column(db.String(120))
    password_hash = db.Column(db.String(128))
    contacts = db.relationship('Contact', backref='owner', lazy='dynamic')

    def __repr__(self):
        return f'<Contact id={self.id}, name={self.last_name}, {self.first_name}>'
    
    def __str__(self):
        return f'<Contact id={self.id}, name={self.last_name}, {self.first_name}>'


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    first_name = db.Column(db.String(120), index=True)
    last_name = db.Column(db.String(120), index=True)
    business = db.Column(db.String(240))
    phone_number = db.Column(db.String(10))
    email = db.Column(db.String(120))
    client_type = db.Column(db.String(240))
    notes = db.Column(db.String(5000))

    def __repr__(self):
        return f'<Contact id={self.id}, name={self.last_name}, {self.first_name}>'
    
    def __str__(self):
        return f'<Contact id={self.id}, name={self.last_name}, {self.first_name}>'


class Meeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))
    date_time = db.Column(db.DateTime, default=datetime.utcnow)
    location = db.Column(db.String(240))
    notes = db.Column(db.String(5000))

    def __repr__(self):
        return f'<Contact {self.user_id}, {self.contact_id}>'
     
    def __str__(self):
        return f'<Contact {self.user_id}, {self.contact_id}>'


class FollowUp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))
    date_time = db.Column(db.DateTime, default=datetime.utcnow)
    notes = db.Column(db.String(5000))

    def __repr__(self):
        return f'<Contact {self.user_id}, {self.contact_id}>'
     
    def __str__(self):
        return f'<Contact {self.user_id}, {self.contact_id}>'
