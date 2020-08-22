from flask import json
from flask_restful import Resource, abort

from app import db
from app.models import Contact

def abort_if_no_contact(contact):
    if not contact:
        print('not found')
        abort(404, message='contact not found')

class ContactResource(Resource):
    def get(self, contact_id):
        contact = Contact.query.filter_by(id=contact_id).first()
        abort_if_no_contact(contact)
        return {
            'id': contact.id,
            'first_name': contact.first_name,
            'last_name': contact.last_name,
            'business': contact.business,
            'phone_number': contact.phone_number,
            'email': contact.email,
            'client_type': contact.client_type,
            'notes': contact.notes
        }

    # def post(self):

    def delete(self, contact_id):
        contact = Contact.query.filter_by(id=contact_id).first()
        abort_if_no_contact(contact)
        db.session.delete(contact)
        db.session.commit()
        return {'message': f'contact_id {contact_id} deleted'}

class ContactResourceList(Resource):
    def get(self):
        # return 'yup'
        return {'data': str(Contact.query.all())}
