from flask import Flask
from controllers import front_controller as fc
from flask_cors import CORS
import logging

app = Flask(__name__)

CORS(app)
logging.basicConfig(filename='myapp.log', level=logging.INFO)
logging.info('Started')
fc.route(app)
app.secret_key = "any random string"
if __name__ == '__main__':
    app.run(debug=True)
