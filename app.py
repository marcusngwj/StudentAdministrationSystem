from flask import Flask
from flask_restful import Resource, Api

from api.RegisterStudent import RegisterStudent
from api.GetCommonStudents import GetCommonStudents
from api.SuspendStudent import SuspendStudent
from api.GetStudentsForNotification import GetStudentsForNotification

app = Flask(__name__)
api = Api(app)

api.add_resource(RegisterStudent, '/api/register')
api.add_resource(GetCommonStudents, '/api/commonstudents')
api.add_resource(SuspendStudent, '/api/suspend')
api.add_resource(GetStudentsForNotification, '/api/retrievefornotifications')

if __name__ == "__main__":
    app.run(debug=True)