import unittest
from daos.course_dao_impl import CourseDAOImpl
from models.course import Course


class TestCourseDAOImpl(unittest.TestCase):
    def test_add_course(self):
        course1 = Course(course_id=None, date='2021-01-01', time='19:30', location_='Miami',
                         description='Server Maintenance', cost_=1000
                         , grading_format='Pass/Fail', event_type='Technical Training', grade_required='P',
                         urgent=False, grade=None, work_justification='Need training for new servers', employee_id=1)

        assert CourseDAOImpl.add_course(course1) == ('Record inserted', 200)
        assert CourseDAOImpl.add_course(2) == ("Invalid Input", 400)


if __name__ == '__main__':
    unittest.main()
