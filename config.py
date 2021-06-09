import os
from instance.config import SECRET_KEY


class Config:
    '''
    general configuration parent class
    '''
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:newPass@3@localhost/watchlist'


class ProdConfig(Config):
    '''
    production configuration child class
    '''
    pass

class DevConfig(Config):
    '''
    development configuration child class
    '''
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production': ProdConfig
}