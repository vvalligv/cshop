from flask import Flask # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask_migrate import Migrate # type: ignore
from flask_login import LoginManager # type: ignore
import os
from flask import Flask, request, jsonify # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore
import os
# type: ignore

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__,instance_path='/home/val_vv/instance/new_db.sqlite')

    
    app.config['SECRET_KEY'] = 'secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
    print("Database URI:", app.config['SQLALCHEMY_DATABASE_URI'])
    #/home/val_vv/instance/new_db.sqlite
   
    import logging
    logging.basicConfig()
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


    db.init_app(app)
    migrate.init_app(app, db)


    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.session_protection = "strong"
    login_manager.init_app(app)

    from .models import User

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    #@login_manager.user_loader
    #def load_user(user_id):
        #return User.query.get(int(user_id))
    #with app.app_context():
        #db.create_all()


    

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))
    
    from .models import User
   # db = SQLAlchemy(app)
    from .main import main as main_blueprint # type: ignore
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint # type: ignore
    app.register_blueprint(auth_blueprint)
    #from .routes import update_loyalty_points # type: ignore
    #app.register_blueprint(update_loyalty_points)
     
    return app
#from cshop import db
#from cshop.models import User

#users = User.query.all()
#for user in users:
#    print(f"ID: {user.id}, Email: {user.Email}, FullName: {user.FullName},Points:{user.Points}")