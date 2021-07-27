from flask import Blueprint
'''
蓝图的三个使用细节
创建蓝图时, 可以通过 url_prefix参数 给蓝图定义的路由添加 统一的URL资源段前缀
蓝图定义的路由, 其函数标记为 蓝图名.函数名
蓝图也可以 设置请求钩子
只有访问该蓝图定义的路由时才会触发
实现局部监听
'''

# 1. 创建蓝图对象
# 细节1: 可以通过url_prefix参数给蓝图定义的路由添加统一的URL资源段前缀
home_blu = Blueprint("home_b", __name__, url_prefix='/home')

# 细节3: 蓝图也可以设置请求钩子 只有访问该蓝图定义的路由时才会触发 局部监听
@home_blu.before_request
def home_prepare():
    print('home_prepare')

# 4. 让视图文件和主程序建立关联
# 遇到ImportError, 需要查看和调整代码的执行顺序
from . import views