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

api.add_resource(RegisterStudent, '/api/register')
api.add_resource(GetCommonStudents, '/api/commonstudents', resource_class_kwargs={'db': mysql})
api.add_resource(SuspendStudent, '/api/suspend')
api.add_resource(GetStudentsForNotification, '/api/retrievefornotifications')

if __name__ == "__main__":
    app.run(debug=True)