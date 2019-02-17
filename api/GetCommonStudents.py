from flask import request
from flask_restful import Resource

from sqlalchemy import create_engine, MetaData, Table
from db import *

class GetCommonStudents(Resource):
    def get(self):
        teachers = request.args.getlist('teacher')

        if not self.areAllTeacherExist(teachers):
            return ({'message': 'Some teachers do not exist in the database'}, 400) 
        else:
            students = self.getCommonStudentsAmongTeachers(teachers)
            return ({'students':students}, 200)

    def areAllTeacherExist(self, teachers):
        for teacher in teachers:
            if not isTeacherExist(teacher):
                return False
        return True

    def getCommonStudentsAmongTeachers(self, teachers):
        students = set([])
        for i in range(len(teachers)):
            if i==0:
                students = set(getStudentsUnderTeacher(teachers[0]))
            else:
                newGroup = set(getStudentsUnderTeacher(teachers[i]))
                students = students.intersection(newGroup)
        return list(students)
