class config():
    SECRET_KEY = 'admin'
    CACHE_TYPE = 'simple'
    SWAGGER = {
        'title': 'Tech Challenger 1',
        'uiversion': 3
    }
    SQLALCHEMY_DATABASE_URI = 'sqlite:///recipes.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'admin'
