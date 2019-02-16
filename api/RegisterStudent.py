from flask_restful import Resource, reqparse
from flaskext.mysql import MySQL
from db import *

class RegisterStudent(Resource):
    def __init__(self, db):
        self.db = db

    def post(self):
        # Parse argument from request
        args = self.getArgsFromRequest()
        teacher = args['teacher']
        students = args['students']

        if not isTeacherExist(self.db, teacher):
            return ({'message': 'Teacher does not exist in the database'}, 400)

        elif self.areAllStudentExist(students):
            insertIntoRegister(self.db, teacher, student)
            return ('Success', '204')
            
        else:
            return ({'message': 'Some students do not exist in the database'}, 400) 

    def get(self):
        return "This is strictly a post api"

    def getArgsFromRequest(self):
        parser = reqparse.RequestParser()
        parser.add_argument('teacher', type=str, required=True, help='Invalid Format: Teacher is missing')
        parser.add_argument('students', action='append', help='Invalid Format: Students are missing')
        args = parser.parse_args()
        return args

    def areAllStudentExist(self, students):
        for student in students:
            if not isStudentExist(self.db, student):
                return False
        return True