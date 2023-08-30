from flask_app.extensions import db
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.sql import func


class Service(db.Model):
    __tablename__="services"
    query = db.session.query_property()

    id = Column(Integer, primary_key=True, autoincrement='auto')
    name = Column(String(45), nullable=False)
    description = Column(String(280), nullable=False)
    price = Column(String(45), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    employer = relationship("User", backref="services")