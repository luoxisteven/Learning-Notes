# Full-Stack Enginnering
## Frontend

### 1) Vue
```bash
# 运行
npm rum build
```

### 2) Angular

### 3) React

## Backend

### 1) Springboot

### 2) Django
https://blog.csdn.net/Ans_min/article/details/123146335

- #### **Build Project**
    ```bash
    django-admin startproject <myproject_name>
    cd myproject
    python manage.py startapp <myapp_name>
    ```
- #### **Build App**
    ```
    Step1:
    python manage.py startapp <app_name>
    Step2:
    在主setting.py 注册 <app_name>/apps.py的config，
    如rfp_llm/apps.py里面RfpLlmConfig，则在主settings.pyd的INSTALL_APPS加上"rfp_llm.apps.RfpLlmConfig"
    ```

- #### **Build API**
    ```
    在urls.py注册views函数
    ```

- #### **Run**
    ```bash
    python manage.py runserver
    ```

- #### **Layout**
    ```
    django_study_demo
    │─ manage.py			【项目管理的脚本，不要修改，eg：启动、创建app、数据库管理等】
    └─django_study_demo		【与项目同名的文件夹】
        │─ asgi.py			【和wsgi.py一起，接收网络请求的】【不用修改】【Django接收异步的】
        │─ settings.py		【项目的配置文件，eg：数据库连接信息、注册app等】【常操作】
        │─ urls.py			【全部的URL和函数的对应关系】【常操作】
        │─ wsgi.py			【和asgi.py一起，接收网络请求的】【不用修改】【Django接收同步的】
        │─ __init__.py
    ```

- #### 数据库增删改查

    在Django中，可以通过操作对象的方式，简化SQL语句的书写，方便地操作数据库表中的数据。以下是增、删、改、查的基本操作示例：

    - `增加数据`
        - 语法：`类名.objects.create()`

        ```python
        # 插入数据到 index_studentinfo 表中
        StudentInfo.objects.create(title="zm")
        # 插入数据到 index_userinfo 表中
        UserInfo.objects.create(name="gzh", password="123", age=18)
        ```
    - `删除数据`
        - 语法1: `类名.objects.filter().delete()`：筛选内容，再删除
        - 语法2: `类名.objects.all().delete()`：删除表内全部内容
        ```python
        # 删除 UserInfo 表中 id 为 2 的数据
        UserInfo.objects.filter(id=2).delete()
        # 删除 StudentInfo 表中所有内容
        StudentInfo.objects.all().delete()
        ```
    - `修改数据`
        - 语法1: `类名.objects.all().update()`：修改全部数据
        - 语法2: `类名.objects.filter().update()`：筛选内容，再修改
        ```python
        # 将 UserInfo 表中所有记录的 password 修改为 "123"
        UserInfo.objects.all().update(password="123")
        # 将 UserInfo 表中 id 为 2 的记录的 password 修改为 "1"
        UserInfo.objects.filter(id=2).update(password="1")
        ```
    - `查询数据`
        - 语法1: `类名.objects.all()`：查询表中所有数据
        - 语法2: `类名.objects.filter()`：筛选相应的数据
        - 返回的数据是一个 QuerySet 类型的数据，可以理解为列表，只是每个元素是一个对象。
            ```python
            # 查询 UserInfo 表中所有数据
            all_data = UserInfo.objects.all()
            for obj in all_data:
                print(obj.id, obj.name, obj.password, obj.age)

            # 查询 UserInfo 表中 id 为 1 的数据
            # 返回的结果是一个 QuerySet 列表，可以使用 first() 获取第一个单独的元素
            data = UserInfo.objects.filter(id=1).first()
            print(data.id, data.name, data.password, data.age)

            ```


#### 跨域
- Step 1 
    - `pip install django-cors-headers`
- Step 2 在settings.py中配置
    ```python
    # settings.py

    # 添加 corsheaders 到已安装应用
    INSTALLED_APPS = [
        ...,
        'corsheaders',
        ...,
    ]

    # 添加 corsheaders.middleware.CorsMiddleware 到中间件的顶部
    MIDDLEWARE = [
        'corsheaders.middleware.CorsMiddleware',  # 放在中间件的第一位
        ...,
    ]

    # 设置允许的跨域源
    CORS_ALLOW_ALL_ORIGINS = True  # 允许所有源访问
    # 或者可以指定允许的源
    # CORS_ALLOWED_ORIGINS = [
    #     "http://localhost:8080",  # 你的前端应用URL
    # ]
    ```

## Deloyment 
```bash
Amazon Linux: yum
Ubuntu: apt
# 安全组 SSH22 服务器端口
    类型：Custom SSH
    协议：TCP
    端口范围：22
    来源：0.0.0.0/0

# 安装git
sudo apt update
sudo apt install git -y

# 安装git的包
git clone "url"

# 安装python
sudo yum install python3 -y
sudo apt install python3

# 安装pip
sudo yum install python3-pip -y
sudo apt install python3-pip

# 虚拟环境
sudo apt install python3-venv
python3 -m venv venv

# 每次进入都进入虚拟环境(要在运行上面语句的目录下运行下面语句)
source venv/bin/activate

# 安装包(可选)
# 如果有langchain建议手动安装
pip install -r requirements.txt

# Django 部署
# Django修改settings.py, ALLOWED_HOSTS里面加上服务器公网IP
ALLOWED_HOSTS = ['your-ec2-public-ip', 'localhost']
ALLOWED_HOSTS = ["*"]
# 设置安全组
    类型：Custom TCP
    协议：TCP
    端口范围：8000
    来源：0.0.0.0/0

# Run Django
python3 manage.py runserver 0.0.0.0:8000

# Apache网络服务器
# Install Apache2 package
sudo apt install apache2

# 查看apache2是否正确运行
sudo systemctl status apache2

# 安装npm 
sudo apt install npm
# 安装Vue CLI
sudo npm install -g @vue/cli

# 把`./dist/`文件夹内的内容移动到`/var/www/html`
# 记得把axios的request的ip换成 http://<公有IP>:8000，接入Django
# **重要**: 修改权限
sudo chown -R ubuntu:ubuntu /var/

# 复制：服务器内复制
sudo cp -r /home/ubuntu/Learning-Notes/dist/* /var/www/html/
# 复制：服务器外复制
scp -i /path/to/your-key.pem -r /path/to/your/project/dist/* ubuntu@your-ec2-ip:/var/www/html/

# 安全组设置Https, Http
    类型：Http, Http
    协议：TCP
    端口范围：80, 443
    来源Source：0.0.0.0/0, :/0 (ipv4/ipv6都加上就行)
```

## 后台运行
```bash
# 后台运行代码（记得先弄好环境）
nohup python3 manage.py runserver 0.0.0.0:8000 &

# 查看后台运行代码（先进入文件的目录下）
ps aux | grep manage.py

# 显示
ubuntu 457123
ubuntu 457124

# 删除
kill 457123 457124
```
