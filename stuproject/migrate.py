'''
coding:utf-8
@Time:2023/3/14 11:26
@Author:dxp
'''
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from common.model.user import db, User
from app import app

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()




