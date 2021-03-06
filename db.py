from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc
from error import CustomError

engine = create_engine('mysql://govtech:password@localhost/database')
Session = sessionmaker(bind=engine)

metadata = MetaData()

teacherTbl = Table('teacher', metadata, autoload=True, autoload_with=engine)
studentTbl = Table('student', metadata, autoload=True, autoload_with=engine)
registerTbl = Table('registers', metadata, autoload=True, autoload_with=engine)

def isTeacherExist(teacher):
    session = Session()
    result = session.query(teacherTbl).filter(teacherTbl.c.email==teacher).first()
    session.close()
    return result is not None if True else False

def isStudentExist(student):
    session = Session()
    result = session.query(studentTbl).filter(studentTbl.c.email==student).first()
    session.close()
    return result is not None if True else False

def insertIntoRegister(teacher, student):
    conn = engine.connect()
    query = registerTbl.insert().values(temail=teacher, semail=student)
    try:
        conn.execute(query)
    except exc.IntegrityError as e:
        raise CustomError(e.code, 'Integrity Error with inserting into register')
    finally:
        conn.close()

def isStudentSuspended(student):
    session = Session()
    result = session.query(studentTbl).filter(studentTbl.c.email==student).filter(studentTbl.c.isSuspended==1).first()
    session.close()
    return result is not None if True else False

def getStudentsUnderTeacher(teacher):
    session = Session()
    result = session.query(registerTbl.c.semail).join(studentTbl, registerTbl.c.semail==studentTbl.c.email).filter(registerTbl.c.temail==teacher).all()
    session.close()
    return [i[0] for i in result]

def getUnsuspendedStudentsRegisteredUnderTeacher(teacher):
    session = Session()
    result = session.query(registerTbl.c.semail).join(studentTbl, registerTbl.c.semail==studentTbl.c.email).filter(registerTbl.c.temail==teacher).filter(studentTbl.c.isSuspended==0).all()
    session.close()
    return [i[0] for i in result]

def suspendStudent(student):
    conn = engine.connect()
    stmt = studentTbl.update().values(isSuspended=1).where(studentTbl.c.email==student)
    conn.execute(stmt)
    conn.close
        