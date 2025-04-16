from flask import Flask
from flasgger import Swagger
from api.routes import register_routes

app = Flask(__name__)

app.config['SWAGGER'] = {
    'title': 'Tech Challeger 1',
    'uiversion': 1
}

swagger = Swagger(app)
register_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
    