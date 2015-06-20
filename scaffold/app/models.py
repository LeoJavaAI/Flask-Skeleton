from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import Schema, fields, validate
from app.users.models import db


class {Resources}(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    {db_rows}

    def __init__(self, {init_args}):
        {init_self_vars}

    def add(self, {resource}):
        db.session.add({resource})
        return session_commit()

    def update(self):
        return session_commit()

    def delete(self, {resource}):
        db.session.delete({resource})
        return session_commit()


class {Resources}Schema(Schema):

    not_blank = validate.Length(min=1, error='Field cannot be blank')
    {schema}

    class Meta:
        fields = ('id', {meta})


def session_commit():
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        reason = str(e)
        return reason
