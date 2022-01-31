from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from resources.Home import Home
from resources.ShortLinks import ShortLinks

app = Flask(__name__)
api = Api(app)
CORS(app)


api.add_resource(ShortLinks, '/shortlinks')
# TODO react-app serving route
api.add_resource(Home, '/')


if __name__ == '__main__':
    app.run(debug=True)
