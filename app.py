import logging
from flask import Flask, request
from config import ApplicationConfig
from services.menu import MenuService
from services.employee import EmployeeService
from services.restaurant import RestaurantService

# Creates a Flask application with logging parameters
app = Flask(__name__)
logging.basicConfig(filename=ApplicationConfig.LOG_FILENAME, level=ApplicationConfig.LOG_LEVEL,
                    format=ApplicationConfig.LOG_FORMAT)


@app.route("/employee/create", methods=["POST"])
def create_employee():
    logging.info('Creating employee')
    return EmployeeService().create(request.get_json())


@app.route("/restaurant/create", methods=["POST"])
def create_restaurant():
    logging.info('Creating restaurant')
    return RestaurantService().create(request.get_json())


@app.route("/menu/upload", methods=["POST"])
def upload_menu():
    logging.info('Uploading menu for restaurant')
    return MenuService().upload(request.get_json())


@app.route("/menu", methods=["GET"])
def get_menu():
    logging.info('Getting current day menu')
    return MenuService().get()


@app.route("/menu/vote", methods=["POST"])
def menu_vote():
    logging.info('Voting for restaurant menu')
    return MenuService().vote(request.get_json())


@app.route("/menu/results", methods=["GET"])
def menu_results():
    logging.info('Getting results for current day')
    return MenuService().results()

# Main entry point into the application
if __name__ == "__main__":
    app.run(debug=True)
