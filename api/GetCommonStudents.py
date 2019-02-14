from flask import request
from flask_restful import Resource
from flaskext.mysql import MySQL

class GetCommonStudents(Resource):
    def __init__(self, db):
        self.db = db

    def get(self):
        conn = self.db.connect()
        cursor = conn.cursor()

        teachers = request.args.getlist('teacher')

        print(teachers)
        

        conn.close()
        return "66"
