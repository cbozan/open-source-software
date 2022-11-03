# Required Libraries - Gerekli Kütüphaneler
#import os
#os.system("pip install flask")
#os.system("pip install flask_restful")
#os.system("pip install pandas")

from flask import Flask, request
from flask_restful import Api, Resource
import pandas as pd
import json

app = Flask(__name__)
api = Api(app)

class DefaultParameters(Resource):
    def get(self):
        f = open("default_parameters.json", "r")
        default_parameters = json.loads(f.read())
        f.close()

        return default_parameters, 200

api.add_resource(DefaultParameters, "/default_parameters")

if __name__ == "__main__":
    app.run()
