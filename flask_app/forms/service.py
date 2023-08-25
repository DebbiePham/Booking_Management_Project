from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired, Length

class ServiceForm(FlaskForm):
    name = StringField("Service Name:", validators=[DataRequired(), Length(2, 45)])
    description = StringField("Description:", validators=[DataRequired(), Length(2, 280)])
    price = StringField("Price:", validators=[DataRequired(), Length(2, 45)])
    user_id = HiddenField()