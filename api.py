# IP代理池-Flask开发对外接口

from flask import Flask,g
from db import RedisClient

__all__ = ['app']
app = Flask(__name__)

def get_coon():
    if not hasattr(g,'redis'):
        g.redis = RedisClient()
    return g.redis

@app.route('/')
def index():
    return '<h2>Welcome to Proxy Pool System</h2>'

@app.route('/random')
def get_proxy():
    '''
    获取随机可用代理
    :return: 随机代理
    '''
    coon = get_coon()
    return coon.random()

@app.route('/count')
def get_counts():
    '''
    获取代理池总量
    :return: 代理池总量
    '''
    coon = get_coon()
    return str(coon.count())

@app.route('/all')
def get_all():
    '''
    获取全部代理
    :return: 全部代理
    '''
    coon = get_coon()
    return '<br>'.join(coon.all())

if __name__ == '__main__':
    app.run()
