from app import db
from sqlalchemy.sql.expression import text
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import Schema, fields, ValidationError


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
    name = fields.Str(required=True)
    email = fields.Email()
    
    class Meta:
       fields = ('id', 'email', 'name')
    
'''
class UsersSchema(Schema):
    formatted_name = fields.Method("format_name")

    def format_name(self, user):
        return "{}, {}".format(user.email, user.name)

    

    def must_not_be_blank(data):
      if not data:
        raise ValidationError('Data not provided.')'''
   
     
def  session_commit ():
      try:
        db.session.commit()
      except SQLAlchemyError as e:
         db.session.rollback()
         reason=str(e)
         return reason
