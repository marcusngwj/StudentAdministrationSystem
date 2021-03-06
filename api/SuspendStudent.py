from flask_restful import Resource, reqparse
from db import *

class SuspendStudent(Resource):
    def post(self):
        # Parse argument from request
        args = self.getArgsFromRequest()
        student = args['student']

        if isStudentExist(student):
            suspendStudent(student)
            return ('Success', '204')
        else:
            return ({'message': 'Student does not exist'}, 400)

    def getArgsFromRequest(self):
        parser = reqparse.RequestParser()
        parser.add_argument('student', type=str, required=True, help='Invalid Format - Student is required')
        args = parser.parse_args()
        return args