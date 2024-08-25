from flask_app import app

from flask_app.controllers import users_controller, reports_controller


import os
from dotenv import load_dotenv

load_dotenv()
password = os.getenv('password')


if __name__ == "__main__":
    app.run(debug=True, host="Localhost", port=5000)
