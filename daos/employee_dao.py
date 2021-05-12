from abc import abstractmethod, ABC


class EmployeeDAO(ABC):
    @abstractmethod
    def get_employee_role(self, employee_id):
        pass

    @abstractmethod
    def get_employee_by_id(self, employee_id):
        pass

    @abstractmethod
    def get_all_employees(self):
        pass

    @abstractmethod
    def authenticate_employee(self, user_name, password):
        pass
