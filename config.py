from distutils.debug import DEBUG



class Config:
  
  SQLCHEMY_TRACK_MODIFICATIONS = False
  SECRET_KEY ='aNGIE'
  UPLOADED_PHOTOS_DEST = 'app/static/photos'
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = "MAIL_USERNAME"
  MAIL_PASSWORD = "MAIL_PASSWORD"

class ProdConfig(Config):
   SQLALCHEMY_DATABASE_URI="DATABASE_URL"

class DevConfig(Config):
  
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:cheeks@localhost/piches'

  DEBUG=True


config_options = {
  'development':DevConfig,
  'production':ProdConfig
}  