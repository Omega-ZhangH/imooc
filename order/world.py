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

from flask import Blueprint


api = Blueprint('imooc', __name__)


@api.route('/')
def hello_world():
    return 'api world'


@api.route('/api')
def index():
    return 'api page'


@api.route('/api/hello')
def hello():
    return 'api hello'
