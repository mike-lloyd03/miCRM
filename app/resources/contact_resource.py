from flask import json
from flask_restful import Resource, abort, reqparse

from app import db
from app.models import Contact

put_args = reqparse.RequestParser()
put_args.add_argument('first_name', type=str)
put_args.add_argument('last_name', type=str)
put_args.add_argument('business', type=str)
put_args.add_argument('phone_number', type=str)
put_args.add_argument('email', type=str)
put_args.add_argument('client_type', type=str)
put_args.add_argument('notes', type=str)


def abort_if_no_contact(contact):
    if not contact:
        print('not found')
        abort(404, message='Contact not found')

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

    def put(self, contact_id):
        contact = Contact.query.filter_by(id=contact_id).first()
        abort_if_no_contact(contact)

    def delete(self, contact_id):
        contact = Contact.query.filter_by(id=contact_id).first()
        abort_if_no_contact(contact)
        db.session.delete(contact)
        db.session.commit()
        return {'message': f'contact_id {contact_id} deleted'}

class ContactResourceList(Resource):
    def get(self):
        return {'data': str(Contact.query.all())}

    def post(self):
        args = put_args.parse_args()
        new_contact = Contact(
            first_name=args['first_name'],
            last_name=args['last_name'],
            business=args['business'],
            phone_number=args['phone_number'],
            email=args['email'],
            client_type=args['client_type'],
            notes=args['notes']
        )
        db.session.add(new_contact)
        db.session.commit()
        return {'message': f'New contact, {args["first_name"]} {args["last_name"]} created.'}, 201

