## Shortcut
``` bash
"Command + C" Copy 
"Command + V" Paste 
"Option + Command + V" Cut 
"Command + Shift + ." Show hidden files
```


## Terminal
```bash
# For " " in filename
cd Coding\ Questions

# Display current path
pwd

# Create a directory
mkdir test

# Enter a directory
cd test

# Go back to the parent directory
cd ..

# Go back two levels
cd ../..

# List files in the directory
ls 

# Delete the file 'file1'
rm -f file1

# Delete the directory 'dir1'
rmdir dir1

# Delete a folder and its contents
rm -rf folder_name

# Interrupt execution
control(^) + c 


## Git
### 1) Initialize Git
```bash
cd /path/to/your/project    # Navigate to the project directory
git init                    # Initialize the Git repository

git add .                   # Stage all files

git commit -m "Initial commit"  # Commit with a message

git remote add origin git@github.com:luoxisteven/knowledge_base.git

git push -u origin main

```

### 2) Pull and Reset
``` bash
# Pull fetches the latest changes from the remote repository and merges them with the current branch.
# It's equivalent to running:
# git fetch (fetch updates) + git merge (merge updates).
git pull origin main  # Pull and merge changes from the main branch

# Discard all 
git restore .

# Save all
git stash

# Commands for switching branches or restoring file states
git checkout feature-branch  # Switch to the feature-branch branch

# Force reset
# Step 1: Switch to the branch
git checkout main
# Step 2: Use log to find the commit ID to roll back to
git log 
# Step 3: Force reset to a specific commit ID
git reset --hard "commit_id"
# Example:
git reset --hard 71181c3bb0d4c5701dbfead5c531875bc8754130
# Step 4 删除那些未跟踪的文件
git clean -fd

# If force reset doesn’t work, try:
git fetch --all
```

### 3) Standard Push
```bash
# Simple push
# add: Stage files
git add .
# commit: Commit to the local repository
git commit -m "***"
git push origin main

# Force push
git push -u origin main --force
```

### 4) Remote Repository
```bash
# View remote repository
git remote -v

# Modify the remote repository
git remote set-url origin "url"
git remote set-url origin git@github.com:addaxis/POC-RFP-Automation.git
```

### 5) Username and Email
```bash
# View
git config --global user.name
git config --global user.email

# Set
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

#  Generate a requirements.txt without version numbers
pip freeze | awk -F '==' '{print $1}' > requirements.txt
pip freeze | sed 's/==.*//' > requirements.txt

# Install requirements
pip install -r requirements.txt
```


### 8) Redo gitignore
```bash
git rm -r --cached .
git add .
```