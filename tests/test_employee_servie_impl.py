import unittest
from services.employee_service_impl import EmployeeServiceImpl
from models.employee_credentials import EmployeeCredentials


class TestEmployeeServiceImpl(unittest.TestCase):

    def test_authenticate_employee(self):
        assert EmployeeServiceImpl.authenticate_employee('Jose', 'Del Valle').user_name == EmployeeCredentials(1, 'Jose',
                                                                                                           'Del Valle',
                                                                                                           1).user_name
        assert EmployeeServiceImpl.authenticate_employee(2, 1) == ("Invalid Input", 400)


if __name__ == '__main__':
    unittest.main()
