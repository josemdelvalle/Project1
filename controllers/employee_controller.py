from werkzeug.utils import redirect

from models.employee_credentials import EmployeeCredentials
from services.employee_service_impl import EmployeeServiceImpl
from flask import jsonify, request
from services.course_service_impl import CourseServiceImpl
from models.course import Course
import logging


def route(app):
    @app.route("/login", methods=['POST'])
    def login():
        try:
            user_name = request.json['userName']
            password = request.json['password']
            response = EmployeeServiceImpl.authenticate_employee(user_name, password)
            if type(response) == EmployeeCredentials:
                if password == response.password and user_name == response.user_name:
                    employee = EmployeeServiceImpl.get_employee_by_id(response.employee_id)
                    employee.role = EmployeeServiceImpl.get_employee_role(response.employee_id)
                    return jsonify(employee.json()), 200
            return jsonify("Invalid user name or password ctr"), 400
        except Exception as e:
            return jsonify("Invalid user name or password ccccc"), 400

    @app.route("/addCourse", methods=['POST'])
    def add_course():
        try:
            try:
                if not request.json['employeeId']:
                    raise Exception
            except Exception as e:
                return jsonify("Need to log in"), 400

            new_course = Course.json_parse(request.json)
            return jsonify(CourseServiceImpl.add_course(new_course))
        except Exception as e:
            return jsonify("Invalid Input"), 400

    @app.route("/getCourses", methods=['POST'])
    def get_courses():
        try:
            try:
                if not request.json['employeeId']:
                    raise Exception
            except Exception as e:
                return jsonify("Need to log in"), 400
            employee_id = request.json['employeeId']
            role = request.json['role']
            department = request.json['department']
            response = CourseServiceImpl.get_all_courses(employee_id, role, department)
            print(response)
            return jsonify(response), 200

        except Exception as e:
            return jsonify("Need to log in"), 400

    @app.route("/approveCourse", methods=['PUT'])
    def approve_course():
        try:
            try:
                if not request.json['role'] and not request.json['courseId'] and not request.json['approval']:
                    raise Exception
            except Exception as e:
                return jsonify("Need to sign in"), 400
            role = request.json['role']
            course_id = request.json['courseId']
            approval = request.json['approval']
            print("her2")
            return jsonify(CourseServiceImpl.approve_course(course_id, role, approval)), 200

        except Exception as e:
            return jsonify("Need to log in"), 400

# print(new_course.json())
# date = request.json['date']
# time = request.json['time']
# location = request.json['location']
# description = request.json['description']
# grading_format = request.json['gradingFormat']
# event_type = request.json['eventType']
# grade_required = request.json['gradeRequired']
# work_justification = request.json['workJustification']
# cost = request.json['cost']
# employee_id = request.json['employeeId']
# print(date, time, location, description, grading_format, event_type, grade_required, work_justification,
#       cost, employee_id)
# course = Course(None, date, time, location, description, cost, grading_format, event_type, grade_required,
#                 False, None, work_justification, employee_id)
