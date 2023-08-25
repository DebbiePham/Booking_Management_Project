from flask_app.extensions import db
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Payment(db.Model):
    __tablename__="payments"
    query = db.session.query_property()

    id = Column(Integer, primary_key=True, autoincrement='auto')
    name_on_card = Column(String(45), nullable=False)
    card_number = Column(Integer(), nullable=False)
    csv = Column(Integer(), nullable=False)
    zip_code = Column(Integer(), nullable=False, unique=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    card_holder = relationship("Customer", backref="payments")