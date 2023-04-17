# 导包
from flask import Flask

# 实例化flask对象
app = Flask(__name__)

# 编写路由与视图
@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/home')
def home():
    return '这是主页！'

# 启动服务
if __name__ == '__main__':
    app.run()

'''
1.实例化Flask对象:
app = Flask(__name__)
	1).__name__参数用于确定启动程序的位置
    2).__name__参数可以传递除了标准模块名的任意字符串, 但不推荐
    3).__name__参数如果传递标准模块名, 不影响路由的匹配, 但会影响静态文件的加载
    
2.@app.route('/'): 路由配置
@app.route('路由')是一装饰器的形式构建路由的, 其第一个参数为路由路径

3.app.run(): Flask实例的方法, 用于启动web服务, 可选参数如下:
	- host: 服务启动的IP地址
    - port: 服务启动的端口
    - debug: 是否以调试模式启动
    示例: app.run(host='127.0.0.1', port=8899, debug=True)
'''
