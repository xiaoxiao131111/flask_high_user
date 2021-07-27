'''
统一处理
需求: 获取用户身份
分析: 除了静态资源, 基本所有视图都需要获取用户身份, 每个视图单独获取出现大量的代码冗余
解决办法: 设置 请求钩子, 并通过 g变量 将数据传递给视图函数
'''
from flask import Flask, session, g

app = Flask(__name__)
app.secret_key = 'test'

# 需求1： 所有视图都需要获取用户身份
# 解决方法：用钩子函数进行封装， 减少代码冗余
@app.before_request
def prepare():
    # 必须使用g变量来传递数据，使用全局变量不能记录并发的多个请求数据
    g.name = session.get('username')


@app.route('/')
def index():
    if g.name:
        return '欢迎回来, %s' % g.name
    else:
        return '首页'


@app.route('/demo1/')
def demo1():
    '''登录'''
    session['username'] = 'zs'
    return '登录成功'

if __name__ == '__main__':
    app.run(debug=True)