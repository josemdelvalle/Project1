from abc import abstractmethod, ABC


class CourseService(ABC):

    @abstractmethod
    def add_course(self, course):
        pass

    @abstractmethod
    def approve_course(self, course_id, role, approval):
        pass

    @abstractmethod
    def get_all_courses(self, employee_id, role, department):
        pass

    @abstractmethod
    def get_all_courses_by_employee_id(self, employee_id):
        pass

    @abstractmethod
    def add_course_to_employee(self, employee_id, course):
        pass

    @abstractmethod
    def get_course_approval(self, course_id):
        pass

    @abstractmethod
    def add_course_approval(self, course_id, role):
        pass

    @abstractmethod
    def get_course_notifications(self, course_id):
        pass

    @abstractmethod
    def add_course_notifications(self, course_id, role):
        pass
