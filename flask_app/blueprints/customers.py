from flask import Blueprint, redirect, render_template, request, flash
from flask_app.forms.customer import CustomerForm
from flask_app.models.customer import Customer
from flask_app.extensions import db
from flask_login import current_user


bp = Blueprint("customers", __name__, url_prefix="/customers")


@bp.route("/")
def all_customer():
    """Display all current customers"""

    customers = Customer.query.all()

    return render_template("/customers/all_customer.html", customers=customers)


@bp.route("/create", methods=["GET", "POST"])
def create_customer():
    """Display and process the new customer form"""

    form = CustomerForm(user_id=current_user.id)

    if form.validate_on_submit():
        """do stuff"""
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        user_id = request.form.get("user_id")

        new_customer = Customer(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            user_id=user_id
        )

        db.session.add(new_customer)
        db.session.commit()

        flash("New customer has been added successfully")
        return redirect("/customers")

    return render_template("/customers/new_customer.html", form=form)


@bp.route("/<int:customer_id>")
def customer_detail(customer_id):
    '''display details of customer by id'''

    customer = Customer.query.filter(Customer.id==customer_id).first()

    return render_template("/customers/detail_customer.html", customer=customer)