from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import Schema, fields, validate
from app.users.models import db

class {Resources}(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(250), unique=True, nullable=False)
  name = db.Column(db.String(250), nullable=False) 

  def __init__(self,email, name,):
    self.email=email
    self.name=name

  def add(self,{resource}):
     db.session.add({resource})
     return session_commit ()

  def update(self):
      return session_commit()

  def delete(self,{resource}):
     db.session.delete({resource})
     return session_commit()

class {Resources}Schema(Schema):

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
