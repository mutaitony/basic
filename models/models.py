from flask_login import UserMixin,login_user,login_required,logout_user,LoginManager,current_user
from datetime import datetime
from __init__ import db
import enum, re, random, pytz
from sqlalchemy.orm import backref
tz = pytz.timezone('Africa/Nairobi')

class Users(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    job_title = db.Column(db.String(255))
    email = db.Column(db.String(80),unique=True)
    phone = db.Column(db.String(80))
    job_id = db.Column(db.String(80),unique=True)
    username = db.Column(db.String(80),unique=True)
    pos = db.Column(db.String(80),default="admin")
    pwd = db.Column(db.String(300), nullable=False, unique=True)
    
    def __repr__(self):
        return '<User %r>' % self.username

class PowerRooms(db.Model):
    __tablename__ = 'power_rooms'
    
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer)
    data = db.Column(db.PickleType)
    date = db.Column(db.DateTime, default=datetime.now())
    
    def __repr__(self):
        return '<Power Rooms %r>' % self.id
    
class Generators(db.Model):
    __tablename__ = 'generators'
    
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer)
    data = db.Column(db.PickleType)
    date = db.Column(db.DateTime, default=datetime.now())
    
    def __repr__(self):
        return '<Generators %r>' % self.id
    
class WhiteSpace(db.Model):
    __tablename__ = 'white_space'
    
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer)
    data = db.Column(db.PickleType)
    date = db.Column(db.DateTime, default=datetime.now())
    
    def __repr__(self):
        return '<White Space %r>' % self.id
    
class CommentsModel(db.Model):
    __tablename__ = 'comments_model'
    
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer)
    data = db.Column(db.PickleType)
    date = db.Column(db.DateTime, default=datetime.now())
    
    def __repr__(self):
        return '<Comments Model %r>' % self.id
    
class LogsModel(db.Model):
    __tablename__ = 'logs_model'
    
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.now())
    
    logs_type = db.Column(db.String(255))
    log_id = db.Column(db.Integer)
    
    def __repr__(self):
        return f'<Log: Date - {self.date}, Type - {self.logs_type}>'
    