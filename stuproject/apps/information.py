from flask import jsonify,request,json
from flask import Blueprint
infor = Blueprint('infor',__name__)
@infor.route('/user/checkUser', methods=['POST'])
def get():
    # username = request.form.get('username')
    # password = request.form.get('password')
    json_data = json.loads(request.get_data().decode('utf-8'))
    username = json_data.get('username')
    password = json_data.get('password')
    # print(username, password)
    if username == 'admin' and password == '123':
        date = {'mate':{'msg': '登录成功','status': 200}}
        return jsonify(date)
    else:
        date = {'mate': {'msg': '登录失败','status': 500}}
        return jsonify(date)















