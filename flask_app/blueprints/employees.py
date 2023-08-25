from flask import Blueprint, redirect, render_template, request, flash
from flask_app.forms.employee import EmployeeForm
from flask_app.models.employee import Employee
from flask_app.extensions import db
from flask_login import current_user


bp = Blueprint("employees", __name__, url_prefix="/employees")


@bp.route("/")
def all_employee():
    """Display all current employees"""

    employees = Employee.query.all()

    return render_template("/employees/all_employee.html", employees=employees)


@bp.route("/create", methods=["GET", "POST"])
def create_employee():
    """Display and process the new employee form"""

    form = EmployeeForm(user_id=current_user.id)

    if form.validate_on_submit():
        """do stuff"""
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        job_title = request.form.get("job_title")
        address = request.form.get("address")
        phone = request.form.get("phone")
        experience = request.form.get("experience")
        email = request.form.get("email")
        pay_rate = request.form.get("pay_rate")
        user_id = request.form.get("user_id")

        new_employee = Employee(
            first_name=first_name,
            last_name=last_name,
            job_title=job_title,
            address=address,
            phone=phone,
            experience=experience,
            email=email,
            pay_rate=pay_rate,
            user_id=user_id
        )

        db.session.add(new_employee)
        db.session.commit()

        flash("Create new employee successful")
        return redirect("/employees")

    return render_template("/employees/new_employee.html", form=form)


@bp.route("/<int:employee_id>")
def employee_detail(employee_id):
    '''display details of employee by id'''

    employee = Employee.query.filter(Employee.id==employee_id).first()

    return render_template("/employees/detail_employee.html", employee=employee)