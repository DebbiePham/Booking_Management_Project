from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, IntegerField
from wtforms.validators import DataRequired, Length

class PaymentForm(FlaskForm):
    name_on_card = StringField("Name On Card:", validators=[DataRequired(), Length(2, 45)])
    card_number = IntegerField("Card Number:", validators=[DataRequired(), Length(15, 16)])
    csv = IntegerField("CSV:", validators=[DataRequired(), Length(3, 4)])
    zip_code = IntegerField("Zip Code:", validators=[DataRequired(), Length(5, 6)])
    customer_id = HiddenField()