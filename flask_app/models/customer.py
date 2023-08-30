from flask_app.extensions import db
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.sql import func

class Customer(db.Model):
    __tablename__="customers"
    query = db.session.query_property()

    id = Column(Integer, primary_key=True, autoincrement='auto')
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    phone = Column(String(12), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    business = relationship("User", backref="customers")