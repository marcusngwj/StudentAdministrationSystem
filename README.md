## Requirements
1. Have python 3.6.0 installed
2. Install MySQL Database for Windows

## MySQL Database for Windows
Download MYSQL database from https://dev.mysql.com/downloads/installer/ <br>
(mysql-installer-community-8.0.15.0.msi)

Create new user for database<br>
user: govtech <br>
pass: password <br>

I did not use root credentials to prevent possible alteration to tables by restricting the privilleges<br>
Privilleges given: <br>
- [x] Delete
- [x] Insert
- [x] Select
- [x] Show Databases
- [x] Trigger
- [x] Update 

## Setup
1. Run `schema.sql` in the mysql workbench to create tables
2. Enter python's virtual environment (on windows)
    - Make virtual environment: `> virtualenv env`
    - Activate environment: `> env\Scripts\activate.bat`
3. pip install dependencies as shown in `requirements.txt`
4. Update database credentials in the file `db.py`
5. Run app using `python app.py` in the root directory of this project

## Testing
Test cases can be found in `\tests\tests.txt`. 

## Comments
This assignment has been very enriching for me. Given a short span of one week to work on this task amid my external commitments, this assignment has been a great challenge. This is my first time extensively working on the backend and I'm glad to be given this opportunity to work on this task. I had learn to use a new framework because I did not use any in the past. I chose flask because of its simplicity and it was easy to pick up. If I had more time, I would like to learn and implement automatic unit testing.