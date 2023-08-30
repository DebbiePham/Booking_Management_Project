from flask_app.extensions import db
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Date, Time
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.sql import func

class Appointment(db.Model):
    __tablename__="appointments"
    query = db.session.query_property()

    id = Column(Integer, primary_key=True, autoincrement='auto')
    customer_name = Column(String(45), nullable=False)
    service_name = Column(String(45), nullable=False)
    duration = Column(String(12), nullable=False)
    employee_name = Column(String(45), nullable=False, unique=True)
    date = Column(Date, nullable=False, unique=True)
    start_time = Column(Time, nullable=False, unique=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    service_id = Column(Integer, ForeignKey("services.id"), nullable=False)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    customer = relationship("Customer", backref="appointments")
    service = relationship("Service", backref="appointments")
    designer = relationship("Employee", backref="appointments")
    