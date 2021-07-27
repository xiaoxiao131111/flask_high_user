from datetime import timedelta

class BaseConfig:
    '''配置基类。 可以将相同的配置抽取到基类中，减少重复代码'''

    # 定义和配置同名的类属性
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)


class DevelopmentConfig(BaseConfig):
    '''开发环境'''
    SQL_URL = '127.0.0.1:3306/test1'  # 数据库地址


class ProductionConfig(BaseConfig):
    '''生产环境'''
    SQL_URL = '127.0.0.1:3306/users'  # 数据库地址

# 主文件 应用配置.py 从对象中加载封装的配置 app.config.from_object()

"""
切换配置
虽然封装了多套配置， 但需要 修改代码才能切换配置， 这种方式并不利于开发和测试
Flask 提供了切换配置的更好方案， 需要进行一下两步
    定义工厂函数， 封装应用的创建过程
    利用环境变量， 调用工厂函数， 指定配置并动态创建应用
"""

# 定义工厂函数， 封装应用的创建过程
# 定义字典来记录 配置类型和配置子类 之间的映射关系
config_dict = {
    'dev': DevelopmentConfig,
    'pro': ProductionConfig
}

# 在 主文件 应用配置.py中， 定义工厂函数封装应用的创建过程，并通过参数指定应用的配置类型