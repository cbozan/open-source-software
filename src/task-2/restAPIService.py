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
    
    def post(self):
        f = open("default_parameters.json", "r")
        default_parameters = json.loads(f.read())
        f.close()
        
        hl = request.args.get('hl')
        tz = request.args.get('tz')
        pn = request.args.get('pn')

        if hl== None:
            hl = default_parameters.get('hl')
            
        if tz == None:
            tz = default_parameters.get('tz')
            
        if pn == None:
            pn = default_parameters.get('pn')

        default_parameters['hl'] = hl
        default_parameters['tz'] = tz
        default_parameters['pn'] = pn

        with open("default_parameters.json", "w") as outfile:
            json.dump(default_parameters, outfile)
        outfile.close()

        return default_parameters, 200


api.add_resource(DefaultParameters, "/default_parameters")

if __name__ == "__main__":
    app.run()
