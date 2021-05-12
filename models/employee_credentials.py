class EmployeeCredentials:
    def __init__(self, employee_credentials_id=None, user_name=None, password=None, employee_id=None):
        self.employee_credentials_id = employee_credentials_id
        self.user_name = user_name
        self.password = password
        self.employee_id = employee_id

    def json(self):
        return {
            'employeeCredentialsId': self.employee_credentials_id,
            'userName': self.user_name,
            'password': self.password,
            'employeeId': self.employee_id

        }

    @staticmethod
    def json_parse(json):
        employee_credentials = EmployeeCredentials()
        employee_credentials.employee_credentials_id = json["employeeCredentialsId"]
        employee_credentials.user_name = json["userName"]
        employee_credentials.password = json["password"]
        employee_credentials.employee_id = json["employeeId"]

        return employee_credentials
