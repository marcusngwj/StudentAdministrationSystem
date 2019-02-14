from flask_restful import Resource, reqparse
from flaskext.mysql import MySQL

class SuspendStudent(Resource):
    def __init__(self, db):
        self.db = db

    def post(self):
        conn = self.db.connect()
        cursor = conn.cursor()

        parser = reqparse.RequestParser()
        parser.add_argument('student', type=str, required=True, help='Student is required')
        args = parser.parse_args()

        student = args['student']

        query = ('UPDATE student SET isSuspended=1 WHERE email=%s')
        result = cursor.execute(query, student)
        conn.commit()

        conn.close()
        return ('Success', '204')

    def get(self):
        return "This is strictly a post api"

# TODO: Check if student is in database, else display error