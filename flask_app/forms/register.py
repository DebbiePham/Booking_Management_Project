from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegisterForm(FlaskForm):
    businessname = StringField("Business Name:", validators=[DataRequired(), Length(2, 45)])
    address = StringField("Address:", validators=[DataRequired(), Length(10, 250)])
    phone = StringField("Phone:", validators=[DataRequired(), Length(10, 12)])
    business_license = StringField("Business License:", validators=[DataRequired(), Length(9, 45)])
    email = EmailField("Email:", validators=[DataRequired(), Email()])
    password = PasswordField("Password:", validators=[DataRequired(), Length(8, 45)])
    confirm_password = PasswordField("Confirm Password:", validators=[EqualTo("password", "password must match.")])