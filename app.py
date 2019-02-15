from flask import Flask, jsonify
from flask_restful import Resource, Api
from flaskext.mysql import MySQL

from api.RegisterStudent import RegisterStudent
from api.GetCommonStudents import GetCommonStudents
from api.SuspendStudent import SuspendStudent
from api.GetStudentsForNotification import GetStudentsForNotification

app = Flask(__name__)

mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'govtech'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'database'

mysql.init_app(app)

api = Api(app)


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
api.add_resource(SuspendStudent, '/api/suspend', resource_class_kwargs={'db': mysql})
api.add_resource(GetStudentsForNotification, '/api/retrievefornotifications', resource_class_kwargs={'db': mysql})

if __name__ == "__main__":
    app.run(debug=True)