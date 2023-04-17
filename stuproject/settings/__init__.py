'''
coding:utf-8
@Time:2023/3/14 11:08
@Author:dxp
'''
class DefaultConfig(object):
    SECERY_KEY = '123esseds'
class DevelopmentConfig(DefaultConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/stu'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    JSON_AS_ASCII = False
    RESTFUL_JSON = dict(ensure_ascii=False)








