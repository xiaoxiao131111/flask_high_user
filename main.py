# 想要让蓝图对象能够完成路由定义, 还需要 Flask应用注册蓝图对象
from flask import Flask
from home import home_blu

app = Flask(__name__)

# 3.应用注册蓝图对象
app.register_blueprint(home_blu)


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)