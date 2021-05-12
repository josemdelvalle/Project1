from services.employee_service import EmployeeService
from daos.employee_dao_impl import EmployeeDAOImpl
from models.employee_credentials import EmployeeCredentials


class EmployeeServiceImpl(EmployeeService):
    @classmethod
    def get_employee_role(cls, employee_id):
        try:
            return EmployeeDAOImpl.get_employee_role(employee_id)
        except Exception as e:
            return "Invalid user name or password", 400

    @classmethod
    def get_employee_by_id(cls, employee_id):
        try:
            return EmployeeDAOImpl.get_employee_by_id(employee_id)
        except Exception as e:
            return "Invalid user name or password", 400

    @classmethod
    def authenticate_employee(cls, user_name, password):
        try:
            if type(user_name) == str and type(password) == str:
                response = EmployeeDAOImpl.authenticate_employee(user_name, password)
                if type(response) == EmployeeCredentials:
                    return response
            else:
                raise ValueError
        except ValueError as e:
            return "Invalid Input", 400
