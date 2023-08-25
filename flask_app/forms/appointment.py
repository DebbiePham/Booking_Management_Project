from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, DateField, TimeField
from wtforms.validators import DataRequired, Length

class AppointmentForm(FlaskForm):
    customer_name = StringField("First Name:", validators=[DataRequired(), Length(2, 45)])
    service_name = StringField("Last Name:", validators=[DataRequired(), Length(2, 45)])
    duration = StringField("Phone:", validators=[DataRequired(), Length(2, 45)])
    employee_name = StringField("Email:", validators=[DataRequired(), Length(2, 45)])
    date = DateField("Service Date:", validators=[DataRequired()])
    start_time = TimeField("Start Time:", validators=[DataRequired()])
    employee_id = HiddenField()
    service_id = HiddenField()
    customer_id = HiddenField()