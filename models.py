
from werkzeug.security import generate_password_hash, check_password_hash # type: ignore
from . import db # type: ignore
import sqlite3 as sql
from flask_login import UserMixin # type: ignore
#from flask_sqlalchemy import SQLAlchemy # type: ignore

# type: ignore
class User(db.Model,UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)
    Email = db.Column(db.String(100), unique=True, nullable=False)
    Password = db.Column(db.String(100), nullable=False)
    FullName = db.Column(db.String(100), nullable=False)
    loyalty_points = db.Column(db.Float, default=0.0) # Add Points field to store loyalty points

    def __repr__(self):
        return f"<User {self.Email}>"
    
    



