from services.course_service import CourseService
from daos.course_dao_impl import CourseDAOImpl


class CourseServiceImpl(CourseService):

    @classmethod
    def add_course(cls, course):
        try:
            return CourseDAOImpl.add_course(course)
        except Exception as e:
            return "Invalid Input", 400

    @classmethod
    def get_all_courses(cls, employee_id, role, department):
        try:
            return CourseDAOImpl.get_all_courses(employee_id, role, department)
        except Exception as e:
            return "No courses found"

    @classmethod
    def approve_course(cls, course_id, role , approval):
        try:
            print("ALOA")
            return CourseDAOImpl.approve_course(course_id, role , approval), 200
        except Exception as e:
            return "No courses found", 404

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
