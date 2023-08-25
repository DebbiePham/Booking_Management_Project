from flask import Blueprint, redirect, render_template, request, flash
from flask_app.forms.service import ServiceForm
from flask_app.models.service import Service
from flask_app.extensions import db
from flask_login import current_user


bp = Blueprint("services", __name__, url_prefix="/services")


@bp.route("/")
def all_service():
    """Display all current services"""

    services = Service.query.all()

    return render_template("/services/all_service.html", services=services)


@bp.route("/create", methods=["GET", "POST"])
def create_service():
    """Display and process the new service form"""

    form = ServiceForm(user_id=current_user.id)

    if form.validate_on_submit():
        """do stuff"""
        name = request.form.get("name")
        description = request.form.get("description")
        price = request.form.get("price")
        user_id = request.form.get("user_id")

        new_service = Service(
            name=name,
            description=description,
            price=price,
            user_id=user_id
        )

        db.session.add(new_service)
        db.session.commit()

        flash("New service has been added successfully")
        return redirect("/services")

    return render_template("/services/new_service.html", form=form)


@bp.route("/<int:service_id>")
def service_detail(service_id):
    '''display details of employee by id'''

    service = Service.query.filter(Service.id==service_id).first()

    return render_template("/services/detail_service.html", service=service)