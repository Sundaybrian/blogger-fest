import os

class Config:
    '''
    General Configurations parent class
    '''

    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://sundaypriest:belter@localhost/blogfest'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG=True
    
    
config_options={
    'development':DevConfig,
    'production':ProdConfig 
}    