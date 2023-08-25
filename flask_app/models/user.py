from flask_app.extensions import db
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class User(UserMixin, db.Model):
    __tablename__="users"
    query = db.session.query_property()

    id = Column(Integer, primary_key=True, autoincrement='auto')
    businessname = Column(String(45), nullable=False)
    address = Column(String(250), nullable=False)
    phone = Column(String(12), nullable=False)
    business_license = Column(String(45), nullable=False)
    email = Column(String(45), nullable=False, unique=True)
    password = Column(String(60), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
