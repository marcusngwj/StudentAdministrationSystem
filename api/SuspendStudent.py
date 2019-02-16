from flask_restful import Resource, reqparse
from flaskext.mysql import MySQL
from db import *

class SuspendStudent(Resource):
    def __init__(self, db):
        self.db = db

    def post(self):
        # Parse argument from request
        args = self.getArgsFromRequest()
        student = args['student']

        if isStudentExist(self.db, student):
            suspendStudent(self.db, student)
            return ('Success', '204')
        else:
            return ({'message': 'Student does not exist'}, 400)

    def get(self):
        return "This is strictly a post api"

    def getArgsFromRequest(self):
        parser = reqparse.RequestParser()
        parser.add_argument('student', type=str, required=True, help='Student is required')
        args = parser.parse_args()
        return args