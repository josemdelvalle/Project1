class Employee:
    def __init__(self, employee_id=None, name=None, last_name=None, reimbursment=0, deparment=None, role=None):
        self.employee_id = employee_id
        self.name = name
        self.last_name = last_name
        self.reimbursment = reimbursment
        self.deparment = deparment
        self.role = role

    def json(self):
        return {
            'employeeId': self.employee_id,
            'name': self.name,
            'lastName': self.last_name,
            'reimbursment': float(self.reimbursment),
            'department': self.deparment,
            'role': self.role
        }

    @staticmethod
    def json_parse(json):
        employee = Employee()
        employee.employee_id = json["employeeId"]
        employee.name = json["name"]
        employee.last_name = json["lastName"]
        employee.reimbursment = json["reimbursment"]
        employee.deparment = json["deparment"]
        employee.role = json["role"]
        return employee
