from flask_restful import Resource, reqparse
from flaskext.mysql import MySQL

class RegisterStudent(Resource):
    def __init__(self, db):
        self.db = db

    def post(self):
        conn = self.db.connect()
        cursor = conn.cursor()

        parser = reqparse.RequestParser()
        parser.add_argument('teacher', type=str, required=True, help='Teacher is required')
        parser.add_argument('students', action='append')
        args = parser.parse_args()

        teacher = args['teacher']
        students = args['students']

        for student in students:
            query = ('INSERT INTO registers(temail, semail) VALUES (%s, %s)')
            data = (teacher, student)
            result = cursor.execute(query, data)
            conn.commit()

        conn.close()
        return ('Success', '204')

    def get(self):
        return "This is strictly a post api"