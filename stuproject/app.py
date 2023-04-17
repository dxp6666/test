from flask import Flask
from settings import DevelopmentConfig,DefaultConfig
from common.model.user import db
from apps.stu import stu_bp
from flask_cors import CORS    # 跨域
from apps.information import infor
def create_flask_app(config):
    app = Flask(__name__)
    db.init_app(app)
    cors = CORS(app)
    cors.init_app(app,supports_credentials=True)
    app.config.from_object(config)
    app.register_blueprint(stu_bp)
    return app
app = create_flask_app(DevelopmentConfig)

app.register_blueprint(infor)
if __name__ == '__main__':
    app.run(port=3001)
