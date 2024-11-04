# Full-Stack Enginnering
## Frontend

### 1) Vue
```bash
# 运行
npm rum build

```

### 2) Angular

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

# 每次进入都进入虚拟环境
source venv/bin/activate

# 安装包(可选)
# 如果有langchain建议手动安装
pip install -r requirements.txt

# Apache网络服务器
# Install Apache2 package
sudo apt install apache2

# After the Apache installation process, the web server service should be started automatically, you can check if it is up and running with the following command.
sudo systemctl status apache2

# 安装npm 
sudo apt install npm

# 安装Vue CLI
sudo npm install -g @vue/cli

# 先进入vue目录，再
npm install

# 再vue目录构建./dist
npm run build

# 把`./dist/`文件夹内的内容移动到`/var/www/html`
scp -i /path/to/your-key.pem -r /path/to/your/project/dist/* ubuntu@your-ec2-ip:/var/www/html/

sudo chmod -R 775 /var/www/
sudo chown -R ubuntu:ubuntu /var/www

sudo cp -r /home/ubuntu/Learning-Notes/dist/* /var/www/html/
```