from app import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), index=True)
    last_name = db.Column(db.String(120), index=True)
    business = db.Column(db.String(240))
    phone_number = db.Column(db.Integer)
    email = db.Column(db.String(120))
    client_type = db.Column(db.String(240))

    def __repr__(self):
        return f'<Contact {self.last_name}, {self.first_name}>'
     
