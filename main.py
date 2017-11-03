from flask import Flask
from config import DevConfig


app = Flask(__name__)
'''
get the config from object of DevConfig
使用config.from_object()而不使用app.config['DEBUG']是因为这样可以
加载class Devconfig的配置变量集合，而不需要一项一项的添加和修改
'''
app.config.from_object(DevConfig)


@app.route('/')
def index():
    return '<h1>Hello World</h1>'


if __name__ == '__main__':
    # entry the application
    app.run()
