from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import Schema, fields, validate
from app.users.models import db


class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(250), nullable=False)
    address = db.Column(db.Text, nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    mobile = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)
    timestamp = db.Column(db.TIMESTAMP,server_default=db.func.current_timestamp(),nullable=False)
    date = db.Column(db.Date, nullable=False)
    pricing = db.Column(db.Numeric, nullable=False)

    def __init__(self,  name,  address,  is_active,  mobile,  email,  url,  timestamp,  date,  pricing, ):

        self.name = name
        self.address = address
        self.is_active = is_active
        self.mobile = mobile
        self.email = email
        self.url = url
        self.timestamp = timestamp
        self.date = date
        self.pricing = pricing

    def add(self, customer):
        db.session.add(customer)
        return session_commit()

    def update(self):
        return session_commit()

    def delete(self, customer):
        db.session.delete(customer)
        return session_commit()


class CustomersSchema(Schema):

    not_blank = validate.Length(min=1, error='Field cannot be blank')

    name = fields.String(validate=not_blank)
    address = fields.String(validate=not_blank)
    is_active = fields.Boolean(validate=not_blank)
    mobile = fields.Integer(validate=not_blank)
    email = fields.Email(validate=not_blank)
    url = fields.URL(validate=not_blank)
    timestamp = fields.DateTime(validate=not_blank)
    date = fields.Date(validate=not_blank)
    pricing = fields.Decimal(validate=not_blank)

    class Meta:
        fields = ('id',  'name',  'address',  'is_active',  'mobile',  'email',  'url',  'timestamp',  'date',  'pricing', )


def session_commit():
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        reason = str(e)
        return reason
