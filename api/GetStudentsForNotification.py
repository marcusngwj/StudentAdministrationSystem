from flask_restful import Resource, reqparse
from flaskext.mysql import MySQL
import re

class GetStudentsForNotification(Resource):
    def __init__(self, db):
        self.db = db

    def post(self):
        conn = self.db.connect()
        cursor = conn.cursor()

        parser = reqparse.RequestParser()
        parser.add_argument('teacher', type=str, required=True, help='Teacher is required')
        parser.add_argument('notification', type=str)
        args = parser.parse_args()

        teacher = args['teacher']
        notiMsg = args['notification']

        mentionedPatternStr = '@(?:[a-z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)*|"(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\\])'
        p = re.compile(mentionedPatternStr)
        studentsInMention = p.findall(notiMsg)

        query = ('SELECT semail FROM registers WHERE temail=%s')
        cursor.execute(query, teacher)
        regStudents = [x[0] for x in cursor.fetchall()]

        receivingStudents = set(regStudents + [x[1:] for x in studentsInMention])

        print(receivingStudents)


        conn.close()
        return ('Success', '204')

    def get(self):
        return "This is strictly a post api"