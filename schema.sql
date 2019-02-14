CREATE SCHEMA `database` ;

CREATE TABLE teacher (
    email VARCHAR(256) PRIMARY KEY
);

CREATE TABLE student (
    email VARCHAR(256) PRIMARY KEY,
    isSuspended TINYINT DEFAULT 0 NOT NULL CHECK(isSuspended=0 OR isSuspended=1)
);

CREATE TABLE registers (
    temail VARCHAR(256) REFERENCES teacher(email),
    semail VARCHAR(256) REFERENCES student(email),
    PRIMARY KEY (temail, semail)
)

INSERT INTO teacher(`email`) VALUES('teacheralice@gmail.com');
INSERT INTO teacher(`email`) VALUES('teacherbob@gmail.com');
INSERT INTO teacher(`email`) VALUES('teachercharlie@gmail.com');
INSERT INTO teacher(`email`) VALUES('teacherdonald@gmail.com');
INSERT INTO teacher(`email`) VALUES('teachereve@gmail.com');
INSERT INTO teacher(`email`) VALUES('teacherfelicia@gmail.com');
INSERT INTO teacher(`email`) VALUES('teachergrace@gmail.com');
INSERT INTO teacher(`email`) VALUES('teacherhelen@gmail.com');
INSERT INTO teacher(`email`) VALUES('teacherivy@gmail.com');
INSERT INTO teacher(`email`) VALUES('teacherjeremy@gmail.com');
INSERT INTO teacher(`email`) VALUES('teacherken@gmail.com');
INSERT INTO teacher(`email`) VALUES('teacher_only_one_student@gmail.com');
INSERT INTO teacher(`email`) VALUES('teacher_no_student@gmail.com');
INSERT INTO teacher(`email`) VALUES('teacher1_with_common_student1@gmail.com');
INSERT INTO teacher(`email`) VALUES('teacher2_with_common_student1@gmail.com');
INSERT INTO teacher(`email`) VALUES('teacher1_with_common_student2@gmail.com');
INSERT INTO teacher(`email`) VALUES('teacher2_with_common_student2@gmail.com');

INSERT INTO student(`email`) VALUES('studentagnes@gmail.com');
INSERT INTO student(`email`) VALUES('studentbernard@gmail.com');
INSERT INTO student(`email`) VALUES('studentbob@gmail.com');
INSERT INTO student(`email`) VALUES('studentcharles@gmail.com');
INSERT INTO student(`email`) VALUES('studentdanial@gmail.com');
INSERT INTO student(`email`) VALUES('studentelvin@gmail.com');
INSERT INTO student(`email`) VALUES('studentfrancis@gmail.com');
INSERT INTO student(`email`) VALUES('studentgeorge@gmail.com');
INSERT INTO student(`email`) VALUES('studentgrace@gmail.com');
INSERT INTO student(`email`) VALUES('studenthon@gmail.com');
INSERT INTO student(`email`) VALUES('studentiris@gmail.com');
INSERT INTO student(`email`) VALUES('studentjon@gmail.com');
INSERT INTO student(`email`) VALUES('studentkelly@gmail.com');
INSERT INTO student(`email`) VALUES('studentlyon@gmail.com');
INSERT INTO student(`email`) VALUES('studentmary@gmail.com');
INSERT INTO student(`email`) VALUES('studentmiche@gmail.com');
INSERT INTO student(`email`) VALUES('studentnatalie@gmail.com');
INSERT INTO student(`email`) VALUES('studentolivia@gmail.com');
INSERT INTO student(`email`) VALUES('studentpatrick@gmail.com');
INSERT INTO student(`email`) VALUES('studentqueen@gmail.com');
INSERT INTO student(`email`) VALUES('studentrandell@gmail.com');
INSERT INTO student(`email`) VALUES('studentroman@gmail.com');
INSERT INTO student(`email`) VALUES('studentsandy@gmail.com');
INSERT INTO student(`email`) VALUES('studentsarah@gmail.com');
INSERT INTO student(`email`) VALUES('studentthomas@gmail.com');
INSERT INTO student(`email`) VALUES('studenttimothy@gmail.com');
INSERT INTO student(`email`) VALUES('studentumar@gmail.com');
INSERT INTO student(`email`) VALUES('studentvalerie@gmail.com');
INSERT INTO student(`email`) VALUES('studentwendy@gmail.com');
INSERT INTO student(`email`) VALUES('studentxavier@gmail.com');
INSERT INTO student(`email`) VALUES('studentyvonne@gmail.com');
INSERT INTO student(`email`) VALUES('studentzachary@gmail.com');
INSERT INTO student(`email`) VALUES('studentzander@gmail.com');
INSERT INTO student(`email`) VALUES('studentzeus@gmail.com');
INSERT INTO student(`email`) VALUES('studentzion@gmail.com');
INSERT INTO student(`email`) VALUES('commonstudent1@gmail.com');
INSERT INTO student(`email`) VALUES('commonstudent2@gmail.com');
INSERT INTO student(`email`) VALUES('student_only_under_teacher_ken@gmail.com');
INSERT INTO student(`email`) VALUES('student_no_teacher@gmail.com');

INSERT INTO registers(`temail`, `semail`) VALUES ('teacherken@gmail.com', 'student_only_under_teacher_ken@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teacherken@gmail.com', 'studentagnes@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teacherken@gmail.com', 'studentbob@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teacherken@gmail.com', 'studentcharles@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teacheralice@gmail.com', 'studentdanial@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teacheralice@gmail.com', 'studentelvin@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teacheralice@gmail.com', 'studentfrancis@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teacherbob@gmail.com', 'studentgeorge@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teacherbob@gmail.com', 'studenthon@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teacherbob@gmail.com', 'studentiris@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teachercharlie@gmail.com', 'studentjon@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teachercharlie@gmail.com', 'studentkelly@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teachercharlie@gmail.com', 'studentlyon@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teacherdonald@gmail.com', 'studentmary@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teacherdonald@gmail.com', 'studentmiche@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teacherdonald@gmail.com', 'studentnatalie@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teachereve@gmail.com', 'studentolivia@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teachereve@gmail.com', 'studentpatrick@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teachereve@gmail.com', 'studentqueen@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teacherfelicia@gmail.com', 'studentrandell@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teacherfelicia@gmail.com', 'studentsandy@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teacherfelicia@gmail.com', 'studentthomas@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teachergrace@gmail.com', 'studentumar@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teachergrace@gmail.com', 'studentvalerie@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teachergrace@gmail.com', 'studentwendy@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teacherhelen@gmail.com', 'studentxavier@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teacherhelen@gmail.com', 'studentyvonne@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teacherhelen@gmail.com', 'studentzachary@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teacherivy@gmail.com', 'studentzander@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teacherivy@gmail.com', 'studenttimothy@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teacherjeremy@gmail.com', 'studentgrace@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teacherjeremy@gmail.com', 'studentsarah@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teacherjeremy@gmail.com', 'studentbernard@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teacher_only_one_student@gmail.com', 'studentzion@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teacher1_with_common_student1@gmail.com', 'commonstudent1@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teacher1_with_common_student1@gmail.com', 'studentzeus@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teacher2_with_common_student1@gmail.com', 'commonstudent1@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teacher2_with_common_student1@gmail.com', 'studentroman@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teacher1_with_common_student2@gmail.com', 'commonstudent2@gmail.com');
INSERT INTO registers(`temail`, `semail`) VALUES ('teacher2_with_common_student2@gmail.com', 'commonstudent2@gmail.com');
