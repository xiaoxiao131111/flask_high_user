'''
上下文
    是一个数据容器，保存了flask 程序运行过程中的一些信息
    flask中有两种上下文，请求上下文和应用上下文
    两种上下文的使用范围相同， 从请求开始到请求结束，在范围外使用会报错
'''

# 请求上下文
'''
记录一些和请求有关的数据，包括request和session两个变量
request： 封装http请求的内容， 针对的是http请求
session： 用来记录请求会话中的信息，针对的是用户信息
'''

# 应用上下文
'''
记录一些和应用有关的数据， 包括current_app 和 g两个变量
current_app: 会自动引用创建的flask对象，需要在项目的其他文件中使用app时，应该通过current_app来获取，可以减少循环导入问题
g： flask给开发者预留的一个容器，用于记录自定义数据
    g变量每次请求会重置数据
    g使用场景： 1>在钩子函数和视图函数之间传递数据  3>函数嵌套调用时传递数据
'''

from flask import Flask, request, current_app, g

# 上下文变量： 有使用范围[请求开始， 请求结束]
# 请求上下文： 记录一些和请求有关的数据 request session
# 应用上下文： 记录一些和应用有关的数据 current_app g

import tool

app = Flask(__name__)


@app.route('/')
def index():
    g.name = 'zs'

    tool.func1()
    return 'index'

@app.route('/demo1')
def demo1():
    print(g.name)  # 会报错
    return 'demo1'