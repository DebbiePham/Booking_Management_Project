from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField, HiddenField
from wtforms.validators import DataRequired, Length, Email

class EmployeeForm(FlaskForm):
    first_name = StringField("First Name:", validators=[DataRequired(), Length(2, 45)])
    last_name = StringField("Last Name:", validators=[DataRequired(), Length(2, 45)])
    job_title = StringField("Job Title:", validators=[DataRequired(), Length(2, 45)])
    address = StringField("Address:", validators=[DataRequired(), Length(10, 250)])
    phone = StringField("Phone:", validators=[DataRequired(), Length(10, 12)])
    experience = StringField("Experience:", validators=[DataRequired(), Length(10, 280)])
    email = StringField("Email:", validators=[DataRequired(), Length(10, 45)])
    pay_rate = StringField("Pay Rate:", validators=[DataRequired(), Length(2, 4)])
    user_id = HiddenField()