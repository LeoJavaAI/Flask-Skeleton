from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import Schema, fields, validate

db = SQLAlchemy()

class Users(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(250), unique=True, nullable=False)
  name = db.Column(db.String(250), nullable=False) 

  def __init__(self,email, name,):
    self.email=email
    self.name=name

  def get_id(self):
    return str(self.id)

  def add(self,user):
     db.session.add(user)
     return session_commit ()

  def update(self):
      return session_commit()

  def delete(self,user):
     db.session.delete(user)
     return session_commit()

class UsersSchema(Schema):

    not_blank = validate.Length(min=1, error='Field cannot be blank')
    name = fields.String(validate=not_blank)
    email = fields.Email()
    
    class Meta:
       fields = ('id', 'email', 'name')
      
     
def  session_commit ():
      try:
        db.session.commit()
      except SQLAlchemyError as e:
         db.session.rollback()
         reason=str(e)
         return reason
