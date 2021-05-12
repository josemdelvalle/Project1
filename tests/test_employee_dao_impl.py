import unittest
from daos.employee_dao_impl import EmployeeDAOImpl
from models.employee_credentials import EmployeeCredentials


class TestEmployeeDAOImpl(unittest.TestCase):

    def test_authenticate_employee(self):
        assert EmployeeDAOImpl.authenticate_employee('Jose', 'Del Valle').user_name == EmployeeCredentials(1, 'Jose', 'Del Valle', 1).user_name
        assert EmployeeDAOImpl.authenticate_employee(2, 1) == ('No record Found', 204)


if __name__ == '__main__':
    unittest.main()
