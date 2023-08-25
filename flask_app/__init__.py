from flask import Flask
from dotenv import load_dotenv
from os import environ
from flask_app.blueprints.main import bp as main
from flask_app.blueprints.auth import bp as auth
from flask_app.blueprints.employees import bp as employees
from flask_app.blueprints.services import bp as services
from flask_app.blueprints.customers import bp as customers
from flask_app.blueprints.payments import bp as payments
from flask_app.blueprints.appointments import bp as appointments
from flask_app.extensions import db, bcrypt, login_manager

load_dotenv()
SECRET_KEY = environ.get("SECRET_KEY")
SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")

def create_app():
    '''Flask app factory'''
    # App configuration
    app = Flask(__name__)
    app.secret_key = SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI


    # Register blueprint
    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(employees)
    app.register_blueprint(services)
    app.register_blueprint(customers)
    app.register_blueprint(payments)
    app.register_blueprint(appointments)

    # Initialize Extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    
    with app.app_context():
        from flask_app.models.user import User
        from flask_app.models.employee import Employee
        from flask_app.models.service import Service
        from flask_app.models.customer import Customer
        from flask_app.models.payment import Payment
        from flask_app.models.appointment import Appointment
        
        db.create_all()

    return app
