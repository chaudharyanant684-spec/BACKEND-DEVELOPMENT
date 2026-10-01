from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import date


# =========================
# DATABASE CONNECTION
# =========================

engine = create_engine("sqlite:///students.db")

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


# =========================
# DEPARTMENT MODEL
# =========================

class Department(Base):

    __tablename__ = "departments"

    id = Column(Integer, primary_key=True)

    name = Column(
        String(100),
        unique=True,
        nullable=False
    )

    students = relationship(
        "Student",
        back_populates="department"
    )

    courses = relationship(
        "Course",
        back_populates="department"
    )


# =========================
# STUDENT MODEL
# =========================

class Student(Base):

    __tablename__ = "students"

    id = Column(Integer, primary_key=True)

    name = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(100),
        unique=True,
        nullable=False
    )

    branch = Column(String(50))

    enrollment_date = Column(Date)

    department_id = Column(
        Integer,
        ForeignKey("departments.id")
    )

    department = relationship(
        "Department",
        back_populates="students"
    )

    enrollments = relationship(
        "Enrollment",
        back_populates="student"
    )


# =========================
# COURSE MODEL
# =========================

class Course(Base):

    __tablename__ = "courses"

    id = Column(
        String(10),
        primary_key=True
    )

    title = Column(
        String(100),
        nullable=False
    )

    credits = Column(
        Integer,
        nullable=False
    )

    department_id = Column(
        Integer,
        ForeignKey("departments.id")
    )

    department = relationship(
        "Department",
        back_populates="courses"
    )

    enrollments = relationship(
        "Enrollment",
        back_populates="course"
    )


# =========================
# ENROLLMENT MODEL
# =========================

class Enrollment(Base):

    __tablename__ = "enrollments"

    student_id = Column(
        Integer,
        ForeignKey("students.id"),
        primary_key=True
    )

    course_id = Column(
        String(10),
        ForeignKey("courses.id"),
        primary_key=True
    )

    semester = Column(String(20))

    grade = Column(String(2))

    student = relationship(
        "Student",
        back_populates="enrollments"
    )

    course = relationship(
        "Course",
        back_populates="enrollments"
    )


# =========================
# CREATE TABLES
# =========================

Base.metadata.create_all(engine)

print("All tables created successfully!")


# =========================
# CREATE DEPARTMENT
# =========================

department = session.query(Department).filter_by(
    name="Computer Science"
).first()

if not department:

    department = Department(
        name="Computer Science"
    )

    session.add(department)
    session.commit()

    print("Department created successfully!")

else:

    print("Department already exists.")


# =========================
# CREATE STUDENT
# =========================

student = session.query(Student).filter_by(
    email="aarav@upes.ac.in"
).first()

if not student:

    student = Student(
        name="Aarav",
        email="aarav@upes.ac.in",
        branch="CSE",
        enrollment_date=date(2026, 10, 1),
        department_id=department.id
    )

    session.add(student)
    session.commit()

    print("Student created successfully!")

else:

    print("Student already exists.")


# =========================
# READ STUDENTS
# =========================

print("\n--- READ ---")

students = session.query(Student).filter(
    Student.branch == "CSE"
).all()

print("CSE Students:")

for student in students:

    print(
        "ID:", student.id,
        "| Name:", student.name,
        "| Email:", student.email,
        "| Branch:", student.branch
    )


# =========================
# UPDATE STUDENT
# =========================

print("\n--- UPDATE ---")

student = session.query(Student).filter_by(
    email="aarav@upes.ac.in"
).first()

if student:

    student.branch = "ECE"

    session.commit()

    print(
        "Student branch updated successfully!"
    )

    print(
        "New branch:",
        student.branch
    )

else:

    print("Student not found.")


# =========================
# READ AFTER UPDATE
# =========================

print("\n--- AFTER UPDATE ---")

student = session.query(Student).filter_by(
    email="aarav@upes.ac.in"
).first()

if student:

    print(
        "Name:", student.name,
        "| Branch:", student.branch
    )


# =========================
# DELETE STUDENT
# =========================

print("\n--- DELETE ---")

student = session.query(Student).filter_by(
    email="aarav@upes.ac.in"
).first()

if student:

    session.delete(student)

    session.commit()

    print("Student deleted successfully!")

else:

    print("Student not found.")


# =========================
# VERIFY DELETE
# =========================

print("\n--- VERIFY DELETE ---")

student = session.query(Student).filter_by(
    email="aarav@upes.ac.in"
).first()

if student:

    print("Student still exists.")

else:

    print("Student does not exist in database.")