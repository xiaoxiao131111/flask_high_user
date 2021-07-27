'''
请求钩子
可以对请求的各阶段进行监听，方便开发者_
针对请求完成一些统一的处理， 以便减少重复的代码
作用类比Django中的中间件
'''
'''
before_request:
    每次执行视图函数之前调用
    对请求进行一些准备处理
    如果在该函数中返回一个响应，视图函数将不再被调用
'''
'''
after_request:
    如果没有抛出错误，每次执行视图函数之后（已经包装为响应对象）调用
    在此函数中可以对响应值在返回之后做最后的修改处理
    接受一个参数： 包装好的响应对象
    需要降修改后的响应对象返回
'''
'''
before_first_request
    web应用被第一次请求钱调用
    可以进行web应用初始化处理
'''
'''
teardown_request:
    每次执行视图函数之后调用
    无论是否出现异常都会执行，一般用于请求收尾
    接受一个参数： 错误信息，如果有相关错误抛出
'''

# 代码示例
from flask import Flask, Response

app = Flask(__name__)

# 每次执行视图函数之前调用，对请求进行一些准备处理，如 参数解析， 黑名单过滤， 数据统计等
@app.before_request
def prepare():
    print('before_request')
# 另一种语法
# def prepare():
#     print('before_request')

app.before_request(prepare)

# 每次执行视图函数之后（已经包装为响应对象）调用， 对响应进行一些加工处理，如设置统一响应头，设置数据的外层包装
@app.after_request
def process(response: Response): # 必须定义形参接受响应对象
    print('after_request:')
    return response

# web应用被第一次请求钱调用，可以进行web应用初始化处理，如数据库连接
@app.before_first_request
def initial():
    print('before_first_request')

# 每次执行视图函数之后调用， 无论是否出现异常都会执行， 一般用于请求收尾， 如资源回收， 异常统计
@app.teardown_request  # 测试时不要开启调试模式
def request_handle(error): # 必须定义形参来接收具体错误信息， 如果没有错误， error=None
    print('teardown_request: %s' % error)


@app.route('/')
def hello_world():
    print('执行视图')
    a = 1 / 0
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
