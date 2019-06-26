#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : 2019-06-25 15:18
Author  : 张皓
Email   : zhanghao12z@163.com
Function: 
===========================================
调用方法
Template:
===========================================
"""

from flask import Flask, url_for
from world import api
from common.libs.UrlManager import UrlManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text


app = Flask(__name__)

USERNAME = 'mstx'
PASSWORD = 'mstx'
HOSTNAME = 'localhost'
PORT = 63306
DATABASE = 'mysql'


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://{username}:{password}@{host}:{port}/" \
         "{db}?charset=utf8".format(username=USERNAME,
                                    password=PASSWORD,
                                    host=HOSTNAME,
                                    port=PORT,
                                    db=DATABASE)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)

app.register_blueprint(api, url_prefix='/imooc')


@app.route('/')
def hello_world():
    url = UrlManager.buildUrl("/api")

    staticUrl = UrlManager.buildStaticUrl("/css/bootstrap.css")

    msg = '连接地址:%s;静态地址：%s' % (url, staticUrl)

    # 分别打印三个级别的日志信息
    app.logger.info(msg)
    app.logger.error(msg)
    app.logger.debug(msg)



    return msg


@app.route('/api')
def index():
    url = url_for('index')
    return 'Index视图的url地址是：' + url


@app.route('/api/hello')
def hello():
    sql = text('select * from user')

    result = db.engine.execute(sql)

    for row in result:
        app.logger.info(row)

    return 'Index hello'


# flask错误处理
@app.errorhandler(404)
def page_not_found(error):
    app.logger.info(error)
    return 'this page does not exist', 404


if __name__ == '__main__':
    app.run(debug=True)
