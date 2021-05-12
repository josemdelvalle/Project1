from daos.course_dao import CourseDAO
from daos.employee_dao import EmployeeDAO
from models.course import Course
from util.db_connection import connection
from models.employee_credentials import EmployeeCredentials


class CourseDAOImpl(CourseDAO):
    @classmethod
    def approve_course(cls, course_id, role, approval):
        try:

            print("HEREE9", course_id, role, approval)
            if role == "supervisor":
                sql = "UPDATE project1.courses SET supervisor_approval = %s  where id = %s "
                cursor = connection.cursor()
                cursor.execute(sql, [approval, course_id])
                connection.commit()
                return "resource updated successfully", 204
            elif role == "department head":
                sql = "UPDATE project1.courses SET supervisor_approval = %s , department_head_approval = %s where id = %s; "
                cursor = connection.cursor()
                cursor.execute(sql, [approval,approval, course_id])

                connection.commit()
                print("jnijnkjnkj")
                return "resource updated successfully", 200
            elif role == "benco":
                sql = "UPDATE project1.courses SET supervisor_approval = %s , department_head_approval = %s, benco_approval = %s where id = %s "
                cursor = connection.cursor()
                cursor.execute(sql, [approval,approval,approval,course_id])
                connection.commit()
                return "resource updated successfully", 204
            else:
                return "You don't have the authorization", 401
        except Exception as e:
            return "You don't have the authorization", 401

    @classmethod
    def add_course(cls, course):
        try:
            if course:
                print(course.grade_required)
                print(course.work_justification)
                sql = "insert into project1.courses values (default, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor = connection.cursor()
                cursor.execute(sql, [course.date,
                                     course.time,
                                     course.location_,
                                     course.description,
                                     course.cost_,
                                     course.grading_format,
                                     course.event_type,
                                     course.grade_required,
                                     course.urgent,
                                     course.grade,
                                     course.work_justification,
                                     course.employee_id,
                                     course.supervisor_approval,
                                     course.department_head_approval,
                                     course.benco_approval])
                connection.commit()
                return "Record inserted", 200
            else:
                return "Invalid Input", 400
        except Exception as e:

            return "Invalid Input", 400

    @classmethod
    def get_all_courses(cls, employee_id, role, department):
        if role == 'supervisor' or role == 'department head':
            sql = "select id from employees where deparment = %s;"  # lista de empleados/ luego la lista para los cursos
            cursor = connection.cursor()
            cursor.execute(sql, [department])
            employee_ids = cursor.fetchall()
            sql = "select * from courses where employee_id = ANY( %s);"
            cursor = connection.cursor()
            cursor.execute(sql, [employee_ids])
            record = cursor.fetchall()
            courses = []
            for course in record:
                courses.append(
                    Course(course[0], course[1], course[2], course[3], course[4], course[5], course[6], course[7],
                           course[8]
                           , course[9], course[10], course[11], course[12], course[13], course[14], course[15]).json())

            return courses
        elif role == 'benco':
            sql = "select * from courses;"
            cursor = connection.cursor()
            cursor.execute(sql, [employee_id])
            record = cursor.fetchall()
            courses = []
            for course in record:
                courses.append(
                    Course(course[0], course[1], course[2], course[3], course[4], course[5], course[6], course[7],
                           course[8]
                           , course[9], course[10], course[11], course[12], course[13], course[14], course[15]).json())

            return courses

        else:
            sql = "select * from courses where employee_id = %s;"
            cursor = connection.cursor()
            cursor.execute(sql, [employee_id])
            record = cursor.fetchall()
            courses = []
            for course in record:
                courses.append(
                    Course(course[0], course[1], course[2], course[3], course[4], course[5], course[6], course[7],
                           course[8]
                           , course[9], course[10], course[11], course[12], course[13], course[14], course[15]).json())

            return courses

    @classmethod
    def get_all_courses_by_employee_id(cls, employee_id):
        pass

    @classmethod
    def add_course_to_employee(cls, employee_id, course):
        pass

    @classmethod
    def get_course_approval(cls, course_id):
        pass

    @classmethod
    def add_course_approval(cls, course_id, role):
        pass

    @classmethod
    def get_course_notifications(cls, course_id):
        pass

    @classmethod
    def add_course_notifications(cls, course_id, role):
        pass


CourseDAOImpl.get_all_courses(1, "supervisor", 'science')
