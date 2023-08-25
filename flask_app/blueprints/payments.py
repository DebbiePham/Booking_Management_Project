from flask import Blueprint, redirect, render_template, request, flash
from flask_app.forms.payment import PaymentForm
from flask_app.models.payment import Payment
from flask_app.models.customer import Customer
from flask_app.extensions import db
from flask_login import current_user


bp = Blueprint("payments", __name__, url_prefix="/payments")


@bp.route("/")
def all_payment():
    """Display payment method of current customer"""

    payments = Payment.query.all()

    return render_template("/payments/all_payment.html", payments=payments)


@bp.route("/create", methods=["GET", "POST"])
def create_payment():
    """Display and process the new payment form"""

    form = PaymentForm(user_id=current_user.id)

    if form.validate_on_submit():
        """do stuff"""
        name_on_card = request.form.get("name_on_card")
        card_number = request.form.get("card_number")
        csv = request.form.get("csv")
        zip_code = request.form.get("zip_code")
        customer_id = request.form.get("customer_id")

        new_payment = Payment(
            name_on_card=name_on_card,
            card_number=card_number,
            csv=csv,
            zip_code=zip_code,
            customer_id=customer_id
        )

        db.session.add(new_payment)
        db.session.commit()

        flash("New payment has been added successfully")
        return redirect("/payments")

    return render_template("/payments/new_payment.html", form=form)

@bp.route("/<int:payment_id>")
def detail_payment(payment_id):
    '''display details of payment by id'''

    payment = Payment.query.filter(Payment.id==payment_id).first()

    return render_template("/payments/detail_payment.html", payment=payment)


@bp.route("/<int:payment_id>/edit")
def edit_payment(payment_id):
    '''display details of payment by id'''

    payment = Payment.query.update(Payment.id==payment_id)

    return render_template("/payments/detail_payment.html", payment=payment)