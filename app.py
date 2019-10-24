from flask import Flask, request
from service import EmployeeService

app = Flask(__name__)


@app.route("/employee/create", methods=["POST"])
def create_employee():
    return EmployeeService().create(request.get_json())


if __name__ == "__main__":
    app.run(debug=True)
