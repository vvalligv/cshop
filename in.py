#from flask import Flask # type: ignore
#from flask_sqlalchemy import SQLAlchemy # type: ignore
#import os
#from .routes import update_loyalty_points

#db = SQLAlchemy()

#def create_app():
 #   app = Flask(__name__,instance_path='/home/val_vv/instance/new_db.sqlite')
 #   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path)
  #  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  #  app.config['SECRET_KEY'] = 'your_secret_key'

  #  db.init_app(app)

  #  from .routes import update_loyalty_points # type: ignore
  #  app.register_blueprint(update_loyalty_points, url_prefix='/api')

  #  return app
