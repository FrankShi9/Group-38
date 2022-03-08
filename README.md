### 3/7跟进： 前后端同步了文件路径和请求ip端口， 更新了渲染忘记密码页面代码
### 问题： 可以启动服务器，但是渲染页面时再次遇到找不到js、css文件: 
`请看‘bug log.txt’文件`

---

#### 3/4尝试了corsheader跨域接收register.vue的post过来的用户输入email与密码，并导入数据库，返回一个‘success’的http响应，但是目前log显示接受的是空内容，数据库存入的也是空内容，需要解决

---

# Group-38

## Run the Project

新建conda环境

`conda create -n proj38 python=3.7`

激活环境

`conda activate proj38`

安装项目依赖

`pip install -r requirements.txt `

运行
```
cd Area_38
python manage.py runserver
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
