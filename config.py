from distutils.debug import DEBUG



class Config:
  
  SQLCHEMY_TRACK_MODIFICATIONS = False
  SECRET_KEY ='aNGIE'
class ProdConfig(Config):
  pass

class DevConfig(Config):
  
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:cheeks@localhost/piches'

  DEBUG=True


config_options = {
  'development':DevConfig,
  'production':ProdConfig
}  