from distutils.debug import DEBUG


class Config:
  
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:cheeks@localhost/piches'

class ProdConfig(Config):
  pass

class DevConfig(Config):

  DEBUG=True


config_options = {
  'development':DevConfig,
  'production':ProdConfig
}  