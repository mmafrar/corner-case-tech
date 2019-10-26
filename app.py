import logging
from flask import Flask, request
from service import EmployeeService, RestaurantService, MenuService


app = Flask(__name__)
logging.basicConfig(filename="app.log", level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s")


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


if __name__ == "__main__":
    app.run(debug=True)
