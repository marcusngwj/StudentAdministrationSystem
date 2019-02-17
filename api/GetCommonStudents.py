from flask import request
from flask_restful import Resource
from flaskext.mysql import MySQL

from sqlalchemy import create_engine, MetaData, Table
from db import *

class GetCommonStudents(Resource):
    def __init__(self, db):
        self.db = db

    def get(self):
        # conn = self.db.connect()
        # cursor = conn.cursor()

        teachers = request.args.getlist('teacher')

        print(getUSRT('teacherken@gmail.com'))

        # abc = getCommonStudentFromTeachers(teachers)

        # print(abc)


        # conn.close()
        return "66"
