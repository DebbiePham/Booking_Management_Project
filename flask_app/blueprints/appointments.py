from flask import Blueprint, redirect, render_template, request, flash
from flask_app.forms.appointment import AppointmentForm
from flask_app.models.appointment import Appointment
from flask_app.extensions import db
from flask_login import current_user


bp = Blueprint("appointments", __name__, url_prefix="/appointments")


