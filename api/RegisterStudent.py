from flask_restful import Resource, reqparse
from db import *
from error import CustomError

class RegisterStudent(Resource):
    def post(self):
        # Parse argument from request
        args = self.getArgsFromRequest()
        teacher = args['teacher']
        students = args['students']

        if not isTeacherExist(teacher):
            return ({'message': 'Teacher does not exist in the database'}, 400)

        elif students is None or len(students) < 1:
            return ({'message':'There are no students selected'}, 400)

        elif self.areAllStudentExist(students):
            try:
                self.registerStudents(teacher, students)
                return ('Success', '204')
            except CustomError as e:
                return ({'message': e.toString()}, 400)            
        else:
            return ({'message': 'Some students do not exist in the database'}, 400) 

    def getArgsFromRequest(self):
        parser = reqparse.RequestParser()
        parser.add_argument('teacher', type=str, required=True, help='Invalid Format - Teacher is missing')
        parser.add_argument('students', action='append', help='Invalid Format - Students are missing')
        args = parser.parse_args()
        return args

    def areAllStudentExist(self, students):
        for student in students:
            if not isStudentExist(student):
                return False
        return True

    def registerStudents(self, teacher, students):
        for student in students:
            insertIntoRegister(teacher, student)
            