from abc import abstractmethod, ABC


class EmployeeService(ABC):

    @abstractmethod
    def authenticate_employee(self,user_name, password):
        pass

    @abstractmethod
    def get_employee_by_id(self, employee_id):
        pass

    @abstractmethod
    def get_employee_role(self, employee_id):
        pass


