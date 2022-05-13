from distutils.debug import DEBUG



class Config:
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:cheeks@localhost/piches'

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
   if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://",1)

class DevConfig(Config):
  
  #SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:cheeks@localhost/piches'
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://jjiahbzznlufye:b171e7612ae7f1ebb4f7cd1eb475413d68bf14cd829ef03564c6ac38714859f7@ec2-54-158-247-210.compute-1.amazonaws.com:5432/de2nhnhleqksmo'
  DEBUG=True


config_options = {
  'development':DevConfig,
  'production':ProdConfig
}  