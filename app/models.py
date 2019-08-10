from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Role(db.Model):
    __tablename__='roles'
    
    id=db.Column(db.Integer(),primary_key=True)
    role=db.Column(db.String(12))
    users=db.relationship('User',backref='role',lazy='dynamic')


class User(UserMixin,db.Model):
    __tablename__='users'
    
    id=db.Column(db.Integer,primary_key=True)
    profile_image=db.Column(db.String(64))
    email=db.Column(db.String(64),unique=True,index=True)
    username=db.Column(db.String(64),unique=True)
    password_hash=db.Column(db.String(128))
    role_id=db.Column(db.Integer(),db.ForeignKey('roles.id'))
    # posts=db.relationship('BlogPost',backref='author',lazy='dynamic')

    comments_user=db.relationship('Comment',backref='commenter',lazy="dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.password_hash=generate_password_hash(password)

    
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def save_user(self):
        '''
        save instance for a user
        '''
        db.session.add(self)
        db.session.commit()  
        
    @classmethod
    def check_roles(cls,user_id,role_id):
        get_role=User.query.filter_by(id=user_id).filter_by(role_id=role_id).first()
        return get_role    
    
    def __repr__(self):
        return f'User {self.username}'    


        
