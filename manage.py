from app import create_app, database
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = create_app()
migrate = Migrate(app, database)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app import models

if __name__ == '__main__':
    manager.run()