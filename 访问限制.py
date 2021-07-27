# 需求： 对指定的路由进行访问限制
# 分析： 部分视图需要身份校验，这部分视图每个单独校验仍会出现大量的代码冗余
# 解决办法： 封装 装饰器 完成身份校验逻辑， 对指定视图函数设置装饰器

# 代码示例
from flask import Flask, session, g, abort
from functools import wraps

app = Flask(__name__)
app.secret_key = 'test'

@app.before_request
def prepare():
    g.name = session.get('username')


@app.route('/')
def index():
    if g.name:
        return '欢迎回来， %s' % g.name
    else:
        return '首页'

@app.route('/login')
def login():
    '''登录'''
    session['username'] = 'zs'
    return '登录成功'

# 需求2： 对部分视图进行访问限制  如个人中心必须登录才能访问
# 解决方案： 使用装饰器封装访问限制  减少代码冗余
def login_required(f):   # f = user

    @wraps(f)
    def wrapper(*args, **kwargs):
        # 获取函数名
        print(wrapper.__name__)

        if g.name: #用户已经登录
            return f(*args, **kwargs)  # 正常访问视图函数
        else:  # 用户未登录
            abort(401)  # 400 语法/参数错误 401 未认证  403 已认证, 权限不足  404 资源不存在  405 请求方式不支持  500 服务器错误

    return wrapper


@app.route('/user')
@login_required
def user():
    '''个人中心'''
    return '访问%s的个人中心' % g.name

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)


'''
functools.wraps
系统内置的装饰器， 主要用于装饰器中的闭包函数
作用是： 将被装饰的函数（wrapper）的函数信息替换为 指定函数（f）的函数信息（包括name 函数名， doc函数注释等）
'''