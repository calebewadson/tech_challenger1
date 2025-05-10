from flask import Flask
from flasgger import Swagger
from api.routes import register_routes
from api.config import config

app = Flask(__name__)

app.config.from_object(config)

swagger = Swagger(app)
register_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
    