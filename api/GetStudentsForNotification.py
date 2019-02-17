from flask_restful import Resource, reqparse
import re
from db import *

class GetStudentsForNotification(Resource):
    def post(self):
        # Parse argument from request
        args = self.getArgsFromRequest()
        teacher = args['teacher']
        notiMsg = args['notification']

        if isTeacherExist(teacher):
            allStudents = []

            # Extract students that are mentioned in the notification and not suspended
            studentsInMention = self.extractEmailFromString(notiMsg)
            studentsInMention = self.getUnsuspendedStudents(studentsInMention)

            # Get all unsuspended students registered under the teacher
            regStudents = getUnsuspendedStudentsRegisteredUnderTeacher(teacher)

            #Merge results and remove duplicates
            recipients = list(set(regStudents + studentsInMention))
            
            return ({'recipients': recipients}, 200)
        else:
            return ({'message': 'Teacher is missing. Please include a teacher'}, 400)

    def getArgsFromRequest(self):
        parser = reqparse.RequestParser()
        parser.add_argument('teacher', type=str, required=True, help='Invalid Format - Teacher is required to post a message')
        parser.add_argument('notification', type=str, required=True, help='Invalid Format - Notification is required to post a message')
        args = parser.parse_args()
        return args

    def extractEmailFromString(self, string):
        mentionedPatternStr = '@(?:[a-z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)*|"(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\\])'
        p = re.compile(mentionedPatternStr)
        return [x[1:] for x in p.findall(string)] # Remove @ from email

    def getUnsuspendedStudents(self, allStudents):
        result = []
        for student in allStudents:
            if not isStudentSuspended(student):
                result.append(student)
        return result