from flask import Flask, jsonify
from flask_restful import Resource, Api
from flaskext.mysql import MySQL

from api.RegisterStudent import RegisterStudent
from api.GetCommonStudents import GetCommonStudents

app = Flask(__name__)

mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'govtech'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'database'

mysql.init_app(app)

api = Api(app)


# cursor.execute("SELECT * from teacher")
# data = cursor.fetchone()


first = {
    "teacher": "teacherken@gmail.com",
    "students":
        [
            "studentjon@gmail.com",
            "studenthon@gmail.com"
        ]
}

# Success 204
# @app.route("/api/register", methods=['GET', 'POST'])
# def register():
#     conn = mysql.connect()
#     cursor = conn.cursor()

#     query = ('INSERT INTO registers(temail, semail) VALUES (%s, %s)')
#     data1 = ('teacherken@gmail.com', 'studentjon@gmail.com')
#     data2 = ('teacherken@gmail.com', 'studenthon@gmail.com')
#     result = cursor.execute(query, data1)
#     result = cursor.execute(query, data2)
#     conn.commit()

#     cursor.execute("SELECT * from registers")
#     res = cursor.fetchall()
#     print(res)
#     conn.close()
#     return "ccc"

# Success 200
# @app.route("/api/commonstudents", methods=['GET'])
# def get_common_students():
#     conn = mysql.connect()
#     cursor = conn.cursor()
#     cursor.execute("SELECT * from registers")
#     res = cursor.fetchall()
#     print(res)
#     conn.close()
#     return "common_students"















@app.route("/hello")
def hello():
    print(data)
    return "Hello World!"

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})








api.add_resource(RegisterStudent, '/api/register', resource_class_kwargs={'db': mysql})
api.add_resource(GetCommonStudents, '/api/commonstudents', resource_class_kwargs={'db': mysql})

if __name__ == "__main__":
    app.run(debug=True)