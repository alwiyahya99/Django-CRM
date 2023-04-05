# Install Mysql on your computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

# git config --global user.name "a.........9"
# git config --global user.email "a.........@gmail.com"
# git config --global push.default matching
# git config --global alias.co checkout
# git init
# git add .
# git commit -am 'Initial Commint'
# git remote add origin https://github.com/alwiyahya99/Django-CRM.git
# git branch -M main
# git push -u origin main


import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost', 
    user = 'root',
    password = ''
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE eldero")

print("All done")