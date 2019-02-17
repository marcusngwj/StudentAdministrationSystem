### Make virtual environment
\> virtualenv env

### Activate virtual environment
\> env\Scripts\activate.bat

### Deactivate virtual environment
\> deactivate

# MySQL Database for Windows

Download MYSQL database from https://dev.mysql.com/downloads/installer/ <br>
(mysql-installer-community-8.0.15.0.msi)

create new user for database, dont use root <br>
user: govtech <br>
pass: password <br>

restrict the permission <br>
Privilleges: <br>
- [x] Delete
- [x] Insert
- [x] Select
- [x] Show Databases
- [x] Trigger
- [x] Update 

pip install mysqlclient==1.3.12