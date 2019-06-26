#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : 2019-06-26 15:42
Author  : 张皓
Email   : zhanghao12z@163.com
Function: 
===========================================
调用方法
Template:
===========================================
"""


class UrlManager:
    @staticmethod
    def buildUrl(path):
        return path

    @staticmethod
    def buildStaticUrl(path):
        path = path + "?ver=" + '20190626155737'
        return path
