from flaskext.mysql import MySQL

def isTeacherExist(database, teacher):
    conn = database.connect()
    cursor = conn.cursor()
    query = ('SELECT 1 FROM teacher WHERE email=%s')
    cursor.execute(query, teacher)
    result = cursor.fetchone() is not None if True else False
    conn.close()
    return result

def isStudentExist(database, student):
    conn = database.connect()
    cursor = conn.cursor()
    query = ('SELECT 1 FROM student WHERE email=%s')
    cursor.execute(query, student)
    result = cursor.fetchone() is not None if True else False
    conn.close()
    return result

def isStudentSuspended(database, student):
    conn = database.connect()
    cursor = conn.cursor()
    query = ('SELECT 1 FROM student WHERE email=%s AND isSuspended=1')
    cursor.execute(query, student)
    result = cursor.fetchone() is not None if True else False
    conn.close()
    return result

def getUnsuspendedStudentsRegisteredUnderTeacher(database, teacher):
    conn = database.connect()
    cursor = conn.cursor()
    query = ('SELECT r.semail FROM registers r, student s WHERE r.semail=s.email AND r.temail=%s AND s.isSuspended!=1')
    cursor.execute(query, teacher)
    conn.close()
    return [x[0] for x in cursor.fetchall()]

def suspendStudent(database, student):
    conn = database.connect()
    cursor = conn.cursor()
    query = ('UPDATE student SET isSuspended=1 WHERE email=%s')
    result = cursor.execute(query, student)
    conn.commit()
    conn.close()