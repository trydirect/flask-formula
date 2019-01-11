from app import db
from app.libs.models import ModelMixin


class Users(db.Model, ModelMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100), nullable=True)
    password = db.Column(db.String(100), nullable=True)
    auth_token = db.Column(db.String(100), nullable=True)
    
    def __repr__(self):
        return '<User %r>' % self.id

    @property
    def get_id(self):
        return self.id

    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password,
            'auth_token': self.auth_token,
        }

