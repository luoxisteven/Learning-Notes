## 快捷键
```
"command + shift + ." 查看隐藏文件
```

## Terminal
```bash
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
# Pull 从远程仓库获取最新的更改，并与本地分支进行合并。
# 它相当于执行了两个操作的组合：
# git fetch（从远程仓库获取最新的更新）和 git merge（将这些更新合并到当前分支）。
git pull origin main  # 从远程仓库的 main 分支拉取最新更改并合并

# 用于切换分支或恢复文件状态的命令
git checkout feature-branch  # 切换到 feature-branch 分支

# 强制回滚
# Step 1 切换到分支
git checkout main
# Step 2 log 查看回滚的commit id
git log 
## Step 3 强制退回 到某个 commit id
git reset --hard "commit_id"
# 例如
git reset --hard 71181c3bb0d4c5701dbfead5c531875bc8754130

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
git push -u origin main --force x
```

### 4) Remote
```bash
# 查看远程仓库
git remote -v

# 修改远程仓库
git remote set-url origin "url"
git remote set-url origin git@github.com:luoxisteven/Learning-Notes.git
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
