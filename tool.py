from flask import g, current_app


def func1():
    print(g.name)
    print(current_app.url_map)