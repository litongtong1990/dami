# 农业管理系统


### 系统说明

* 本系统使用Python的Django框架搭建。
* 前端部分使用bootstrap。


### 运行说明

* 首先运行 pip install django-crontab 来安装 django-crontab 这个插件
* 运行 python manage.py crontab add 来运行crontab
* 在终端中执行`python manage.py runserver`命令即可运行本地开发服务器。
* 在浏览器里访问`http://127.0.0.1:8000`即可查看该网站。


### 功能实现

* 实现了用户权限相关的基本操作（注册、登陆、修改密码、注销）
* 实现了用户分级（普通用户与管理员用户）
* 管理员账号：admin123 密码：admin123。
* 在管理员权限下可以进行添加溯源信息以及生成二维码，其他页面在普通权限的用户下就可以进行操作。



sqlite3 db.sqlite3
sqlite>.header on
sqlite>.mode column
sqlite> select * from management_environment;
