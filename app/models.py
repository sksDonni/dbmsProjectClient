from app import db

class Department(db.Model):
  dept_id = db.Column(db.Integer, primary_key = True)
  dept_budget = db.Column(db.Integer)
  name = db.Column(db.String(64), nullable=False)
  instructors = db.relationship('Instructor', backref='instructors', lazy='dynamic')

class Instructor(db.Model):
  instructor_id = db.Column(db.Integer, primary_key=True)
  instructor_name = db.Column(db.String(64), nullable=False)
  salary = db.Column(db.Integer)
  dept_id = db.Column(db.Integer, db.ForeignKey('department.dept_id'), nullable=False)
  teaches = db.relationship('Course', backref='courses', lazy='dynamic')

class Section(db.Model):
  section_id = db.Column(db.Integer, primary_key=True)
  semester = db.Column(db.Integer)
  year = db.Column(db.Integer)

class Student(db.Model):
  student_id = db.Column(db.Integer, primary_key=True)
  student_name = db.Column(db.String(64), nullable=False)
  credits = db.Column(db.Integer, nullable=False)
  dept_id = db.Column(db.Integer, db.ForeignKey('department.dept_id'), nullable=False)
  sec_id = db.Column(db.Integer, db.ForeignKey('section.section_id'), nullable=False)

class Course(db.Model):
  course_id = db.Column(db.Integer, primary_key=True)
  course_title = db.Column(db.String(64))
  course_credits = db.Column(db.Integer)
  dept_id = db.Column(db.Integer, db.ForeignKey('department.dept_id'))
  course_tutor = db.Column(db.Integer, db.ForeignKey('instructor.instructor_id'))


