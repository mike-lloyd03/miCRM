from flask import request
from app import app
from app.models import Contact
from app import db

@app.route('/')
def index():
    return 'This is a functional app!'

@app.route('/create-contact', methods=['GET'])
def create_contact():
    new_contact = Contact(
        first_name=request.args.get('first-name'),
        last_name=request.args.get('last-name')
    )
    db.session.add(new_contact)
    db.session.commit()
    return request.args.get('first-name') + request.args.get('last-name')

@app.route('/show-db')
def show_dp():
    all_contacts = Contact.query.all()
    print((all_contacts))
    return str(all_contacts)
