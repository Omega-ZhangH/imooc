### Python Flask构建微信小程序订餐系统

```
Date    : 2019-06-25 16:28:06
Author  : 张皓
Email   : zhanghao12z@163.com
===========================================
简介     :利用flask编写小程序后端
				  并部署到centos7云主机
===========================================
```

#### 概述

项目准备：

```
开发工具：pycharm(内置数据库连接工具)
数据库：mysql(Mac推荐XAMPP)
py环境：Python3.6
运行主机:CentOS7
Python库：
flask
flask_sqlalchemy
pymysql
```

配置虚拟环境

首先在新建项目文件夹**imooc**

然后在当前文件夹运行

- 新建虚拟环境

```
pipenv install
```

- 查看新建的虚拟环境

```
pipenv —venv
```

- 在pycharm中新建项目imooc，并查找到对应的虚拟环境
- ![image-20190625163247753](/Users/omega/Library/Application Support/typora-user-images/image-20190625163247753.png)

#### 4-5 链接管理器和版本管理

连接管理器：url_for

版本管理：自定义的类

```python
/Users/omega/Downloads/学习成长/编程语言/python/mooc_py/Python Flask构建微信小程序订餐系统/imooc/common/libs/UrlManager.py

class UrlManager:
    @staticmethod
    def buildUrl(path):
        return path

    @staticmethod
    def buildStaticUrl(path):
        path = path + "?ver=" + '20190626155737'
        return path

```

#### 4-6 日志系统

```

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
```

#### 4-7 错误处理

```python
# flask错误处理
@app.errorhandler(404)
def page_not_found(error):
    app.logger.info(error)
    return 'this page does not exist', 404
```

#### 4-8 数据库ORM

需要新装 flask_sqlalchemy 和 mysqlclient（因这个需要安装依赖，这里用pymysql代替）

在imooc文件夹下，进入项目的Python虚拟环境

```
pipenv shell
```

分别安装

```
 pip3 install flask_sqlalchemy

 pip3 install pymysql
```

或者在pycharm中安装

![image-20190626173358550](/Users/omega/Library/Application Support/typora-user-images/image-20190626173358550.png)

#### 4-9 打造高可用flask mvc框架