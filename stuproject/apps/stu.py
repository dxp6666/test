'''
coding:utf-8
@Time:2023/3/14 16:23
@Author:dxp
'''
from flask import Blueprint, request, Flask, jsonify
from flask_restful import Api, Resource, marshal, fields, reqparse
from common.model.user import db, User
stu_bp = Blueprint('student', __name__)
api = Api(stu_bp)
# stu_select = Blueprint('select', __name__)
# API = Api(stu_select)
# 序列化
ai_resource = {
    'id': fields.Integer,
    'user_id': fields.String,
    'user_pw': fields.String,
    'user_name': fields.String,
    'user_fullname': fields.String
}
class aioneRescoure(Resource):
    def __init__(self):
        self.parse = reqparse.RequestParser()
    def post(self):
        self.parse.add_argument('id', type=int)
        self.parse.add_argument('user_id', type=str)
        self.parse.add_argument('user_pw', type=str)
        self.parse.add_argument('user_name', type=str)
        self.parse.add_argument('user_fullname', type=str)
        args = self.parse.parse_args()
    # 3.获取参数
        user_id = args['user_id']
        user_pw = args['user_pw']
        user_name = args['user_name']
        user_fullname = args['user_fullname']

        user = User(user_id=user_id, user_pw=user_pw, user_name=user_name, user_fullname=user_fullname)
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            print(e)
            data = {"mate": {"msg": "添加失败", "status": 500}}
            return jsonify(data)
        data = {"mate": {"msg": "添加成功", "status": 200}}
        return jsonify(data)

class Ai(Resource):
    def get(self):
        res = User.query.all()
        return marshal(res, ai_resource)

class Ais(Resource):
    def get(self):
        res = User.query.all()
        print(res, '>>>>>>>>>>>')
        li = []
        for u in res:
            data = {"user_id":u.user_id, "user_pw":u.user_pw, "user_name":u.user_name, "user_fullname":u.user_fullname}
            li.append(data)
        a = {"msg": "查询成功", "status": 200}
        print(li)
        return jsonify({"data": li, "mate": a})

# 路由
api.add_resource(aioneRescoure, '/user/add', endpoint='user')
api.add_resource(Ai, '/user/check', endpoint='check')
api.add_resource(Ais, '/user/list', endpoint='list')

