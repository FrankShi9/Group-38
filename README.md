# Group-38

## Run the Project

新建conda环境

`conda create -n proj38 python=3.7`

激活环境

`conda activate proj38`

安装项目依赖

`pip install -r requirements.txt `

数据库迁移

```
cd Area_38
python manage.py makemigrations
python manage.py migrate
```

最后启动服务器，正常测试
```
python manage.py runserver
```

浏览器输入
```
http://127.0.0.1:8000/
```

## 查看数据库

`sqlite3 db.sqlite3`

支持sql查询

https://blog.csdn.net/u013664733/article/details/54912201



## 开源项目参考

### 百科全书： https://github.com/FrankShi9/awesome-business-intelligence

### 项目1： 可视化管理： https://github.com/FrankShi9/grafana

### 项目2： 股票可视化分析： https://github.com/meppps/ML-Financial-Analysis-WebApp



## 后端代码库：
https://github.com/FrankShi9/Area_38_Backend



## 前端代码

https://github.com/FrankShi9/Group-38/tree/frontend-dev

还是在这个仓库里，我新建了一个分支。
