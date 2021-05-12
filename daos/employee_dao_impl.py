from daos.employee_dao import EmployeeDAO
from util.db_connection import connection
from models.employee import Employee
from models.employee_credentials import EmployeeCredentials


class EmployeeDAOImpl(EmployeeDAO):
    @classmethod
    def get_employee_role(cls, employee_id):
        try:
            sql = "select * from departments where emloyee_id = %s"
            cursor = connection.cursor()
            cursor.execute(sql, [employee_id])
            record = cursor.fetchone()
            if not record:
                return "employee"
            role = record[2]
            return role
        except Exception as e:
            return "No employee found", 400

    @classmethod
    def get_employee_by_id(cls, employee_id):
        try:
            sql = "select * from employees where id = %s"
            cursor = connection.cursor()
            cursor.execute(sql, [employee_id])
            record = cursor.fetchone()
            employee = Employee(record[0], record[1], record[2], record[3], record[4])
            return employee
        except Exception as e:
            return "Invalid user name or password", 400

    @classmethod
    def get_all_employees(cls):
        pass

    @classmethod
    def authenticate_employee(cls, user_name, password):
        try:
            sql = f"SELECT * FROM employee_credentials WHERE user_name= '{user_name}' AND password_ ='{password}';"
            cursor = connection.cursor()
            cursor.execute(sql)
            record = cursor.fetchone()
            credentials = EmployeeCredentials(record[0], record[1], record[2], record[3])
            return credentials
        except Exception as e:
            return "Invalid user name or password", 400
