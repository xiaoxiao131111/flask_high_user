# 1. 加载配置： app.config 用于设置配置，该属性继承自dict， 可以以字典形式赋值取值
from flask import Flask, session
from datetime import timedelta
from config import config_dict

# 工厂函数： 根据参数需求， 内部封装对象的创建过程
def create_app(config_type):
    '''封装应用的创建过程'''
    # 创建应用
    flask_app = Flask(__name__)
    # 根据配置类型取出对应的配置子类
    config_class = config_dict[config_type]
    # 加载普通配置
    flask_app.config.from_object(config_class)

    return flask_app

# 创建应用对象
app = create_app('dev')
app.secret_key = 'test'

@app.route("/create")
def create():
    print(app.config.get('SQL_URL'))
    return "index"
# 从对象中加载配置
# 优点： 面向对象的设计有利于 减少重复代码， 以及代码解耦合
from config import DevelopmentConfig
app.config.from_object(DevelopmentConfig)

# config属性用于设置配置
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)

@app.route('/')
def index():
    # 设置session 用于测试配置是否生效
    session['name'] = 'zs'

    # 读取配置
    print(app.config.get('PERMANENT_SESSION_LIFETIME'))
    return 'index'



if __name__ == '__main__':
    app.run(debug=True)