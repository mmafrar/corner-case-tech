from flask import Flask, request
from service import EmployeeService, RestaurantService, MenuService

app = Flask(__name__)


@app.route("/employee/create", methods=["POST"])
def create_employee():
    return EmployeeService().create(request.get_json())


@app.route("/restaurant/create", methods=["POST"])
def create_restaurant():
    return RestaurantService().create(request.get_json())


@app.route("/menu/upload", methods=["POST"])
def upload_menu():
    return MenuService().upload(request.get_json())


@app.route("/menu", methods=["GET"])
def get_menu():
    return MenuService().get()


if __name__ == "__main__":
    app.run(debug=True)
