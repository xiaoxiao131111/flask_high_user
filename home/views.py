# 定义视图函数时, 使用蓝图对象来定义路由
from home import home_blu
from flask import url_for

# 2. 使用蓝图对象来定义路由
@home_blu.route('/')
def index():

    return "第一个蓝图"

@home_blu.route('/demo1')
def demo1():
    # 细节2: 蓝图定义的路由, 其函数标记为 蓝图名.函数名
    url1 = url_for('home_b.demo1')
    print(url1)
    return 'demo1'
