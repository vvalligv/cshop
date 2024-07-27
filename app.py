from http.client import UPGRADE_REQUIRED
from msilib.schema import Upgrade
from cshop import create_app # type: ignore
from flask import Flask # type: ignore
from flask_migrate import Migrate # type: ignore
from flask_script import Manager  # type: ignore
from flask_migrate import MigrateCommand# type: ignore
from app import create_app, db

app = create_app()
#migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
@manager.command
def migrate_db():
    UPGRADE_REQUIRED() 


if __name__ == "__main__":
    app.run()