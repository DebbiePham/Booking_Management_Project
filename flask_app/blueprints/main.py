from flask import Blueprint, render_template, redirect, request, flash
from flask_app.forms.register import RegisterForm
from flask_app.forms.login import LoginForm
from flask_app.forms.appointment import AppointmentForm
from flask_login import current_user, login_required
from flask_app.models.appointment import Appointment
from flask_app.extensions import db


bp = Blueprint("main", __name__)


appointments = [
    {
        'customer_name' : 'Test',
        'service_name' : 'Test',
        'employee_name' : 'Test',
        'duration' : 'Test',
        'date' : '2023-08-25',
        'start_time' : '11:00',
    },
    {
        'customer_name' : 'AnotherTest',
        'service_name' : 'AnotherTest',
        'employee_name' : 'AnotherTest',
        'duration' : 'AnotherTest',
        'date' : '2023-08-27',
        'start_time' : '15:00',
    }
]



@bp.get("/")
def index():
    '''Display the home page'''
    
    return redirect("/auth/login")


@bp.get("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")

@bp.route("/add")
def add_appointment():
    '''display the add appointment form'''
    return render_template("/appointments/add.html")

@bp.route("/create", methods=['GET', 'POST'])
def create_appointment():

    """do stuff"""
    
    form = AppointmentForm(user_id=current_user.id)

    if form.validate_on_submit():
        customer_name = request.form.get("customer_name")
        service_name = request.form.get("service_name")
        duration = request.form.get("duration")
        employee_name = request.form.get("employee_name")
        date = request.form.get("date")
        start_time = request.form.get("start_time")
        customer_id = request.form.get("customer_id")
        service_id = request.form.get("service_id")
        employee_id = request.form.get("employee_id")

        new_appointment = Appointment(
            customer_name=customer_name,
            service_name=service_name,
            duration=duration,
            employee_name=employee_name,
            date=date,
            start_time=start_time,
            customer_id=customer_id,
            service_id=service_id,
            employee_id=employee_id
        )

        db.session.add(new_appointment)
        db.session.commit()

        flash("New appointment has been added successfully")
        return redirect("/dashboard")

    return render_template("/appointments/add.html", form=form)