from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired, Length

class CustomerForm(FlaskForm):
    first_name = StringField("First Name:", validators=[DataRequired(), Length(2, 45)])
    last_name = StringField("Last Name:", validators=[DataRequired(), Length(2, 45)])
    phone = StringField("Phone:", validators=[DataRequired(), Length(10, 12)])
    email = StringField("Email:", validators=[DataRequired(), Length(10, 250)])
    user_id = HiddenField()