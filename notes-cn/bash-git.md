# Bash

## 常用命令
``` bash
# Server
# Package update
sudo apt upgrade

# Chinese Regex
[\u4e00-\u9fff]

# Discard all
git restore .
git checkout -- .
# Create a new branch and switch it
git checkout -b <new-branch-name>
# Create a new branch without switching to it
git branch <new-branch-name>
# Remove Tracking
git rm -r --cached .

# Remote Repo
git remote -v
# Add new remote repo
git remote add origin <repo_address>
# Update remote repo
git remote set-url origin <repo_address>
```

## 部署
```bash
# Virtrual Enviornment
source venv/bin/activate
# See nohup background
ps aux | grep dotnet
# Kill background
kill -9 118590 118683
# Run Background and Log
nohup dotnet run >> output.log 2>&1 &

# Dotnet Release
dotnet publish -c Release
cd bin/Release/net8.0
dotnet dotnet_back.dll
nohup dotnet dotnet_back.dll >> output.log 2>&1 &
```

## 快捷键
```bash
"Command + C" 复制
"Command + V" 粘贴
"Option + Command + V" 剪切
"Command + Shift + ." 查看隐藏文件
```

## Terminal
```bash
# 当在终端里进入带有空格的文件夹，需要加上"\"转义符
cd Coding\ Questions

# 显示目前路径
pwd

# 创建目录
mkdir test

# 进入目录
cd test

# 返回上一级目录
cd ..

# 返回上两级目录
cd ../..

# 查看目录下的文件
ls 

# 删除’file1’⽂件
rm -f file1

# 删除’dir1’⽬录
rmdir dir1

# 删除文件夹和文件夹内所有内容
rm -rf folder_name

# 中断执行
control(^) + c 
```

## Git
### 1) 初始化 Git
```bash
cd /path/to/your/project    # 进入项目目录
git init                    # 初始化 Git 仓库

git add .                   # 添加所有文件

git commit -m "Initial commit"  # 提交，并添加提交信息

git remote add origin git@github.com:luoxisteven/knowledge_base.git

git push -u origin main
```

### 2) Pull 回滚
``` bash
# Pull最新的
git pull origin main

# 切换分支
# 把现有修改都删掉
git restore .
git checkout -- .
# or 把现有修改都保存
git stash
# 用于切换分支或恢复文件状态的命令
git checkout feature-branch  # 切换到 feature-branch 分支

# Pull 从远程仓库获取最新的更改，并与本地分支进行合并。
# 它相当于执行了两个操作的组合：
# git fetch（从远程仓库获取最新的更新）和 git merge（将这些更新合并到当前分支）。
git pull origin feature-branch  # 从远程仓库的 feature-branch 分支拉取最新更改并合并


# 强制回滚
# Step 1 切换到分支
git checkout main
# Step 2 log 查看回滚的commit id
git log 
## Step 3 强制退回 到某个 commit id
git reset --hard "commit_id"
# 例如
git reset --hard 71181c3bb0d4c5701dbfead5c531875bc8754130
# Step 4 删除那些未跟踪的文件
git clean -fd

# 如果强制回滚不行试试
git fetch --all
```

### 3) 普通Push
```bash
# 简单 push
# add：将文件添加到缓存区
git add .
# commit：提交到本地仓库
git commit -m "***"
git push origin main

# Force push
git push -u origin main --force
```

### 4) Remote
```bash
# 查看远程仓库
git remote -v

# 修改远程仓库
git remote set-url origin "url"
git remote set-url origin git@github.com:addaxis/POC-RFP-Automation.git
```

### 5) 用户名和邮箱
```bash
# 查看
git config --global user.name
git config --global user.email

# 设置
git config --global user.name "luoxisteven"
git config --global user.email "429066012@qq.com"
```

### 6) Log
```bash
git log
```

### 7) Requirements.txt
```bash
# Freeze
pip freeze > requirements.txt

# 生成没版本号的
pip freeze | awk -F '==' '{print $1}' > requirements.txt
pip freeze | sed 's/==.*//' > requirements.txt

# Install requirements
pip install -r requirements.txt
```
### 8) 重做gitignore
```bash
git rm -r --cached .
git add .
```

### 9) Branch
```bash
# Create a new branch and switch it
git checkout -b <new-branch-name>

# Create a new branch without switching to it
git branch <new-branch-name>
```

### 10) Repo Address
```bash
# Lookup Remote Repo Address
git remote -v

# Add Remote Repo Address
git remote add origin <repo_address>

# Change Remote Repo Address
git remote set-url origin <repo_address>
```
